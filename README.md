# Portnoy Terminal (Polymarket Terminal MVP)

A web-based dashboard for monitoring prediction markets on Polymarket — inspired by a Bloomberg Terminal layout. This repo is a monorepo (npm workspaces) with an API and a Web app, developed with strict TDD where practical.

## Monorepo Layout
- `packages/api` — Node.js + TypeScript + Express server (health endpoint, future Polymarket proxy)
- `packages/web` — Vite + React + TypeScript frontend

## Quick Start
- Prereqs: Node 20+ (Node 24 tested), npm 9+
- Install deps: `npm install`
- Run tests (Node runner + Vitest wrappers): `npm test`
- API
  - Dev: `npm run -w @portnoy/api dev`
  - Build: `npm run -w @portnoy/api build`
  - Start (after build): `npm run -w @portnoy/api start`
- Web
  - Dev: `npm run -w @portnoy/web dev`
  - Build: `npm run -w @portnoy/web build`
  - Preview (after build): `npm run -w @portnoy/web preview`

## Scripts (root)
- `npm test` — Runs Node’s test runner against `tests/**/*.mjs` (workspace + tooling checks) and indirectly verifies Vitest runs in both workspaces.
- `npm run typecheck` — TypeScript project-wide check (no emit).
- `npm run lint` — ESLint across `packages/`, `tools/`, and `tests/`.
- `npm run format` / `format:check` — Prettier write/check.

## Stack
- Workspaces: npm
- Language: TypeScript (tsconfig.base.json)
- Backend: Express
- Frontend: Vite + React
- Tests: Node test runner (repo infra), Vitest (packages)
- Lint/Format: ESLint + Prettier

See `STACK.md` for more details and `PRD.json`/`PRD.md` for the product plan.

