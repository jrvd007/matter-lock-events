"""
Captured Matter Door Lock event payloads.

Device:
    Schlage Sense Pro

Purpose:
    Regression fixtures for translator and serializer tests.

These payloads were captured from a real device during development.
They should never be modified to "make tests pass."
"""

REMOTE_UNLOCK = {
    "lockOperationType": 1,
    "operationSource": 7,
    "userIndex": None,
    "fabricIndex": 2,
    "sourceNode": 112233,
    "credentials": None,
}