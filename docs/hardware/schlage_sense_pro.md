# Schlage Sense Pro Validation

## Hardware

- Lock: Schlage Sense Pro
- Firmware: *(optional)*
- Protocol: Matter
- Integration: Home Assistant Matter

This document records the observed Matter behavior of the Schlage Sense Pro.
It serves as a reference when validating support for other Matter-compatible
door locks.

---

# LockOperation Events

## Unlock using keypad

Observed Matter event

- Operation: `kUnlock`
- Source: `kKeypad`
- User Index populated
- Credential information populated

Published Home Assistant event

- `matter_lock_events.operation`

---

## Lock using keypad

Observed Matter event

- Operation: `kLock`
- Source: `kButton`
- User Index: `None`
- Credential information: `None`

Published Home Assistant event

- `matter_lock_events.operation`

---

## Unlock using Home Assistant

Observed Matter event

- Operation: `kUnlock`
- Source: `kRemote`
- User Index: `None`

Published Home Assistant event

- `matter_lock_events.operation`

Notes

The Home Assistant Activity Log correctly attributes the action to the Home Assistant
user that initiated the unlock.

Matter identities and Home Assistant user identities are independent systems and
should remain separate within the integration.

---

## Thumbturn

Observed Matter event

- Operation: `kUnlock`
- Source: `kManual`

Published Home Assistant event

- `matter_lock_events.operation`

---

## Auto Lock

Observed Matter event

- Operation: `kLock`
- Source: `kAuto`

Published Home Assistant event

- `matter_lock_events.operation`

---

# LockOperationError Events

## Invalid keypad code

Observed Matter event

- Operation: `kUnlock`
- Source: `kKeypad`
- Error: `kInvalidCredential`
- User Index: `None`

Published Home Assistant event

- `matter_lock_events.operation_error`

---

# DoorLockAlarm Events

## Bolt jam / door ajar

Observed Matter event

- Alarm: `kLockJammed`

Published Home Assistant event

- `matter_lock_events.alarm`

---

## Four consecutive invalid PIN entries

Observed Matter event

- Alarm: `kWrongCodeEntryLimit`

Published Home Assistant event

- `matter_lock_events.alarm`

---

# Observations

The Schlage Sense Pro publishes the following Matter Door Lock events:

- LockOperation
- LockOperationError
- DoorLockAlarm

The following Matter Door Lock events are defined by the specification but have
not yet been observed on this hardware:

- DoorStateChange
- LockUserChange

Support for these events may vary between manufacturers.