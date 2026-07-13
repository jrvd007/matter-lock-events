# Contributing

## Branch Strategy

- `main` contains stable releases.
- `dev` is the integration branch.
- Feature development happens in `feature/*` branches.

## Development Process

1. Create a feature branch from `dev`.
2. Keep each commit focused on a single feature.
3. Use type hints for all public code.
4. Follow Home Assistant coding conventions.
5. Update documentation when architecture changes.
6. Open a Pull Request into `dev`.

## Commit Guidelines

Examples:

- Create integration framework
- Subscribe to Matter node events
- Add lock operation event decoding
- Add user mapping
- Add sensors

Architecture decisions belong in ARCHITECTURE.md.