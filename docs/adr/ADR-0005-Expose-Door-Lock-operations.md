# ADR-0005: Expose Door Lock operations through a single Home Assistant event

- Status: Accepted
- Date: 2026-07-24

## Context

The integration needs to expose Matter Door Lock operations to Home Assistant
automations while maintaining compatibility with future Matter revisions.

## Decision

The integration shall publish a single Home Assistant event named

matter_lock_events.operation

All operation-specific information is carried within the event payload.

The payload preserves Matter semantics while exposing human-readable values and
their corresponding numeric identifiers.

## Consequences

Positive

- Stable event API.
- Extensible payload.
- One automation trigger for all Door Lock operations.
- Payload remains compatible with future Matter extensions.

Negative

- Consumers filter on event data rather than event type.