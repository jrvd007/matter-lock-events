# Matter Lock Events

## Overview

Matter Lock Events exposes Matter Door Lock operations through the Home Assistant
event bus.

The integration emits a single event whose payload preserves Matter semantics
while providing Home Assistant-friendly values.

---

## Event Type

matter_lock_events.operation

---

## Event Data

| Field | Type | Description |
|--------|------|-------------|
| api_version | int | Event API version |
| node_id | int | Matter node identifier |
| endpoint_id | int | Matter endpoint identifier |
| entity_id | string | null | Home Assistant Entity ID |
| operation | string | Matter operation name |
| operation_id | int | Raw Matter operation enum |
| source | string | Matter operation source |
| source_id | int | Raw Matter source enum |
| user_index | int \| null | Matter user index |
| user_name | string | null | Matter user name |
| fabric_index | int \| null | Matter fabric identifier |
| source_node | int \| null | Originating Matter node |
| credentials | list | Credentials used during the operation |

---

## Credential Object

| Field | Type | Description |
|--------|------|-------------|
| credential_type | string | Credential type |
| credential_type_id | int | Raw Matter credential enum |
| credential_index | int | Credential slot |

---

## API Stability

The event type and documented field names constitute the public API of this
integration.

Future releases may add new optional fields but will not rename or remove
existing fields without a major version increment of the event API.

---

## Example

```yaml
event_type: matter_lock_events.operation

event_data:
  api_version: 1

  node_id: 23
  endpoint_id: 1

  entity_id: lock.sense_pro

  operation: unlock
  operation_id: 1

  source: remote
  source_id: 7

  user_index: null
  user_name: John

  fabric_index: 2

  source_node: 112233

  credentials: []