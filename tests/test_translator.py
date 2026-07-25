"""Tests for translator.py."""

from chip.clusters import Objects as clusters
from matter_server.common.helpers.util import dataclass_from_dict
from matter_server.common.models import MatterNodeEvent

from custom_components.matter_lock_events.translator import (
    translate_door_lock_operation,
)

from .fixtures.schlage_sense_pro_events import REMOTE_UNLOCK

def test_translate_remote_unlock() -> None:
    """Translate a remote unlock event."""

    # Arrange

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

    # Act

    operation = translate_door_lock_operation(event)

    # Assert

    assert operation is not None

    assert operation.node_id == 23
    assert operation.endpoint_id == 1

    assert (
        operation.operation_type
        == clusters.DoorLock.Enums.LockOperationTypeEnum.kUnlock
    )

    assert (
        operation.operation_source
        == clusters.DoorLock.Enums.OperationSourceEnum.kRemote
    )

    assert operation.user_index is None
    assert operation.fabric_index == 2
    assert operation.source_node == 112233

    assert operation.credentials == ()