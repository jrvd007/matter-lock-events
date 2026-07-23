"""Matter Door Lock translator."""

from __future__ import annotations

import logging

from chip.clusters import Objects as clusters
from matter_server.common.models import MatterNodeEvent

from .door_lock import (
    LockCredential,
    LockOperation,
)

_LOGGER = logging.getLogger(__name__)


def translate_door_lock_operation(
    event: MatterNodeEvent,
) -> LockOperation | None:
    """Translate a Matter Door Lock event."""

    data = event.data or {}

    try:
        operation_type = (
            clusters.DoorLock.Enums.LockOperationTypeEnum(
                data["lockOperationType"]
            )
        )

        operation_source = (
            clusters.DoorLock.Enums.OperationSourceEnum(
                data["operationSource"]
            )
        )

    except (KeyError, ValueError) as err:
        _LOGGER.warning(
            "Unable to translate Door Lock event: %s",
            err,
        )
        return None

    credentials: list[LockCredential] = []

    for credential in data.get("credentials") or ():

        try:
            credentials.append(
                LockCredential(
                    credential_type=(
                        clusters.DoorLock.Enums.CredentialTypeEnum(
                            credential["credentialType"]
                        )
                    ),
                    credential_index=credential["credentialIndex"],
                )
            )

        except (KeyError, ValueError) as err:
            _LOGGER.warning(
                "Ignoring invalid credential: %s",
                err,
            )

    return LockOperation(
        node_id=event.node_id,
        endpoint_id=event.endpoint_id,
        operation_type=operation_type,
        operation_source=operation_source,
        user_index=data.get("userIndex"),
        credentials=tuple(credentials),
    )