"""Manager for Matter Lock Events."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from homeassistant.core import HomeAssistant

from .exceptions import MatterLockEventsError
from .matter_runtime import async_get_adapter

if TYPE_CHECKING:
    from homeassistant.components.matter.adapter import MatterAdapter

_LOGGER = logging.getLogger(__name__)


class MatterLockEventsManager:
    """Coordinates the integration lifecycle."""

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the manager."""
        self.hass = hass
        self._adapter: MatterAdapter | None = None

    async def async_initialize(self) -> None:
        """Initialize the integration."""

        try:
            self._adapter = async_get_adapter(self.hass)

        except MatterLockEventsError:
            _LOGGER.exception(
                "Unable to acquire the Matter runtime."
            )
            raise

        _LOGGER.info("Matter runtime acquired successfully.")

        _LOGGER.debug(
            "Matter adapter: %s",
            type(self._adapter).__name__,
        )