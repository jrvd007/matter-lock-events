"""Matter Lock Events integration."""

from __future__ import annotations

import logging

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .const import NAME, __version__
from .manager import MatterLockEventsManager
from .models import (
    MatterLockEventsConfigEntry,
    MatterLockEventsData,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup(
    hass: HomeAssistant,
    config,
) -> bool:
    """Set up the integration."""

    _LOGGER.info("%s %s", NAME, __version__)

    return True


async def async_setup_entry(
    hass: HomeAssistant,
    entry: MatterLockEventsConfigEntry,
) -> bool:
    """Set up a config entry."""

    _LOGGER.info("Initializing integration...")

    manager = MatterLockEventsManager(hass)

    await manager.async_initialize()

    entry.runtime_data = MatterLockEventsData(
        manager=manager,
    )

    _LOGGER.info("Initialization complete.")

    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: MatterLockEventsConfigEntry,
) -> bool:
    """Unload the config entry."""

    _LOGGER.info("Unloading integration.")

    return True