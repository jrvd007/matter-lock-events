"""Home Assistant event payload adapter."""

from __future__ import annotations

from typing import Any

from enum import Enum

from .door_lock import (
    LockOperation, 
    LockOperationError,
    DoorLockAlarm,
)

from .const import (
    API_VERSION,
    FIELD_API_VERSION,
    FIELD_NODE_ID,
    FIELD_ENDPOINT_ID,
    FIELD_ENTITY_ID,
    FIELD_OPERATION,
    FIELD_OPERATION_ID,
    FIELD_SOURCE,
    FIELD_SOURCE_ID,
    FIELD_USER_INDEX,
    FIELD_USER_NAME,
    FIELD_FABRIC_INDEX,
    FIELD_SOURCE_NODE,
    FIELD_CREDENTIALS,
    FIELD_CREDENTIAL_TYPE,
    FIELD_CREDENTIAL_TYPE_ID,
    FIELD_CREDENTIAL_INDEX,
    FIELD_ERROR,
    FIELD_ERROR_ID,
    FIELD_ALARM,
    FIELD_ALARM_ID,
)

import re

def _enum_name(value: Enum) -> str:
    """Convert a Matter enum into a Home Assistant event value."""

    name = value.name.removeprefix("k")
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()
    
def serialize_operation(
    operation: LockOperation,
    entity_id: str | None = None,
    user: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Convert a LockOperation into a Home Assistant event payload."""

    payload = _serialize_common_operation(operation)

    payload.update(
        {
            FIELD_ENTITY_ID: entity_id,
            FIELD_USER_NAME: (
                user["user_name"] 
                if user is not None 
                else None
            )
        }
    )
    return payload

def serialize_operation_error(
    operation: LockOperationError,
    entity_id: str | None = None,
    user: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Convert a LockOperationError into a Home Assistant event payload."""

    payload = _serialize_common_operation(operation)

    payload.update(
        {
            FIELD_ENTITY_ID: entity_id,
            FIELD_USER_NAME: user["user_name"] if user else None,
            FIELD_ERROR: _enum_name(operation.operation_error),
            FIELD_ERROR_ID: int(operation.operation_error),
        }
    )

    return payload

def serialize_alarm(
    operation: DoorLockAlarm,
    entity_id: str | None = None,
) -> dict[str, Any]:
    """Convert a DoorLockAlarm into a Home Assistant event payload."""

    return {
        FIELD_API_VERSION: API_VERSION,
        
        FIELD_NODE_ID: operation.node_id,
        FIELD_ENDPOINT_ID: operation.endpoint_id,

        FIELD_ENTITY_ID: entity_id,

        FIELD_ALARM: _enum_name(operation.alarm_code),
        FIELD_ALARM_ID: int(operation.alarm_code),
    }

def _serialize_common_operation(
    operation,
) -> dict[str, Any]:
    """Return the base of all the operations handled"""

    return {
        FIELD_API_VERSION: API_VERSION,

        FIELD_NODE_ID: operation.node_id,
        FIELD_ENDPOINT_ID: operation.endpoint_id,

        FIELD_OPERATION: _enum_name(operation.operation_type),
        FIELD_OPERATION_ID: int(operation.operation_type),

        FIELD_SOURCE: _enum_name(operation.operation_source),
        FIELD_SOURCE_ID: int(operation.operation_source),

        FIELD_USER_INDEX: operation.user_index,

        FIELD_FABRIC_INDEX: operation.fabric_index,

        FIELD_SOURCE_NODE: operation.source_node,

        FIELD_CREDENTIALS: [
                    {
                        FIELD_CREDENTIAL_TYPE: _enum_name(credential.credential_type),
                        FIELD_CREDENTIAL_TYPE_ID: int(credential.credential_type),
                        FIELD_CREDENTIAL_INDEX: credential.credential_index,
                    }
                    for credential in operation.credentials
                ],
    }