# Engineering Principles

## 1. Upstream First

Reuse Home Assistant APIs when available.
Otherwise reuse Matter APIs.
Implement locally only when necessary.

## 2. Strong Domain Boundary

Matter runtime objects never leave the runtime layer.
The rest of the integration works with project-owned domain models.

## 3. Small Focused Commits

Every commit answers one engineering question.

## 4. Testability

Business logic should be testable without Home Assistant.

## 5. Explicit Architecture

Significant architectural decisions are documented in ADRs.

## 6. Logging is a Feature

Logs should help users and developers understand what the integration is doing.