"""Helpers to resolve Home Assistant entities from Matter nodes."""

from __future__ import annotations

from chip.clusters import Objects as clusters
from matter_server.client import MatterClient

from .const import MATTER_LOCK_ENTITY_KEY


def resolve_entity_id(
    hass,
    server_info,
    matter_client: MatterClient,
    node_id: int,
    endpoint_id: int,
) -> str | None:
    """Resolve the Home Assistant entity_id for a Matter Door Lock."""

    from homeassistant.components.matter.helpers import get_device_id
    from homeassistant.helpers import entity_registry as er

    node = matter_client.get_node(node_id)
    if node is None:
        return None

    endpoint = node.endpoints.get(endpoint_id)
    if endpoint is None:
        return None

    matter_device_id = get_device_id(server_info, endpoint)

    unique_id = (
        f"{matter_device_id}-"
        f"{endpoint.endpoint_id}-"
        f"{MATTER_LOCK_ENTITY_KEY}-"
        f"{clusters.DoorLock.id}-"
        f"{clusters.DoorLock.Attributes.LockState.attribute_id}"
    )

    entity_registry = er.async_get(hass)

    return entity_registry.async_get_entity_id(
        "lock",
        "matter",
        unique_id,
    )
