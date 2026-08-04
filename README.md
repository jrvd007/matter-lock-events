# Matter Lock Events

A Home Assistant custom integration that exposes Matter Door Lock events as Home Assistant events, making it easy to build automations based on lock activity.

Matter Lock Events works alongside the official Matter integration and provides additional event information that is not currently exposed by Home Assistant, including lock user names, operation sources, lock errors, and lock alarms.

## Features
* ✅ Lock and unlock events  
* ✅ Lock operation error events  
* ✅ Door lock alarm events  
* ✅ Resolves the Home Assistant lock entity automatically  
* ✅ Resolves Matter user indexes to user names  
* ✅ Preserves Matter enum IDs for advanced automations  
* ✅ Lightweight implementation with no polling  
* ✅ Fully tested with pytest  
* ✅ HACS compatible  

## Supported Matter Events

The integration currently publishes the following Home Assistant events:

### Supported Matter Events

The integration currently publishes the following Home Assistant events:

| Event | Description |
| :--- | :--- |
| `matter_lock_operation` | Successful lock and unlock operations |
| `matter_lock_operation_error` | Failed lock operations (wrong PIN, invalid credential, etc.) |
| `matter_lock_alarm` | Door lock alarms (lock jammed, wrong code entry limit, etc.) |


## Event Examples

**matter_lock_events.operation**

api_version: 1
entity_id: lock.front_door
node_id: 23

operation: unlock
source: keypad

user:
  user_index: 1
  user_name: John


**matter_lock_events.operation_error**

api_version: 1
entity_id: lock.front_door
node_id: 23

operation: unlock
source: keypad

error: invalid_credential
error_id: 1


**matter_lock_events.alarm**

api_version: 1
entity_id: lock.front_door
node_id: 23

alarm: lock_jammed
alarm_id: 4

## Installation
### HACS (Recommended)
1. Open HACS.
2. Go to Integrations.
3. Open the ⋮ menu.
4. Select Custom repositories.
5. Add:
    https://github.com/jrvd007/matter-lock-events

  **Category:**
  Integration

6. Install Matter Lock Events.
7. Restart Home Assistant.

### Manual Installation
1. Download this repository.
2. Copy the matter_lock_events folder into:
  config/custom_components/
3. Restart Home Assistant.
4. Add the integration from Settings → Devices & Services.

## Example Automation

**Notify when the front door fails to lock because it is jammed:**

alias: Notify Lock Jam

trigger:
  - platform: event
    event_type: matter_lock_events.alarm

condition:
  - condition: template
    value_template: >
      {{ trigger.event.data.alarm == "lock_jammed" }}

action:
  - service: notify.mobile_app_phone
    data:
      message: The front door failed to lock because it is jammed.

## Requirements
- Home Assistant
- Official Matter integration
- A Matter-compatible door lock

## Development

**Create a virtual environment:**

```bash
python -m venv .venv
```

**Activate it:**

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Install development dependencies:**

```bash
pip install -r requirements-dev.txt
```

**Run the full test suite:**

```bash
pytest
```

**Run an individual test file:**

```bash
pytest tests/test_translator.py
pytest tests/test_event_adapter.py
pytest tests/test_manager.py
```

## License

This project is released under the MIT License.
