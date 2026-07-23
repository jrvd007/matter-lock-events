# Schlage Sense Pro

## Hardware

- Lock: Schlage Sense Pro
- Protocol: Matter

## Validation

### Unlock using keypad

Result

- Operation: kUnlock
- Source: kKeypad
- User Index populated
- Credential information populated

### Lock using keypad

Result

- Operation: kLock
- Source: kButton

### Unlock using Home Assistant

Result

- Operation: kUnlock
- Source: kRemote
- User Index: None

The Home Assistant Activity Log correctly attributes the action to the Home Assistant
user that initiated the unlock.

This indicates that Matter identities and Home Assistant user identities are
independent systems and should remain separate within the integration.