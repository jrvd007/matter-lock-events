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
from .const import DOMAIN

"""_LOGGER = logging.getLogger(f"custom_components.{DOMAIN}")"""
"""_LOGGER.warning("Logger name: %s", _LOGGER.name)"""

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

    _LOGGER.warning("Initializing integration...")

    manager = MatterLockEventsManager(hass)

    await manager.async_initialize()

    entry.runtime_data = MatterLockEventsData(
        manager=manager,
    )

    _LOGGER.warning("Initialization complete.")

    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: MatterLockEventsConfigEntry,
) -> bool:
    """Unload the config entry."""

    await entry.runtime_data.manager.async_shutdown()

    _LOGGER.warning("Integration unloaded.")

    return True