# Product Requirements (MVP)

See `PRD.json` for the authoritative, structured requirements. Highlights:

- Goal: A web dashboard that lists Polymarket markets, lets a user select one, and shows a live-updating price widget in a terminal-like layout.
- Architecture: Monorepo with `packages/api` (backend proxy to Polymarket API + WebSockets) and `packages/web` (React + Vite frontend).
- Methodology: TDD-first. Tests added/updated before implementation when practical.

## Phase 1 — Project Setup & Foundation
- Monorepo workspaces, shared TS/ESLint/Prettier.
- API skeleton (Express + /health, build pipeline).
- Web skeleton (Vite React TS, build pipeline).
- Testing: Node test runner for workspace/tooling; Vitest in each package with placeholder tests.

Subsequent phases cover backend API endpoints, WebSocket real-time updates, and UI widgets integrating live data.
