"""Tests for translator.py."""

from chip.clusters import Objects as clusters
from matter_server.common.helpers.util import dataclass_from_dict
from matter_server.common.models import MatterNodeEvent

from custom_components.matter_lock_events.translator import (
    translate_door_lock_operation,
    translate_lock_operation_error,
    translate_door_lock_alarm,
)

from tests.fixtures.schlage_sense_pro_events import (
    KEYPAD_LOCK, 
    REMOTE_UNLOCK,
    KEYPAD_UNLOCK,
    MANUAL_THUMBTURN_LOCK,
    WRONG_PIN,
)

def test_translate_remote_unlock() -> None:
    """Translate a remote unlock event."""

    event = dataclass_from_dict(
        MatterNodeEvent,
        {
            "node_id": 23,
            "endpoint_id": 1,
            "cluster_id": clusters.DoorLock.id,
            "event_id": clusters.DoorLock.Events.LockOperation.event_id,
            "event_number": 1,
            "priority": 1,
            "timestamp": 0,
            "data": REMOTE_UNLOCK,
        },
    )

    operation = translate_door_lock_operation(event)

    assert operation is not None
    assert operation.node_id == 23
    assert operation.endpoint_id == 1
    assert operation.operation_type == clusters.DoorLock.Enums.LockOperationTypeEnum.kUnlock
    assert operation.operation_source == clusters.DoorLock.Enums.OperationSourceEnum.kRemote
    assert operation.user_index is None
    assert operation.fabric_index == 2
    assert operation.source_node == 112233
    assert operation.credentials == ()


def test_translate_keypad_lock() -> None:
    """Translate a keypad lock event."""

    event = dataclass_from_dict(
        MatterNodeEvent,
        {
            "node_id": 23,
            "endpoint_id": 1,
            "cluster_id": clusters.DoorLock.id,
            "event_id": clusters.DoorLock.Events.LockOperation.event_id,
            "event_number": 2,
            "priority": 1,
            "timestamp": 0,
            "data": KEYPAD_LOCK,
        },
    )

    operation = translate_door_lock_operation(event)

    assert operation is not None
    assert operation.node_id == 23
    assert operation.endpoint_id == 1
    assert operation.operation_type == clusters.DoorLock.Enums.LockOperationTypeEnum.kLock
    assert operation.operation_source == clusters.DoorLock.Enums.OperationSourceEnum.kButton
    assert operation.user_index is None
    assert operation.fabric_index is None
    assert operation.source_node is None
    assert operation.credentials == ()

def test_translate_keypad_unlock() -> None:
    """Translate a keypad unlock event."""

    event = dataclass_from_dict(
        MatterNodeEvent,
        {
            "node_id": 23,
            "endpoint_id": 1,
            "cluster_id": clusters.DoorLock.id,
            "event_id": clusters.DoorLock.Events.LockOperation.event_id,
            "event_number": 3,
            "priority": 1,
            "timestamp": 0,
            "data": KEYPAD_UNLOCK,
        },
    )

    operation = translate_door_lock_operation(event)

    assert operation is not None
    assert operation.node_id == 23
    assert operation.endpoint_id == 1
    assert operation.operation_type == clusters.DoorLock.Enums.LockOperationTypeEnum.kUnlock
    assert operation.operation_source == clusters.DoorLock.Enums.OperationSourceEnum.kKeypad
    assert operation.user_index == 1
    assert operation.fabric_index is None
    assert operation.source_node is None
    assert len(operation.credentials) == 1
    assert operation.credentials[0].credential_type == clusters.DoorLock.Enums.CredentialTypeEnum.kPin
    assert operation.credentials[0].credential_index == 1

def test_translate_manual_thumbturn_lock() -> None:
    """Translate a manual thumbturn lock event."""

    event = dataclass_from_dict(
        MatterNodeEvent,
        {
            "node_id": 23,
            "endpoint_id": 1,
            "cluster_id": clusters.DoorLock.id,
            "event_id": clusters.DoorLock.Events.LockOperation.event_id,
            "event_number": 4,
            "priority": 1,
            "timestamp": 0,
            "data": MANUAL_THUMBTURN_LOCK,
        },
    )

    operation = translate_door_lock_operation(event)

    assert operation is not None
    assert operation.node_id == 23
    assert operation.endpoint_id == 1
    assert operation.operation_type == clusters.DoorLock.Enums.LockOperationTypeEnum.kLock
    assert operation.operation_source == clusters.DoorLock.Enums.OperationSourceEnum.kManual
    assert operation.user_index is None
    assert operation.fabric_index is None
    assert operation.source_node is None
    assert operation.credentials == ()

def test_translate_lock_operation_error() -> None:
    """Translate a lock error."""

    event = dataclass_from_dict(
        MatterNodeEvent,
        {
            "node_id": 23,
            "endpoint_id": 1,
            "cluster_id": clusters.DoorLock.id,
            "event_id": clusters.DoorLock.Events.LockOperationError.event_id,
            "event_number": 1,
            "priority": 1,
            "timestamp": 0,
            "data": WRONG_PIN,
        },
    )

    operation = translate_lock_operation_error(event)

    assert operation is not None
    assert operation.node_id == 23
    assert operation.endpoint_id == 1
    assert operation.operation_type == clusters.DoorLock.Enums.LockOperationTypeEnum.kUnlock
    assert operation.operation_source == clusters.DoorLock.Enums.OperationSourceEnum.kKeypad
    assert operation.operation_error == clusters.DoorLock.Enums.OperationErrorEnum.kInvalidCredential
    assert operation.user_index is None
    assert operation.fabric_index is None
    assert operation.source_node is None
    assert operation.credentials == ()

def test_translate_door_lock_alarm() -> None:
    """Translate a lock alarm."""

    event = dataclass_from_dict(
        MatterNodeEvent,
        {
            "node_id": 23,
            "endpoint_id": 1,
            "event_id": clusters.DoorLock.Events.DoorLockAlarm.event_id,
            "data": {
                "alarmCode": 0,
            }
        },
    )

    alarm = translate_door_lock_alarm(event)

    assert alarm is not None
    assert alarm.node_id == 23
    assert alarm.endpoint_id == 1
    assert alarm.alarm_code == 0