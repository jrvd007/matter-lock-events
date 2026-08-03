"""Matter Lock Events integration."""

from __future__ import annotations

import logging

_LOGGER = logging.getLogger(__name__)

from typing import TYPE_CHECKING, Any

from .const import DOMAIN, NAME, __version__

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.core import HomeAssistant

    from .models import MatterLockEventsConfigEntry, MatterLockEventsData


async def async_setup(hass: HomeAssistant, config: dict[str, Any]) -> bool:
    """Set up the integration."""
    return True


async def async_setup_entry(
    hass: HomeAssistant,
    entry: MatterLockEventsConfigEntry,
) -> bool:
    """Set up a config entry."""
    from .manager import MatterLockEventsManager
    from .models import MatterLockEventsData

    _LOGGER.info("%s %s", NAME, __version__)
    _LOGGER.info("Initializing integration...")

    manager = MatterLockEventsManager(hass)
    await manager.async_initialize()

    entry.runtime_data = MatterLockEventsData(manager=manager)

    _LOGGER.info("Initialization complete.")
    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: MatterLockEventsConfigEntry,
) -> bool:
    """Unload the config entry."""
    await entry.runtime_data.manager.async_shutdown()
    _LOGGER.info("Integration unloaded.")
    return True