# Stack

- Package manager: npm workspaces
- Language: TypeScript (strict), project base config in `tsconfig.base.json`
- Backend (packages/api): Node.js + Express, compiled with `tsc`
- Frontend (packages/web): Vite + React + TypeScript
- Tests: 
  - Repository infra tests via Node’s built-in test runner (`node --test`)
  - Package-level tests via Vitest (`vitest`)
- Linting/Formatting: ESLint + Prettier

Rationale:
- npm workspaces keep API and Web in a single repo with shared tooling.
- TypeScript strict mode ensures early correctness.
- Express is a minimal, reliable baseline for the API proxy.
- Vite + React deliver fast DX and simple static output.
- Node test runner guards workspace/tooling guarantees; Vitest focuses on unit tests in each package.

