"""Test NFL Sensor"""

from unittest.mock import AsyncMock, patch

from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.nfl.const import DOMAIN
from tests.const import CONFIG_DATA


async def test_sensor(hass):

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

    assert "nfl" in hass.config.components
