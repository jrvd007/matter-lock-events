# Matter Lock Events Architecture

## Overview

Matter Lock Events is a Home Assistant custom integration that exposes Matter Door Lock events as native Home Assistant events while reusing Home Assistant's existing Matter infrastructure.

The integration does **not** create its own Matter client or websocket connection. Instead, it integrates with Home Assistant's Matter integration and subscribes to the Matter event stream already maintained by Home Assistant.

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
      ├── Scripts
      ├── Future sensors
      └── Future integrations
```

---

# Design Goals

The project is designed around the following goals:

* Reuse Home Assistant's existing Matter client.
* Never open a second websocket connection to the Matter Server.
* Publish a stable event API for Home Assistant automations.
* Preserve Matter semantics while exposing Home Assistant-friendly payloads.
* Keep event handling independent from entity creation.
* Follow Home Assistant coding conventions.
* Remain fully compatible with HACS.
* Keep the codebase modular, maintainable, and testable.

---

# Design Principles

The architecture follows several guiding principles.

1. Reuse Home Assistant's Matter integration.
2. Never create a second Matter client.
3. Keep transport objects separate from immutable domain models.
4. Separate translation, serialization, and orchestration responsibilities.
5. Publish stable event contracts.
6. Keep runtime state typed.
7. Keep features independently testable.

These principles are further documented in the project's Architecture Decision Records (ADRs).

---

# High-Level Architecture

The integration is intentionally divided into small components, each with a single responsibility.

```
Matter Events
      │
      ▼
+---------------------------+
| MatterLockEventsManager   |
+---------------------------+
            │
            ├──────────────┐
            ▼              ▼
     Entity Resolver   Lock User Resolver
            │
            ▼
       Translator
            │
            ▼
     Domain Models
            │
            ▼
      Event Adapter
            │
            ▼
Home Assistant Event Bus
```

---

# Component Responsibilities

## MatterLockEventsManager

Responsible for:

* Initializing the integration.
* Subscribing to Matter node events.
* Dispatching incoming Matter Door Lock events.
* Resolving Home Assistant entity IDs.
* Resolving Matter lock user names.
* Publishing Home Assistant events.

The manager coordinates the integration but intentionally contains very little business logic.

---

## Translator

The translator converts Matter transport objects into immutable project-owned domain models.

Responsibilities include:

* Decoding Matter event payloads.
* Converting Matter enums into typed domain objects.
* Shielding the remainder of the project from Matter transport details.

No Home Assistant-specific logic exists in this layer.

---

## Domain Models

The integration owns immutable dataclasses representing Door Lock concepts, including:

* LockOperation
* LockOperationError
* DoorLockAlarm
* LockCredential

These models provide a stable boundary between Matter transport objects and the remainder of the integration.

---

## Entity Resolver

Maps Matter node and endpoint identifiers to Home Assistant entity IDs.

This allows published events to reference the corresponding Home Assistant lock entity.

---

## Lock User Resolver

Resolves Matter lock user indexes into human-readable user names by querying the lock through Home Assistant's existing Matter helper functions.

The resolver performs lookups on demand rather than maintaining a local cache, avoiding cache invalidation complexity while keeping the implementation simple.

---

## Event Adapter

Serializes immutable domain models into Home Assistant event payloads.

Responsibilities include:

* Converting enums into human-readable values.
* Preserving Matter numeric identifiers.
* Maintaining a stable public event schema.
* Including the API version in every published event.

---

# Event Flow

```
Matter Lock
      │
      ▼
Matter Server
      │
      ▼
Home Assistant Matter Integration
      │
      ▼
MatterLockEventsManager
      │
      ▼
Translator
      │
      ▼
Domain Models
      │
      ▼
Event Adapter
      │
      ▼
Home Assistant Event Bus
      │
      ├── matter_lock_events.operation
      ├── matter_lock_events.operation_error
      └── matter_lock_events.alarm
```

---

# Published Events

The integration currently publishes three Home Assistant events.

| Event                                | Description                           |
| ------------------------------------ | ------------------------------------- |
| `matter_lock_events.operation`       | Successful lock and unlock operations |
| `matter_lock_events.operation_error` | Failed lock or unlock attempts        |
| `matter_lock_events.alarm`           | Door Lock alarms reported by Matter   |

Each event exposes a stable payload documented in the public Event API.

---

# Testing Philosophy

The project emphasizes small, independently testable components.

Unit tests validate:

* Matter payload translation.
* Event serialization.
* Manager orchestration.
* Entity resolution.
* User name resolution.

Captured Matter payloads from real hardware are used whenever practical to ensure compatibility with physical devices.

---

# Architectural References

Long-term architectural decisions are documented in the ADRs located in the `docs/adr/` directory.

These records explain the rationale behind significant design choices and should be consulted before making architectural changes.
