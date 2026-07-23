"""Manager for Matter Lock Events."""

from __future__ import annotations



import logging
from collections.abc import Callable

from matter_server.common.models import EventType, MatterNodeEvent

from homeassistant.core import HomeAssistant

from homeassistant.components.matter.const import DOMAIN as MATTER_DOMAIN
from homeassistant.components.matter.helpers import MatterConfigEntry

from .const import NAME, __version__

from .translator import translate_door_lock_operation

_LOGGER = logging.getLogger(__name__)


class MatterLockEventsManager:
    """Coordinates Matter event subscriptions."""

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the manager."""
        self.hass = hass
        self._unsubscribe: Callable[[], None] | None = None

    async def async_initialize(self) -> None:
        """Initialize the manager."""

        _LOGGER.warning("%s %s", NAME, __version__)
        _LOGGER.warning("Searching for Matter integration...")

        matter_entries = self.hass.config_entries.async_loaded_entries(
            MATTER_DOMAIN
        )

        if not matter_entries:
            raise RuntimeError("Matter integration is not loaded.")

        matter_entry: MatterConfigEntry = matter_entries[0]

        _LOGGER.warning("Matter integration found.")

        matter_client = matter_entry.runtime_data.adapter.matter_client

        _LOGGER.warning("Subscribing to Matter node events...")

        self._unsubscribe = matter_client.subscribe_events(
            callback=self._handle_node_event,
            event_filter=EventType.NODE_EVENT,
        )

        _LOGGER.warning("Matter node event subscription established.")

    async def async_shutdown(self) -> None:
        """Shutdown the manager."""

        if self._unsubscribe is not None:
            _LOGGER.warning("Unsubscribing from Matter node events...")
            self._unsubscribe()
            self._unsubscribe = None

    def _handle_node_event(
        self,
        event_type: EventType,
        event: MatterNodeEvent,
    ) -> None:
        """Handle Matter node events."""
      
        if event.cluster_id != clusters.DoorLock.id:
            return

        if event.event_id != clusters.DoorLock.Events.LockOperation.event_id:
            return

        operation = translate_door_lock_operation(event)

        if operation is None:
            return

        _LOGGER.warning(
            (
                "\n"
                "========== Matter Door Lock Operation ==========\n"
                "Node ID: %s \n"
                "Endpoint: %s \n"
                "Operation: %s \n"
                "Source: %s \n"
                "User Index: %s \n"
                "Credentials: %s \n"
                "==============================================="
            ),
            operation.node_id,
            operation.endpoint_id,
            operation.operation_type.name,
            operation.operation_source.name,
            operation.user_index,
            [
                (
                    credential.credential_type.name,
                    credential.credential_index,
                )
                for credential in operation.credentials
            ],
        )