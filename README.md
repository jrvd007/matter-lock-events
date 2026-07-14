# Matter Lock Events

A Home Assistant custom integration that exposes Matter Door Lock operation events for automations.

The project is being developed incrementally, with each commit representing a small, independently testable milestone.

## Goals

- Expose Matter Door Lock Operation events
- Include user index
- Include operation source
- Map user IDs to names
- Create sensors for last user and operation
- Be fully compatible with HACS

## Project Status

Matter Lock Events is currently under active development.

### Roadmap

- ✅ Project framework
- ✅ Runtime abstraction
- ⏳ Matter event subscription
- ⏳ LockOperation event decoding
- ⏳ Home Assistant event generation
- ⏳ User index extraction
- ⏳ User name mapping
- ⏳ HACS release