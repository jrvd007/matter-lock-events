"""
Translate Matter Server transport data into immutable domain models.

The Matter Server client API exposes Door Lock event data as
MatterNodeEvent.data (dict[str, Any]). This module is the only
component that understands the transport format and converts it
into the integration's domain model.
"""

from __future__ import annotations

import logging

from chip.clusters import Objects as clusters
from matter_server.common.models import MatterNodeEvent

from .const import (
    DATA_ALARM_CODE,
    DATA_CREDENTIAL_INDEX,
    DATA_CREDENTIAL_TYPE,
    DATA_CREDENTIALS,
    DATA_FABRIC_INDEX,
    DATA_LOCK_OPERATION_TYPE,
    DATA_OPERATION_ERROR,
    DATA_OPERATION_SOURCE,
    DATA_SOURCE_NODE,
    DATA_USER_INDEX,
)
from .door_lock import (
    DoorLockAlarm,
    LockCredential,
    LockOperation,
    LockOperationError,
)

_LOGGER = logging.getLogger(__name__)


def translate_door_lock_operation(
    event: MatterNodeEvent,
) -> LockOperation | None:
    """Translate a Matter Door Lock event."""

    data = event.data or {}

    try:
        operation_type = clusters.DoorLock.Enums.LockOperationTypeEnum(
            data[DATA_LOCK_OPERATION_TYPE]
        )

        operation_source = clusters.DoorLock.Enums.OperationSourceEnum(
            data[DATA_OPERATION_SOURCE]
        )

    except (KeyError, ValueError) as err:
        _LOGGER.warning(
            "Unable to translate Door Lock operation: %s",
            err,
        )
        return None

    credentials: list[LockCredential] = []

    for credential in data.get(DATA_CREDENTIALS) or ():
        try:
            credentials.append(
                LockCredential(
                    credential_type=(
                        clusters.DoorLock.Enums.CredentialTypeEnum(
                            credential[DATA_CREDENTIAL_TYPE]
                        )
                    ),
                    credential_index=credential[DATA_CREDENTIAL_INDEX],
                )
            )

        except (KeyError, ValueError) as err:
            _LOGGER.warning(
                "Ignoring invalid Door Lock credential: %s",
                err,
            )

    return LockOperation(
        node_id=event.node_id,
        endpoint_id=event.endpoint_id,
        operation_type=operation_type,
        operation_source=operation_source,
        user_index=data.get(DATA_USER_INDEX),
        fabric_index=data.get(DATA_FABRIC_INDEX),
        source_node=data.get(DATA_SOURCE_NODE),
        credentials=tuple(credentials),
    )


def translate_lock_operation_error(
    event: MatterNodeEvent,
) -> LockOperationError:
    """Translate a Matter LockOperationError event."""

    data = event.data or {}

    try:
        operation_type = clusters.DoorLock.Enums.LockOperationTypeEnum(
            data[DATA_LOCK_OPERATION_TYPE]
        )

        operation_source = clusters.DoorLock.Enums.OperationSourceEnum(
            data[DATA_OPERATION_SOURCE]
        )

    except (KeyError, ValueError) as err:
        _LOGGER.warning(
            "Unable to translate Door Lock operation: %s",
            err,
        )
        return None

    credentials: list[LockCredential] = []

    for credential in data.get(DATA_CREDENTIALS) or ():
        try:
            credentials.append(
                LockCredential(
                    credential_type=(
                        clusters.DoorLock.Enums.CredentialTypeEnum(
                            credential[DATA_CREDENTIAL_TYPE]
                        )
                    ),
                    credential_index=credential[DATA_CREDENTIAL_INDEX],
                )
            )

        except (KeyError, ValueError) as err:
            _LOGGER.warning(
                "Ignoring invalid Door Lock credential: %s",
                err,
            )

    return LockOperationError(
        node_id=event.node_id,
        endpoint_id=event.endpoint_id,
        operation_type=operation_type,
        operation_source=operation_source,
        operation_error=clusters.DoorLock.Enums.OperationErrorEnum(
            data[DATA_OPERATION_ERROR]
        ),
        user_index=data.get(DATA_USER_INDEX),
        fabric_index=data.get(DATA_FABRIC_INDEX),
        source_node=data.get(DATA_SOURCE_NODE),
        credentials=tuple(credentials),
    )


def translate_door_lock_alarm(
    event: MatterNodeEvent,
) -> DoorLockAlarm | None:
    """Translate a Matter DoorLockAlarm event."""

    data = event.data or {}

    return DoorLockAlarm(
        node_id=event.node_id,
        endpoint_id=event.endpoint_id,
        alarm_code=clusters.DoorLock.Enums.AlarmCodeEnum(data[DATA_ALARM_CODE]),
    )
