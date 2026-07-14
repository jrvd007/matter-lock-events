"""Manager for Matter Lock Events."""

from __future__ import annotations

import logging

from homeassistant.core import HomeAssistant

from .exceptions import MatterLockEventsError
from .matter_runtime import async_get_adapter

_LOGGER = logging.getLogger(__name__)


class MatterLockEventsManager:
    """Coordinates the integration lifecycle."""

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the manager."""
        self.hass = hass

    async def async_initialize(self) -> None:
        """Initialize the integration."""

        try:
            adapter = async_get_adapter(self.hass)

        except MatterLockEventsError:
            _LOGGER.exception(
                "Unable to acquire the Matter runtime."
            )
            raise

        _LOGGER.info(
            "Matter runtime acquired successfully."
        )

        #
        # Temporary until Commit #4
        #
        _LOGGER.debug(
            "Matter adapter: %s",
            type(adapter).__name__,
        )