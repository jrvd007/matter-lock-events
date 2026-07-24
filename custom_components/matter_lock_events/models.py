"""Runtime models."""

from __future__ import annotations

from dataclasses import dataclass

from homeassistant.config_entries import ConfigEntry

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .manager import MatterLockEventsManager

@dataclass(slots=True)
class MatterLockEventsData:
    """Runtime data for Matter Lock Events."""

    manager: MatterLockEventsManager


type MatterLockEventsConfigEntry = ConfigEntry[MatterLockEventsData]