"""Tests for manager.py."""

from types import SimpleNamespace
from unittest.mock import Mock
from unittest.mock import AsyncMock

from chip.clusters import Objects as clusters

from custom_components.matter_lock_events.const import EVENT_OPERATION, EVENT_OPERATION_ERROR, EVENT_ALARM
from custom_components.matter_lock_events.manager import MatterLockEventsManager

import asyncio

class FakeBus:
    def __init__(self) -> None:
        self.async_fire = Mock()


class FakeHass:
    def __init__(self) -> None:
        self.bus = FakeBus()

    def async_create_task(self, coro):
        return asyncio.run(coro)


def test_handle_node_event_fires_home_assistant_event(
    monkeypatch,
) -> None:
    """Manager publishes the serialized Home Assistant event."""

    hass = FakeHass()
    manager = MatterLockEventsManager(hass)
    manager._server_info = Mock()
    manager._matter_client = Mock()

    fake_operation = SimpleNamespace(
        node_id=23,
        endpoint_id=1,
        user_index=1,
    )

    fake_entity_id = "lock.sense_pro"

    fake_payload = {
        "operation": "unlock",
        "source": "remote",
        "entity_id": fake_entity_id,
    }

    monkeypatch.setattr(
        "custom_components.matter_lock_events.manager.translate_door_lock_operation",
        lambda event: fake_operation,
    )
    monkeypatch.setattr(
       "custom_components.matter_lock_events.manager.resolve_entity_id",
        lambda *args, **kwargs: fake_entity_id,
    )

    resolve_lock_user_mock = AsyncMock(
        return_value={
            "user_index": 1,
            "user_name": "John",
        }
    )

    monkeypatch.setattr(
        "custom_components.matter_lock_events.manager.resolve_lock_user",
        resolve_lock_user_mock,
    )

    serialize_mock = Mock(return_value=fake_payload)

    monkeypatch.setattr(
        "custom_components.matter_lock_events.manager.serialize_operation",
        serialize_mock,
    )

    event = SimpleNamespace(
        cluster_id=clusters.DoorLock.id,
        event_id=clusters.DoorLock.Events.LockOperation.event_id,
        node_id=23,
        endpoint_id=1,
        data={},
    )

    manager._handle_node_event(SimpleNamespace(), event)

    resolve_lock_user_mock.assert_awaited_once_with(
        hass,
        manager._server_info,
        manager._matter_client,
        23,
        1,
        1,
    )

    serialize_mock.assert_called_once_with(
        fake_operation,
        entity_id=fake_entity_id,
        user={
            "user_index": 1,
            "user_name": "John",
        },
    )

    hass.bus.async_fire.assert_called_once_with(
        EVENT_OPERATION,
        fake_payload,
    )

def test_handle_node_event_error_fires_home_assistant_event(
    monkeypatch,
) -> None:
    """Manager publishes the serialized Home Assistant event."""

    hass = FakeHass()
    manager = MatterLockEventsManager(hass)
    manager._server_info = Mock()
    manager._matter_client = Mock()

    fake_operation = SimpleNamespace(
        node_id=23,
        endpoint_id=1,
        user_index=None,
    )

    fake_entity_id = "lock.sense_pro"

    fake_payload = {
        "operation": "unlock",
        "source": "keypad",
        "entity_id": fake_entity_id,
        "error": "invalid_credential",
        "error_id": 1,
    }

    monkeypatch.setattr(
        "custom_components.matter_lock_events.manager.translate_lock_operation_error",
        lambda event: fake_operation,
    )
    monkeypatch.setattr(
       "custom_components.matter_lock_events.manager.resolve_entity_id",
        lambda *args, **kwargs: fake_entity_id,
    )
  

    serialize_mock = Mock(return_value=fake_payload)

    monkeypatch.setattr(
        "custom_components.matter_lock_events.manager.serialize_operation_error",
        serialize_mock,
    )

    event = SimpleNamespace(
        cluster_id=clusters.DoorLock.id,
        event_id=clusters.DoorLock.Events.LockOperationError.event_id,
        node_id=23,
        endpoint_id=1,
        data={},
    )

    manager._handle_node_event(SimpleNamespace(), event)
 
    serialize_mock.assert_called_once_with(
        fake_operation,
        entity_id=fake_entity_id,
        user=None,
    )

    hass.bus.async_fire.assert_called_once_with(
        EVENT_OPERATION_ERROR,
        fake_payload,
    )

def test_handle_node_event_alarm_fires_home_assistant_event(
    monkeypatch,
) -> None:
    """Manager publishes the serialized Home Assistant event."""

    hass = FakeHass()
    manager = MatterLockEventsManager(hass)
    manager._server_info = Mock()
    manager._matter_client = Mock()

    fake_operation = SimpleNamespace(
        node_id=23,
        endpoint_id=1,
    )

    fake_entity_id = "lock.sense_pro"

    fake_payload = {
        "entity_id": fake_entity_id,
        "alarm": "lock_jammed",
        "alarm_id": 0,
    }

    monkeypatch.setattr(
        "custom_components.matter_lock_events.manager.translate_door_lock_alarm",
        lambda event: fake_operation,
    )
    monkeypatch.setattr(
       "custom_components.matter_lock_events.manager.resolve_entity_id",
        lambda *args, **kwargs: fake_entity_id,
    )
  

    serialize_mock = Mock(return_value=fake_payload)

    monkeypatch.setattr(
        "custom_components.matter_lock_events.manager.serialize_alarm",
        serialize_mock,
    )

    event = SimpleNamespace(
        cluster_id=clusters.DoorLock.id,
        event_id=clusters.DoorLock.Events.DoorLockAlarm.event_id,
        node_id=23,
        endpoint_id=1,
        data={},
    )

    manager._handle_node_event(SimpleNamespace(), event)
 
    serialize_mock.assert_called_once_with(
        fake_operation,
        entity_id=fake_entity_id,
    )

    hass.bus.async_fire.assert_called_once_with(
        EVENT_ALARM,
        fake_payload,
    )

def test_handle_node_event_ignores_non_door_lock_event(monkeypatch) -> None:
    """Manager ignores unrelated Matter events."""

    hass = FakeHass()
    manager = MatterLockEventsManager(hass)

    translate_mock = Mock()
    serialize_mock = Mock()

    monkeypatch.setattr(
        "custom_components.matter_lock_events.manager.translate_door_lock_operation",
        translate_mock,
    )
    monkeypatch.setattr(
        "custom_components.matter_lock_events.manager.serialize_operation",
        serialize_mock,
    )

    event = SimpleNamespace(
        cluster_id=clusters.DoorLock.id + 1,
        event_id=clusters.DoorLock.Events.LockOperation.event_id,
        node_id=23,
        endpoint_id=1,
        data={},
    )

    manager._handle_node_event(SimpleNamespace(), event)

    translate_mock.assert_not_called()
    serialize_mock.assert_not_called()
    hass.bus.async_fire.assert_not_called()