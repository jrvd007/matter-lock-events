"""Constants for Matter Lock Events."""

DOMAIN = "matter_lock_events"

NAME = "Matter Lock Events"

EVENT_OPERATION = "matter_lock_events.operation"

# Matter entity description key used by the Home Assistant Matter integration.
MATTER_LOCK_ENTITY_KEY = "MatterLock"

__version__ = "0.1.0"

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