# ADR-0002: Use Home Assistant Config Entries

**Status:** Accepted

**Date:** 2026-07-15

## Context

Matter Lock Events was initially designed as a YAML-based integration.

The original intent was to minimize the amount of Home Assistant infrastructure required while proving that Matter Door Lock events could be accessed and exposed through a custom integration.

During development, several observations were made:

- Modern Home Assistant integrations are based on Config Entries.
- The Matter integration itself exposes its runtime state through `ConfigEntry.runtime_data`.
- Integration lifecycle management (setup, unload and reload) is built around Config Entries.
- A Config Entry based integration provides the best installation experience for HACS users.

Unlike many integrations, Matter Lock Events does not require any user-provided configuration. It simply subscribes to events exposed by the existing Matter integration.

## Decision

Matter Lock Events uses Home Assistant Config Entries as its integration lifecycle model.

The integration does not use YAML configuration.

No runtime configuration is required from the user.

The integration initializes itself from the existing Matter integration and stores its runtime state using `ConfigEntry.runtime_data`.

## Consequences

### Advantages

- Aligns with Home Assistant Core architecture.
- Supports Home Assistant's standard setup and unload lifecycle.
- Integrates naturally with HACS.
- Eliminates YAML configuration.
- Stores runtime state using `ConfigEntry.runtime_data`.
- Remains consistent with the Matter integration.

### Disadvantages

- Depends on Home Assistant's Config Entry lifecycle.
- Requires the Matter integration to be installed and initialized.

## Alternatives Considered

### YAML configuration

Rejected.

The integration has no configuration that would benefit from YAML and Home Assistant has largely standardized on Config Entries.

### Hybrid YAML + Config Entries

Rejected.

Supporting two configuration mechanisms would increase maintenance complexity without providing any practical benefit.

## Rationale

Matter Lock Events is designed to behave like a native Home Assistant integration while remaining as simple as possible.

Using Config Entries provides the appropriate lifecycle management without introducing unnecessary configuration for the user.

The integration's purpose is to extend the existing Matter integration rather than configure independent hardware, making a configuration-free Config Entry architecture the simplest and most maintainable solution.