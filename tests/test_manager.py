"""Tests for manager.py."""

from types import SimpleNamespace
from unittest.mock import Mock

from chip.clusters import Objects as clusters

from custom_components.matter_lock_events.const import EVENT_OPERATION
from custom_components.matter_lock_events.manager import MatterLockEventsManager


class FakeBus:
    def __init__(self) -> None:
        self.async_fire = Mock()


class FakeHass:
    def __init__(self) -> None:
        self.bus = FakeBus()


def test_handle_node_event_fires_home_assistant_event(
    monkeypatch,
) -> None:
    """Manager publishes the serialized Home Assistant event."""

    hass = FakeHass()
    manager = MatterLockEventsManager(hass)

    fake_operation = object()
    fake_payload = {"operation": "unlock", "source": "remote"}

    monkeypatch.setattr(
        "custom_components.matter_lock_events.manager.translate_door_lock_operation",
        lambda event: fake_operation,
    )
    monkeypatch.setattr(
        "custom_components.matter_lock_events.manager.serialize_operation",
        lambda operation: fake_payload,
    )

    event = SimpleNamespace(
        cluster_id=clusters.DoorLock.id,
        event_id=clusters.DoorLock.Events.LockOperation.event_id,
        node_id=23,
        endpoint_id=1,
        data={},
    )

    manager._handle_node_event(SimpleNamespace(), event)

    hass.bus.async_fire.assert_called_once_with(
        EVENT_OPERATION,
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