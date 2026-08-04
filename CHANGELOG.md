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

## v0.0.8

### Added
- Regression tests for translator, serializer, and manager behavior using real captured Matter payloads.
- Local development workflow documentation for running tests outside Home Assistant.

### Changed
- Centralized Matter Server transport keys in const.py.
- Hardened the translator boundary between Matter Server transport data and the immutable domain model.
- Added manager orchestration coverage for publishing Home Assistant events and ignoring unrelated Matter events.

### Fixed
- Prevented import-time Home Assistant dependencies from blocking local unit tests.
- Improved testability by making the integration package import-light.

## v1.0.0
### Added
- Lock operation events (matter_lock_events.operation).
- Lock operation error events (matter_lock_events.operation_error).
- Door lock alarm events (matter_lock_events.alarm).
- Automatic resolution of Matter user indexes to lock user names.
- Automatic resolution of Home Assistant lock entity IDs.
- Support for Matter Door Lock LockOperation, LockOperationError, and DoorLockAlarm events.
- Alarm serialization with both human-readable names and raw Matter enum values.
- Comprehensive unit tests covering translators, serializers, manager orchestration, and user resolution.
- HACS compatibility.

### Changed
- Refactored manager orchestration to support multiple Matter Door Lock event types.
- Centralized event field names, payload keys, and API constants in const.py.
- Improved serializer consistency across all published events.
- Standardized payload structure with api_version included in every event.
- Simplified lock user resolution by querying the Matter lock directly instead of maintaining a local cache.

### Fixed
- Correctly resolve Matter lock user names for keypad operations.
- Improved compatibility with local pytest execution outside Home Assistant.
- Various internal refactoring and cleanup to improve maintainability and testability.