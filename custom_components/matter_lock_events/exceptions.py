"""Custom exceptions for Matter Lock Events."""


class MatterLockEventsError(Exception):
    """Base exception for Matter Lock Events."""


class MatterNotAvailableError(MatterLockEventsError):
    """Raised when the Matter integration is unavailable."""