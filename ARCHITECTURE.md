# Matter Lock Events Architecture

## Overview

Matter Lock Events is a Home Assistant custom integration that exposes Matter Door Lock events as native Home Assistant events.

The project is designed to reuse Home Assistant's existing Matter infrastructure rather than creating a second Matter client.

```
Matter Lock
      │
      ▼
Matter Server Add-on
      │
      ▼
Home Assistant Matter Integration
      │
      ▼
Matter Lock Events
      │
      ▼
Home Assistant Event Bus
      │
      ├── Automations
      ├── Sensors
      ├── History
      └── Future integrations
```

## Design Goals

- Reuse Home Assistant's existing Matter client.
- Never open a second websocket connection to the Matter Server.
- Keep event handling independent from entity creation.
- Be compatible with HACS.
- Follow Home Assistant coding conventions.
- Keep features modular and testable.

## Design Principles

The project follows these principles:

1. Reuse Home Assistant's Matter integration.
2. Never create a second Matter client.
3. Prefer ConfigEntry.runtime_data over hass.data.
4. Separate lifecycle management from event processing.
5. Keep all runtime state typed.
6. Keep commits small and independently testable.

## Planned Architecture

```
Manager
    │
    ├── Acquire MatterAdapter
    ├── Subscribe to Matter events
    ├── Dispatch callbacks
    └── Shutdown cleanly

Callbacks
    │
    ├── Decode Matter events
    ├── Convert to internal models
    └── Fire Home Assistant events

Models
    │
    └── Typed dataclasses shared by the integration
```

## Event Flow

```
Matter Lock
    │
    ▼
Matter Server
    │
    ▼
MatterAdapter
    │
    ▼
Matter Lock Events
    │
    ▼
matter_lock_operation
    │
    ├── Automations
    ├── Sensors
    └── History
```

## Roadmap

### v0.1

- Subscribe to Matter node events
- Expose LockOperation events

### v0.2

- Map Matter nodes to Home Assistant entities
- User index support

### v0.3

- User name mapping

### v0.4

- Sensors

### v1.0

- Stable HACS release