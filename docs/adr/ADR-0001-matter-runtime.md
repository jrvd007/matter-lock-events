# ADR-0001: Accessing the Matter Runtime

**Status:** Accepted

**Date:** 2026-07-14

## Context

Matter Lock Events requires access to Home Assistant's existing Matter runtime in order to receive Door Lock events.

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

Matter Lock Events retrieves the loaded Matter Config Entry through Home Assistant's public Config Entry API.

The running `MatterAdapter` is obtained from:

```python
entry.runtime_data.adapter
```

All interaction with Home Assistant's Matter integration is encapsulated in `matter_runtime.py`.

No other module should directly depend on the Matter integration.

## Rationale

This approach:

- Reuses Home Assistant's existing Matter client.
- Avoids creating a second websocket connection.
- Minimizes coupling to Matter's internal helper modules.
- Follows Home Assistant's runtime architecture.
- Keeps Matter-specific logic isolated.

## Consequences

### Advantages

- Single Matter client.
- Easy to maintain.
- Small public interface.
- Easy to unit test.
- Future Matter changes are isolated to one module.

### Disadvantages

- Depends on the runtime structure of the Matter integration.
- May require updates if Home Assistant changes how Matter runtime data is exposed.

## Alternatives Rejected

### Import `get_matter()`

Although simple, it introduces a dependency on an internal helper module.

### Second websocket connection

Rejected because Home Assistant already maintains a Matter client and event listener.

Duplicating this functionality would increase complexity and resource usage.