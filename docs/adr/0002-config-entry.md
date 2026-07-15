# ADR-0002: Use Home Assistant Config Entries Instead of YAML Configuration

- **Status:** Accepted
- **Date:** 2026-07-15

## Context

Matter Lock Events was initially designed as a YAML-based integration.

The original intent was to minimize the amount of Home Assistant infrastructure required while proving that Matter lock events could be accessed and exposed through a custom integration.

During development, several observations were made:

- Home Assistant discovered the integration but did not initialize it from `configuration.yaml`.
- Modern Home Assistant integrations are primarily based on Config Entries.
- The Matter integration itself uses Config Entries and stores its runtime state using `ConfigEntry.runtime_data`.
- Supporting reload, unload and future options is significantly simpler with Config Entries.
- A Config Entry based integration provides a better installation experience for HACS users.

## Decision

Matter Lock Events will use Home Assistant Config Entries as its primary integration model.

The integration will no longer rely on YAML configuration.

A minimal Config Flow will be implemented that:

- Allows exactly one instance of the integration.
- Requires no user configuration.
- Immediately creates the Config Entry.

Runtime state will be stored using `ConfigEntry.runtime_data`.

## Consequences

### Positive

- Aligns with Home Assistant Core architecture.
- Native "Add Integration" user experience.
- Supports Reload and Delete from the UI.
- Enables future Options Flow without architectural changes.
- Eliminates the need for `hass.data` as the primary runtime store.
- Keeps the integration consistent with the Matter integration itself.

### Negative

- Requires implementing a Config Flow earlier than originally planned.
- Slightly increases the amount of Home Assistant boilerplate.

## Alternatives Considered

### Continue using YAML

Rejected.

Although simpler initially, YAML configuration does not align with the direction of Home Assistant Core and would require additional migration work later.

### Hybrid YAML + Config Entry

Rejected.

Supporting two configuration mechanisms would unnecessarily increase maintenance complexity while providing little benefit.

## Rationale

The long-term goal of Matter Lock Events is to become a polished HACS integration that behaves like a native Home Assistant integration.

Using Config Entries from the beginning provides a cleaner architecture, improves the installation experience, and follows the same lifecycle model as the Matter integration.

This decision intentionally prioritizes long-term maintainability over minimizing short-term implementation effort.