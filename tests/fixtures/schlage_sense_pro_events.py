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

KEYPAD_LOCK = {
    "lockOperationType": 0,
    "operationSource": 5,
    "userIndex": None,
    "fabricIndex": None,
    "sourceNode": None,
    "credentials": None,
}

KEYPAD_UNLOCK = {
    "lockOperationType": 1,
    "operationSource": 3,
    "userIndex": 1,
    "fabricIndex": None,
    "sourceNode": None,
    "credentials": [
        {
            "credentialType": 1,
            "credentialIndex": 1,
        }
    ],
}

MANUAL_THUMBTURN_LOCK = {
    "lockOperationType": 0,
    "operationSource": 1,
    "userIndex": None,
    "fabricIndex": None,
    "sourceNode": None,
    "credentials": None,
}

WRONG_PIN = {
    "lockOperationType": 1,
    "operationSource": 3,
    "operationError": 1,
    "userIndex": None,
    "fabricIndex": None,
    "sourceNode": None,
    "credentials": None,
}
