"""Tests for init."""

from datetime import timedelta
from unittest.mock import AsyncMock, patch

import pytest
from homeassistant.components.sensor import DOMAIN as SENSOR_DOMAIN
from homeassistant.const import CONF_NAME
from homeassistant.helpers.entity_registry import async_get
from homeassistant.helpers.update_coordinator import UpdateFailed
from homeassistant.setup import async_setup_component
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.nfl import (
    DEFAULT_SCAN_INTERVAL,
    LIVE_SCAN_INTERVAL,
    MIN_PREGAME_SCAN_INTERVAL,
    _LOGGER,
    _compute_update_interval,
    NFLDataUpdateCoordinator,
    async_get_state,
)
from custom_components.nfl.const import CONF_TEAM_ID, DOMAIN
from tests.const import CONFIG_DATA


async def test_setup_entry(
    hass,
):
    """Test settting up entities."""
    entry = MockConfigEntry(
        domain=DOMAIN,
        title="NFL",
        data=CONFIG_DATA,
    )

    entry.add_to_hass(hass)
    with patch(
        "custom_components.nfl.NFLDataUpdateCoordinator.async_refresh",
        new=AsyncMock(return_value=None),
    ):
        assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert len(hass.states.async_entity_ids(SENSOR_DOMAIN)) == 1
    entries = hass.config_entries.async_entries(DOMAIN)
    assert len(entries) == 1


async def test_unload_entry(hass):
    """Test unloading entities."""
    entry = MockConfigEntry(
        domain=DOMAIN,
        title="NFL",
        data=CONFIG_DATA,
    )

    entry.add_to_hass(hass)
    with patch(
        "custom_components.nfl.NFLDataUpdateCoordinator.async_refresh",
        new=AsyncMock(return_value=None),
    ):
        assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert len(hass.states.async_entity_ids(SENSOR_DOMAIN)) == 1
    entries = hass.config_entries.async_entries(DOMAIN)
    assert len(entries) == 1

    assert await hass.config_entries.async_unload(entries[0].entry_id)
    await hass.async_block_till_done()
    assert len(hass.states.async_entity_ids(SENSOR_DOMAIN)) == 1
    assert len(hass.states.async_entity_ids(DOMAIN)) == 0

    assert await hass.config_entries.async_remove(entries[0].entry_id)
    await hass.async_block_till_done()
    assert len(hass.states.async_entity_ids(SENSOR_DOMAIN)) == 0


def test_coordinator_passes_config_entry(hass):
    """Test the coordinator passes the config entry to Home Assistant."""
    entry = MockConfigEntry(
        domain=DOMAIN,
        title="NFL",
        data=CONFIG_DATA,
    )

    with patch(
        "custom_components.nfl.DataUpdateCoordinator.__init__",
        autospec=True,
        return_value=None,
    ) as mock_init:
        coordinator = NFLDataUpdateCoordinator(
            hass, entry.data, entry.data.get("timeout"), config_entry=entry
        )

    mock_init.assert_called_once_with(
        coordinator,
        hass,
        _LOGGER,
        config_entry=entry,
        name=CONFIG_DATA[CONF_NAME],
        update_interval=timedelta(minutes=10),
    )


def test_update_interval_live_is_fast():
    """A live game polls at the fast live cadence."""
    assert _compute_update_interval("IN", 0) == LIVE_SCAN_INTERVAL
    # Case-insensitive and independent of any kickoff value.
    assert _compute_update_interval("in", None) == LIVE_SCAN_INTERVAL


def test_update_interval_finished_or_idle_is_default():
    """Finished/idle states fall back to the default cadence."""
    for state in ("POST", "BYE", "NOT_FOUND", "", None):
        assert _compute_update_interval(state, None) == DEFAULT_SCAN_INTERVAL


def test_update_interval_imminent_kickoff_is_fast():
    """PRE within the imminent window (or past kickoff) polls fast."""
    # Already elapsed but still reported as PRE (ESPN lag).
    assert _compute_update_interval("PRE", -30) == MIN_PREGAME_SCAN_INTERVAL
    # Exactly at / just inside the 60s window.
    assert _compute_update_interval("PRE", 60) == MIN_PREGAME_SCAN_INTERVAL
    assert _compute_update_interval("PRE", 30) == MIN_PREGAME_SCAN_INTERVAL
    # Unknown kickoff time is treated as imminent.
    assert _compute_update_interval("PRE", None) == MIN_PREGAME_SCAN_INTERVAL


def test_update_interval_pregame_scales_and_converges():
    """Pre-game cadence halves the remaining time, clamped to sane bounds."""
    # Far out: capped at the default cadence, never longer.
    assert _compute_update_interval("PRE", 24 * 3600) == DEFAULT_SCAN_INTERVAL
    # Mid-range: half of the remaining time.
    assert _compute_update_interval("PRE", 600) == timedelta(seconds=300)
    assert _compute_update_interval("PRE", 200) == timedelta(seconds=100)
    # As kickoff approaches the interval keeps shrinking (monotonic), so the
    # final pre-game poll lands within seconds of kickoff.
    prev = DEFAULT_SCAN_INTERVAL
    for secs in (3600, 1800, 900, 300, 120, 61):
        current = _compute_update_interval("PRE", secs)
        assert current <= prev
        assert current >= MIN_PREGAME_SCAN_INTERVAL
        prev = current


async def test_async_get_state_raises_on_api_failure(hass):
    """A non-200 response must surface as UpdateFailed, not look like a bye (#61)."""

    class FakeResponse:
        status = 503

        async def json(self):
            return None

        async def __aenter__(self):
            return self

        async def __aexit__(self, *args):
            return None

    class FakeSession:
        def get(self, url, headers=None):
            return FakeResponse()

        async def __aenter__(self):
            return self

        async def __aexit__(self, *args):
            return None

    with patch("custom_components.nfl.aiohttp.ClientSession", return_value=FakeSession()):
        with pytest.raises(UpdateFailed, match="503"):
            await async_get_state(CONFIG_DATA)


async def test_async_get_state_sends_no_user_agent(hass):
    """ESPN 403s browser user agents, so we must not send one (#61)."""

    sent_headers = {}

    class FakeResponse:
        status = 200

        async def json(self):
            return {"events": [], "week": {}}

        async def __aenter__(self):
            return self

        async def __aexit__(self, *args):
            return None

    class FakeSession:
        def get(self, url, headers=None):
            sent_headers.update(headers or {})
            return FakeResponse()

        async def __aenter__(self):
            return self

        async def __aexit__(self, *args):
            return None

    with patch("custom_components.nfl.aiohttp.ClientSession", return_value=FakeSession()):
        values = await async_get_state(CONFIG_DATA)

    assert "User-Agent" not in sent_headers
    assert values["state"] == "NOT_FOUND"


# async def test_import(hass):
#     """Test importing a config."""
#     entry = MockConfigEntry(
#         domain=DOMAIN,
#         title="NFL",
#         data=CONFIG_DATA,
#     )
#     await async_setup_component(hass, "persistent_notification", {})
#     with patch(
#         "custom_components.nfl.async_setup_entry",
#         return_value=True,
#     ) as mock_setup_entry:

#         ent_reg = async_get(hass)
#         ent_entry = ent_reg.async_get_or_create(
#             "sensor", DOMAIN, unique_id="replaceable_unique_id", config_entry=entry
#         )
#         entity_id = ent_entry.entity_id
#         entry.add_to_hass(hass)
#         await hass.config_entries.async_setup(entry.entry_id)
#         assert entry.unique_id is None
#         assert ent_reg.async_get(entity_id).unique_id == entry.entry_id
