"""Manager for Matter Lock Events."""

from __future__ import annotations

import logging

from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)


class MatterLockEventsManager:
    """Coordinates the integration lifecycle."""

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the manager."""
        self.hass = hass

    async def async_initialize(self) -> None:
        """Initialize the integration."""
        _LOGGER.info("Matter Lock Events manager started")