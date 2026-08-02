"""Tests for event_adapter.py."""

from chip.clusters import Objects as clusters

from custom_components.matter_lock_events.door_lock import (
    LockCredential,
    LockOperation,
    LockOperationError,
)
from custom_components.matter_lock_events.event_adapter import (
    serialize_operation,
    serialize_operation_error,
)


def test_serialize_unlock_remote() -> None:
    """Serialize a remote unlock operation."""

    operation = LockOperation(
        node_id=23,
        endpoint_id=1,
        operation_type=clusters.DoorLock.Enums.LockOperationTypeEnum.kUnlock,
        operation_source=clusters.DoorLock.Enums.OperationSourceEnum.kRemote,
        user_index=None,
        fabric_index=2,
        source_node=112233,
        credentials=(),
    )

    payload = serialize_operation(
        operation,                      
        entity_id="lock.sense_pro",
        user=None,
    )

    assert payload == {
        "api_version": 1,
        "entity_id": "lock.sense_pro",
        "node_id": 23,
        "endpoint_id": 1,
        "operation": "unlock",
        "operation_id": 1,
        "source": "remote",
        "source_id": 7,
        "user_index": None,
        "user_name":None,
        "fabric_index": 2,
        "source_node": 112233,
        "credentials": [],
    }


def test_serialize_lock_button() -> None:
    """Serialize a keypad lock operation."""

    operation = LockOperation(
        node_id=23,
        endpoint_id=1,
        operation_type=clusters.DoorLock.Enums.LockOperationTypeEnum.kLock,
        operation_source=clusters.DoorLock.Enums.OperationSourceEnum.kButton,
        user_index=None,
        fabric_index=None,
        source_node=None,
        credentials=(),
    )

    payload = serialize_operation(
        operation,
        entity_id="lock.sense_pro",
        user=None,
    )

    assert payload == {
        "api_version": 1,
        "node_id": 23,
        "endpoint_id": 1,
        "entity_id": "lock.sense_pro",
        "operation": "lock",
        "operation_id": 0,
        "source": "button",
        "source_id": 5,
        "user_index": None,
        "user_name":None,
        "fabric_index": None,
        "source_node": None,
        "credentials": [],
    }

def test_serialize_unlock_keypad() -> None:
    """Serialize a keypad unlock operation."""

    operation = LockOperation(
        node_id=23,
        endpoint_id=1,
        operation_type=clusters.DoorLock.Enums.LockOperationTypeEnum.kUnlock,
        operation_source=clusters.DoorLock.Enums.OperationSourceEnum.kKeypad,
        user_index=1,
        fabric_index=None,
        source_node=None,
        credentials=(
            LockCredential(
                credential_type=clusters.DoorLock.Enums.CredentialTypeEnum.kPin,
                credential_index=1,
            ),
        ),
    )

    payload = serialize_operation(
        operation,
        entity_id=None,
        user={
        "user_index": 1,
        "user_name": "John",
        },
    )

    assert payload == {
        "api_version": 1,
        "node_id": 23,
        "endpoint_id": 1,
        "entity_id": None,
        "operation": "unlock",
        "operation_id": 1,
        "source": "keypad",
        "source_id": 3,
        "user_index": 1,
        "user_name": "John",
        "fabric_index": None,
        "source_node": None,
        "credentials": [
            {
                "credential_type": "pin",
                "credential_type_id": 1,
                "credential_index": 1,
            }
        ],
    }

def test_serialize_lock_manual() -> None:
    """Serialize a manual thumbturn lock operation."""

    operation = LockOperation(
        node_id=23,
        endpoint_id=1,
        operation_type=clusters.DoorLock.Enums.LockOperationTypeEnum.kLock,
        operation_source=clusters.DoorLock.Enums.OperationSourceEnum.kManual,
        user_index=None,
        fabric_index=None,
        source_node=None,
        credentials=(),
    )

    payload = serialize_operation(
        operation,
        entity_id=None,
        user=None,
    )

    assert payload == {
        "api_version": 1,
        "node_id": 23,
        "endpoint_id": 1,
        "entity_id": None,
        "operation": "lock",
        "operation_id": 0,
        "source": "manual",
        "source_id": 1,
        "user_index": None,
        "user_name": None,
        "fabric_index": None,
        "source_node": None,
        "credentials": [],
    }

def test_serialize_operation_error() -> None:
    """Serialize a keypad unlock operation."""

    operation = LockOperationError(
        node_id=23,
        endpoint_id=1,
        operation_type=clusters.DoorLock.Enums.LockOperationTypeEnum.kUnlock,
        operation_source=clusters.DoorLock.Enums.OperationSourceEnum.kKeypad,
        operation_error=clusters.DoorLock.Enums.OperationErrorEnum.kInvalidCredential,
        user_index=None,
        fabric_index=None,
        source_node=None,
        credentials=(),
    )

    payload = serialize_operation_error(
        operation,
        entity_id="lock.sense_pro",
        user=None,
    )

    assert payload == {
        "api_version": 1,
        "node_id": 23,
        "endpoint_id": 1,
        "error": "invalidcredential",
        "error_id": 1,
        "entity_id": "lock.sense_pro",
        "operation": "unlock",
        "operation_id": 1,
        "source": "keypad",
        "source_id": 3,
        "user_index": None,
        "user_name": None,
        "fabric_index": None,
        "source_node": None,
        "credentials": [],
    }