# ADR-0005: Expose Matter Door Lock events through dedicated Home Assistant events

* **Status:** Accepted
* **Date:** 2026-07-24
* **Updated:** 2026-08-03

## Context

The integration exposes Matter Door Lock events to Home Assistant so they can be used in automations.

Initially, the integration considered publishing all Door Lock events through a single Home Assistant event with an event-type field in the payload.

As support expanded beyond successful lock operations to include operation errors and lock alarms, these events were found to represent distinct concepts with different automation use cases.

## Decision

The integration publishes one Home Assistant event for each Matter Door Lock event category:

* `matter_lock_events.operation`
* `matter_lock_events.operation_error`
* `matter_lock_events.alarm`

Each event publishes only the fields relevant to that event type while preserving both the human-readable Matter enum names and their corresponding numeric identifiers.

Common fields, such as `api_version`, `node_id`, and `entity_id`, remain consistent across all event types.

## Consequences

### Positive

* Event names clearly communicate the type of activity that occurred.
* Automations can subscribe directly to the event of interest without additional filtering.
* Payloads remain focused and contain only relevant fields.
* The design closely follows the Matter Door Lock event model.
* Additional Matter Door Lock events can be added in the future without changing existing event schemas.

### Negative

* Consumers interested in every Door Lock event must subscribe to multiple Home Assistant events instead of a single event.
* Some common payload fields are repeated across event types.
