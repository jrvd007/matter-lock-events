"""Matter Lock Events integration."""

from __future__ import annotations

import logging

_LOGGER = logging.getLogger(__name__)

from typing import TYPE_CHECKING, Any

from .const import DOMAIN, NAME, __version__
from .manager import MatterLockEventsManager

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.core import HomeAssistant



async def async_setup(hass: HomeAssistant, config: dict[str, Any]) -> bool:
    """Set up the integration."""
    return True


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
) -> bool:
    """Set up a config entry."""
    
    _LOGGER.info("%s %s", NAME, __version__)

    manager = MatterLockEventsManager(hass)
    await manager.async_initialize()

    entry.runtime_data = manager

    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
) -> bool:
    """Unload the config entry."""

    await entry.runtime_data.async_shutdown()
    
    return True