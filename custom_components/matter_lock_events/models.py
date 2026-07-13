"""Shared models for Matter Lock Events."""

from dataclasses import dataclass


@dataclass(slots=True)
class IntegrationContext:
    """Shared runtime context."""