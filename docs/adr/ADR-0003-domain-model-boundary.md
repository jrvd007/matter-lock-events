# ADR-0003: Domain Model Boundary

- Status: Accepted
- Date: 2026-07-20

## Context

The Home Assistant Matter integration exposes Matter events through
`MatterNodeEvent` objects.

These objects are owned by the upstream Matter integration and may evolve as
Matter or Home Assistant changes.

Allowing these objects to propagate throughout the codebase would tightly
couple this integration to implementation details outside its control.

## Decision

`MatterNodeEvent` objects shall only exist within the runtime layer of this
integration.

Stable Matter specification enums may be reused directly when they represent standardized protocol concepts rather than runtime objects.

Specifically:

- `MatterLockEventsManager` is responsible for receiving Matter events.
- The manager immediately translates supported events into project-owned
  domain models.
- All downstream code works exclusively with those domain models.
- Raw Matter dictionaries and `MatterNodeEvent` instances must never leave
  the runtime boundary.

The integration preserves Matter semantics.

Matter protocol values are translated into immutable domain models without altering
their meaning.

Manufacturer-specific values exposed by the Matter SDK are preserved exactly as
received.

The integration does not reinterpret Matter operation sources and does not merge
Matter identities with Home Assistant identities.

Matter-specific parsing is isolated within the translator layer. The remainder of
the integration operates exclusively on project-owned domain models.

## Consequences

### Advantages

- Strong separation of concerns.
- Easier unit testing.
- No Matter runtime objects leave the runtime layer.
- Future Matter protocol changes are isolated.
- Cleaner public API inside the project.

### Disadvantages

- Introduces a translation step.

## Rationale

This integration is intended to become a generic Matter Door Lock event
integration rather than an implementation tied to one version of Home
Assistant's Matter internals.

Maintaining a strict domain boundary ensures the integration remains stable,
testable and maintainable over time.