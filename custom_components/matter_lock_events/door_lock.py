"""Door Lock domain models."""

from __future__ import annotations

from dataclasses import dataclass

from chip.clusters import Objects as clusters


@dataclass(frozen=True, slots=True)
class LockCredential:
    """Credential used during a lock operation."""

    credential_type: clusters.DoorLock.Enums.CredentialTypeEnum
    credential_index: int


@dataclass(frozen=True, slots=True)
class LockOperation:
    """Door Lock operation."""

    node_id: int
    endpoint_id: int

    operation_type: clusters.DoorLock.Enums.LockOperationTypeEnum
    operation_source: clusters.DoorLock.Enums.OperationSourceEnum

    user_index: int | None

    fabric_index: int | None
    source_node: int | None

    credentials: tuple[LockCredential, ...]