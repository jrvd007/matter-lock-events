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