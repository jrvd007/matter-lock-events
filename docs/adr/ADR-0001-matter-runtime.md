# ADR-0001: Accessing the Matter Runtime

**Status:** Accepted

**Date:** 2026-07-14

## Context

Matter Lock Events needs access to Home Assistant's existing Matter runtime in order to subscribe to Matter Door Lock events.

Several approaches were considered.

### Option 1

Import Matter's internal helper function:

```python
get_matter(hass)
```

### Option 2

Retrieve the loaded Matter Config Entry through Home Assistant's Config Entry API and access its runtime data.

### Option 3

Open a second websocket connection directly to the Matter Server.

## Decision

Matter Lock Events retrieves the loaded Matter Config Entry using Home Assistant's Config Entry API.

The running Matter client is obtained from the integration's runtime data:

```python
matter_entry.runtime_data.adapter.matter_client
```

The `MatterLockEventsManager` is responsible for acquiring the Matter client during initialization and subscribing to Matter node events.

No additional abstraction layer is introduced between the manager and Home Assistant's Matter integration.

## Rationale

This approach:

- Reuses Home Assistant's existing Matter client.
- Avoids creating a second websocket connection.
- Uses Home Assistant's supported runtime architecture.
- Keeps the integration simple by avoiding unnecessary wrapper layers.
- Makes the manager the single owner of Matter event subscriptions.

## Consequences

### Advantages

- Single Matter client.
- No duplicated websocket connections.
- Minimal architecture.
- Easy to understand.
- Easy to test.
- Follows Home Assistant's Config Entry runtime model.

### Disadvantages

- Depends on the runtime structure exposed by the Matter integration.
- May require updates if Home Assistant changes how `runtime_data` is organized.

## Alternatives Rejected

### Import `get_matter()`

Rejected because it depends on an internal helper rather than the integration's public runtime state.

### Additional runtime wrapper (`matter_runtime.py`)

Rejected because it introduced an unnecessary abstraction without reducing coupling or simplifying the implementation.

### Second websocket connection

Rejected because Home Assistant already maintains a Matter client and event subscription.

Creating another connection would duplicate functionality, increase complexity, and consume additional resources.