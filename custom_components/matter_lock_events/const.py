"""Constants for Matter Lock Events."""

DOMAIN = "matter_lock_events"

API_VERSION = 1

NAME = "Matter Lock Events"

#
# Event names
#
EVENT_OPERATION = "matter_lock_events.operation"
EVENT_OPERATION_ERROR = "matter_lock_events.operation_error"
EVENT_ALARM = "matter_lock_events.alarm"

# Matter entity description key used by the Home Assistant Matter integration.
MATTER_LOCK_ENTITY_KEY = "MatterLock"

__version__ = "0.2.0"

# -----------------------------------------------------------------------------
# MatterNodeEvent.data transport keys
# -----------------------------------------------------------------------------

DATA_LOCK_OPERATION_TYPE = "lockOperationType"
DATA_OPERATION_SOURCE = "operationSource"
DATA_OPERATION_ERROR = "operationError"
DATA_USER_INDEX = "userIndex"
DATA_FABRIC_INDEX = "fabricIndex"
DATA_SOURCE_NODE = "sourceNode"
DATA_CREDENTIALS = "credentials"

DATA_CREDENTIAL_TYPE = "credentialType"
DATA_CREDENTIAL_INDEX = "credentialIndex"

#
# Payload fields
#

FIELD_API_VERSION = "api_version"



FIELD_NODE_ID = "node_id"
FIELD_ENDPOINT_ID = "endpoint_id"
FIELD_ENTITY_ID = "entity_id"

FIELD_OPERATION = "operation"
FIELD_OPERATION_ID = "operation_id"

FIELD_SOURCE = "source"
FIELD_SOURCE_ID = "source_id"

FIELD_USER_NAME = "user_name"
FIELD_USER_INDEX = "user_index"

FIELD_FABRIC_INDEX = "fabric_index"
FIELD_SOURCE_NODE = "source_node"

FIELD_CREDENTIALS = "credentials"
FIELD_CREDENTIAL_TYPE = "credential_type"
FIELD_CREDENTIAL_TYPE_ID = "credential_type_id"
FIELD_CREDENTIAL_INDEX = "credential_index"

FIELD_ERROR = "error"
FIELD_ERROR_ID = "error_id"

FIELD_ALARM = "alarm"
FIELD_ALARM_ID = "alarm_id"