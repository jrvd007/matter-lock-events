"""Manager for Matter Lock Events."""

from __future__ import annotations

import logging
from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from chip.clusters import Objects as clusters
from matter_server.common.models import EventType, MatterNodeEvent

from .const import (
    EVENT_OPERATION, 
    EVENT_OPERATION_ERROR,
    EVENT_ALARM,
    NAME, 
    __version__,
)
from .door_lock import (
    LockOperation,
    LockOperationError,
    DoorLockAlarm,
)
from .event_adapter import (
    serialize_operation,
    serialize_operation_error,
    serialize_alarm,
)
from .translator import (
    translate_door_lock_operation,
    translate_lock_operation_error,
    translate_door_lock_alarm,
)
from .entity_resolver import resolve_entity_id
from .lock_user_resolver import resolve_lock_user



if TYPE_CHECKING:
    from homeassistant.components.matter.helpers import MatterConfigEntry
    from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)


class MatterLockEventsManager:
    """Coordinates Matter event subscriptions."""

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the manager."""
        self.hass = hass
        self._unsubscribe: Callable[[], None] | None = None
        self._matter_client = None
        self._server_info = None
        
    async def async_initialize(self) -> None:
        """Initialize the manager."""

        _LOGGER.info("%s %s", NAME, __version__)
        _LOGGER.info("Searching for Matter integration...")

        matter_entries = self.hass.config_entries.async_loaded_entries(
            "matter"
        )

        if not matter_entries:
            raise RuntimeError("Matter integration is not loaded.")

        matter_entry: MatterConfigEntry = matter_entries[0]

        _LOGGER.info("Matter integration found.")

        matter_client = matter_entry.runtime_data.adapter.matter_client

        self._matter_client = matter_client
        self._server_info = matter_client.server_info

        _LOGGER.info("Subscribing to Matter node events...")

        self._unsubscribe = matter_client.subscribe_events(
            callback=self._handle_node_event,
            event_filter=EventType.NODE_EVENT,
        )

        _LOGGER.info("Matter node event subscription established.")



    async def async_shutdown(self) -> None:
        """Shutdown the manager."""

        if self._unsubscribe is not None:
            _LOGGER.info("Unsubscribing from Matter node events...")
            self._unsubscribe()
            self._unsubscribe = None

    def _fire_operation(
        self, 
        operation: LockOperation, 
        entity_id: str | None, 
        user: dict[str, Any] | None = None,
    ) -> None:
        """Fire a Home Assistant event for a lock operation."""
        event_data = serialize_operation(
            operation,
            entity_id=entity_id,
            user=user,
        )

        self.hass.bus.async_fire(
            EVENT_OPERATION,
            event_data,
        )

        _LOGGER.debug("Published Home Assistant event: %s", EVENT_OPERATION)

    def _fire_operation_error(
        self, 
        operation: LockOperationError, 
        entity_id: str | None, 
        user: dict[str, Any] | None = None,
    ) -> None:
        """Fire a Home Assistant event for a lock operation error."""
        event_data = serialize_operation_error(
            operation,
            entity_id=entity_id,
            user=user,
        )
    
        self.hass.bus.async_fire(
            EVENT_OPERATION_ERROR,
            event_data,
        )
    
        _LOGGER.debug("Published Home Assistant event: %s", EVENT_OPERATION_ERROR)

    def _fire_alarm(
        self, 
        operation: DoorLockAlarm, 
        entity_id: str | None, 
    ) -> None:
        """Fire a Home Assistant event for a door lock alarm."""
        event_data = serialize_alarm(
            operation,
            entity_id=entity_id,
        )
        
        self.hass.bus.async_fire(
            EVENT_ALARM,
            event_data,
        )
        
        _LOGGER.debug("Published Home Assistant event: %s", EVENT_ALARM)

    def _handle_node_event(
        self,
        event_type: EventType,
        event: MatterNodeEvent,
    ) -> None:
        """Handle Matter node events."""

        if event.cluster_id != clusters.DoorLock.id:
            return


        if event.event_id == clusters.DoorLock.Events.LockOperation.event_id:
            operation = translate_door_lock_operation(event)

            if operation is None:
                return

            self.hass.async_create_task(
                self._async_handle_lock_operation(operation)
            )
            return

        elif event.event_id == clusters.DoorLock.Events.LockOperationError.event_id:
            operation = translate_lock_operation_error(event)

            if operation is None:
                return

            self.hass.async_create_task(
                self._async_handle_lock_operation_error(operation)
            )
            return

        elif event.event_id == clusters.DoorLock.Events.DoorLockAlarm.event_id:
            alarm = translate_door_lock_alarm(event)

            if alarm is None:
                return

            self.hass.async_create_task(
                self._async_handle_alarm(alarm)
            )
            return

        
    async def _async_handle_lock_operation(
        self,
        operation: LockOperation,
    ) -> None:
        """Resolve additional information and fire the HA event."""

        entity_id = resolve_entity_id(
            self.hass,
            self._server_info,
            self._matter_client,
            operation.node_id,
            operation.endpoint_id,
        )

        user = await resolve_lock_user(
            self.hass,
            self._server_info,
            self._matter_client,
            operation.node_id,
            operation.endpoint_id,
            operation.user_index,
        )

        self._fire_operation(
            operation,
            entity_id,
            user=user,
        )

    async def _async_handle_lock_operation_error(
            self,
            operation: LockOperationError,
        ) -> None:
            """Resolve additional information and fire the HA event for an error."""
    
            entity_id = resolve_entity_id(
                self.hass,
                self._server_info,
                self._matter_client,
                operation.node_id,
                operation.endpoint_id,
            )
    
            user = await resolve_lock_user(
                self.hass,
                self._server_info,
                self._matter_client,
                operation.node_id,
                operation.endpoint_id,
                operation.user_index,
            )
    
            self._fire_operation_error(
                operation,
                entity_id,
                user=user,
            )

    async def _async_handle_alarm (
            self,
            operation: DoorLockAlarm,
    ) -> None:
        """Resolve additional information and fire the HA event for an alarm."""
        entity_id = resolve_entity_id(
            self.hass,
            self._server_info,
            self._matter_client,
            operation.node_id,
            operation.endpoint_id,
        )
               
        self._fire_alarm(
            operation,
            entity_id,
        )