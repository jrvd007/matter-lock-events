# Matter Lock Events - Event API

## Overview

This integration exposes Matter Door Lock operations through the Home Assistant
event bus.

The integration emits a single generic event whose payload preserves the Matter
semantics while providing Home Assistant-friendly string values.

## Event

Event type:

matter_lock_events.operation

## Event Data

| Field | Type | Description |
|-------|------|-------------|
| node_id | int | Matter node identifier |
| endpoint_id | int | Matter endpoint identifier |
| operation | string | Door lock operation name |
| operation_id | int | Raw Matter LockOperationType enum value |
| source | string | Door lock operation source name |
| source_id | int | Raw Matter OperationSource enum value |
| user_index | int \| null | Matter user index |
| fabric_index | int \| null | Matter fabric index |
| source_node | int \| null | Originating Matter node |
| credentials | list | Credentials used during the operation |

## Credentials

Each credential is represented as:

| Field | Type | Description |
|-------|------|-------------|
| credential_type | string | Credential type name |
| credential_type_id | int | Raw Matter CredentialType enum value |
| credential_index | int | Credential index |

## Example

```yaml
event_type: matter_lock_events.operation

event_data:
  node_id: 23
  endpoint_id: 1

  operation: unlock
  operation_id: 1

  source: remote
  source_id: 7

  user_index: null

  fabric_index: 2

  source_node: 112233

  credentials: []```
  
## API Stability

The event type and documented field names are considered part of the public API
of this integration.

Future releases may add new optional fields but will not rename or remove
existing fields without a major version change. 