"""Home Assistant event payload adapter."""

from __future__ import annotations

from typing import Any

from enum import Enum

from .door_lock import LockOperation

def _enum_name(value: Enum) -> str:
    """Convert a Matter enum into a Home Assistant event value."""

    return value.name.removeprefix("k").lower()
    
def serialize_operation(
    operation: LockOperation,
) -> dict[str, Any]:
    """Convert a LockOperation into a Home Assistant event payload."""

    return {
        "api_version": 1,
        
        "node_id": operation.node_id,
        "endpoint_id": operation.endpoint_id,

        "operation": _enum_name(operation.operation_type),
        "operation_id": int(operation.operation_type),

        "source": _enum_name(operation.operation_source),
        "source_id": int(operation.operation_source),

        "user_index": operation.user_index,

        "fabric_index": operation.fabric_index,

        "source_node": operation.source_node,

        "credentials": [
            {
                "credential_type": _enum_name(credential.credential_type),
                "credential_type_id": int(credential.credential_type),
                "credential_index": credential.credential_index,
            }
            for credential in operation.credentials
        ],
    }