"""Matter Lock Events integration."""

from __future__ import annotations

import logging

from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .manager import MatterLockEventsManager

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the Matter Lock Events integration."""

    _LOGGER.info("Setting up Matter Lock Events")

    manager = MatterLockEventsManager(hass)

    await manager.async_initialize()

    hass.data[DOMAIN] = manager

    _LOGGER.info("Matter Lock Events initialized")

    return True