# Matter Lock Events

A Home Assistant custom integration that exposes Matter Door Lock operation events for automations.

The project is being developed incrementally, with each commit representing a small, independently testable milestone.

## Home Assistant Events

The integration publishes Matter Door Lock operations through the Home Assistant
event bus.

Event type:

matter_lock_events.operation

See `docs/events.md` for the complete event schema.

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

## Development

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate
Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

### Install Development Dependencies
```bash
pip install -r requirements-dev.txt
```

### Run Tests
```bash
pytest
```

### Run a single test file

```bash
pytest tests/test_translator.py
pytest tests/test_event_adapter.py
pytest tests/test_manager.py
```