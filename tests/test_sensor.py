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


async def test_setup_platform_yaml(hass):
    """YAML setup must handle the immutable NodeDictClass config (#49)."""
    try:
        from homeassistant.util.yaml.objects import NodeDictClass
    except ImportError:  # older Home Assistant
        from homeassistant.util.yaml import NodeDictClass

    from custom_components.nfl.sensor import async_setup_platform

    # A real YAML config object; attributes cannot be assigned onto it, which is
    # exactly what broke the previous implementation on HA 2024.05+.
    config = NodeDictClass()
    config.update({"platform": "nfl", "name": "NFL", "team_id": "SEA", "timeout": 120})

    added = []

    def _add_entities(entities, update_before_add=False):
        added.extend(entities)

    with patch(
        "custom_components.nfl.NFLDataUpdateCoordinator.async_refresh",
        new=AsyncMock(return_value=None),
    ):
        await async_setup_platform(hass, config, _add_entities)
    await hass.async_block_till_done()

    # One sensor created, and the coordinator registered under a slugified id
    # derived from the team without mutating the original config object.
    assert len(added) == 1
    assert "sea" in hass.data[DOMAIN]
