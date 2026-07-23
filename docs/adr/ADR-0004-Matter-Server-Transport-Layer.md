# ADR-0004: Terminate the Matter Server transport layer at the translator

- Status: Accepted
- Date: 2026-07-23

## Context

The Home Assistant Matter integration delivers Matter events to custom
integrations using `MatterNodeEvent`.

Runtime validation on Home Assistant confirmed that Door Lock event payloads are
currently exposed through the `data` attribute as decoded dictionaries.

The Matter SDK defines typed event classes internally, but those classes are not
part of the callback contract exposed to custom integrations.

## Decision

The translator forms the architectural boundary between the Matter Server
transport layer and the integration's domain model.

No `MatterNodeEvent` instances or transport-layer payloads shall be used outside
the translator.

The remainder of the integration operates exclusively on immutable domain
objects owned by this project.

## Consequences

Positive

- Stable abstraction over the Matter Server API.
- Future changes to Matter payload representation remain isolated to a single
  module.
- Business logic is independent of transport details.

Negative

- Manual translation remains necessary.