"""Resolve Matter lock users."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from homeassistant.components.matter.lock_helpers import get_lock_users

if TYPE_CHECKING:
    from matter_server.client.models.node import MatterNode
    from matter_server.common.models import ServerInfoMessage
    from homeassistant.core import HomeAssistant
    


import logging
_LOGGER = logging.getLogger(__name__)


def _find_node(
    matter_client,
    node_id: int,
) -> MatterNode | None:
    """Return the Matter node matching the node id."""

    return next(
        (node for node in matter_client.get_nodes() if node.node_id == node_id),
        None,
    )


async def resolve_lock_user(
    hass: HomeAssistant,
    server_info: ServerInfoMessage,
    matter_client,
    node_id: int,
    endpoint_id: int,
    user_index: int | None,
) -> dict[str, Any] | None:
    """Resolve the Matter lock user from a Matter event."""

    if user_index is None:
        return None

    node = _find_node(matter_client, node_id)

    if node is None:
        _LOGGER.debug("Matter node %s not found", node_id)
        return None

    try:
        users = await get_lock_users(
            matter_client,
            node,
        )
    except Exception:
        _LOGGER.exception(
            "Unable to retrieve users for Matter node %s",
            node_id,
        )
        return None

    for user in users["users"]:
        if user["user_index"] == user_index:
            return user

    return None