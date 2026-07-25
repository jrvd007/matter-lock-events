"""Constants for Matter Lock Events."""

DOMAIN = "matter_lock_events"

NAME = "Matter Lock Events"

EVENT_OPERATION = "matter_lock_events.operation"

__version__ = "0.0.8"

# -----------------------------------------------------------------------------
# MatterNodeEvent.data transport keys
# -----------------------------------------------------------------------------

DATA_LOCK_OPERATION_TYPE = "lockOperationType"
DATA_OPERATION_SOURCE = "operationSource"
DATA_USER_INDEX = "userIndex"
DATA_FABRIC_INDEX = "fabricIndex"
DATA_SOURCE_NODE = "sourceNode"
DATA_CREDENTIALS = "credentials"

DATA_CREDENTIAL_TYPE = "credentialType"
DATA_CREDENTIAL_INDEX = "credentialIndex"