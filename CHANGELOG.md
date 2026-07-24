# Changelog

## v0.0.5

### Added

- Door Lock domain model.
- Translator layer between Matter events and the domain model.
- Immutable `LockOperation` and `LockCredential` models.
- Structured logging for Door Lock operations.
- Hardware validation documentation.

### Changed

- Replaced magic cluster and event identifiers with official Matter SDK constants.
- Manager now delegates all Matter payload parsing to the translator.

### Fixed

- Correctly handle Matter events with `credentials=None`.

## v0.0.6

### Changed

- Validated the architectural boundary between the Matter Server transport layer
  and the integration domain model.

### Documentation

- Added ADR-0004 describing the translator as the boundary between Matter Server
  transport objects and immutable project-owned domain models.
  
## v0.0.7

### Added

- Home Assistant event API.
- Event serializer.
- Public event `matter_lock_events.operation`.

### Documentation

- Added Event API reference.
- Added ADR-0005 documenting the event architecture.

### Changed

- Added event API version field.