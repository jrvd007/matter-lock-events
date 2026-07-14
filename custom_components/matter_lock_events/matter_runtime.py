"""Helpers for accessing Home Assistant's Matter runtime."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from homeassistant.core import HomeAssistant

from .exceptions import (
    InvalidMatterConfigurationError,
    MatterNotAvailableError,
)

if TYPE_CHECKING:
    from homeassistant.components.matter.helpers import MatterConfigEntry
    from homeassistant.components.matter.adapter import MatterAdapter


from homeassistant.components.matter.const import DOMAIN as MATTER_DOMAIN


def async_get_matter_entry(hass: HomeAssistant) -> MatterConfigEntry:
    """Return the loaded Matter config entry."""

    entries = hass.config_entries.async_loaded_entries(MATTER_DOMAIN)

    if not entries:
        raise MatterNotAvailableError(
            "The Matter integration is not loaded."
        )

    if len(entries) != 1:
        raise InvalidMatterConfigurationError(
            f"Expected exactly one Matter config entry, found {len(entries)}."
        )

    return cast("MatterConfigEntry", entries[0])


def async_get_adapter(hass: HomeAssistant) -> MatterAdapter:
    """Return the running Matter adapter."""

    entry = async_get_matter_entry(hass)

    return entry.runtime_data.adapter