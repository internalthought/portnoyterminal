/** @type {import('eslint').Linter.Config} */
module.exports = {
  root: true,
  env: { node: true, es2022: true, browser: true },
  parser: '@typescript-eslint/parser',
  parserOptions: { ecmaVersion: 'latest', sourceType: 'module' },
  plugins: ['@typescript-eslint', 'import'],
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:import/recommended',
    'plugin:import/typescript',
    'prettier'
  ],
  ignorePatterns: [
    'node_modules/',
    'dist/',
    'build/',
    '.codex/',
    'polymarket_docs/',
    '**/*.d.ts'
  ],
  settings: {
    'import/resolver': {
      node: { extensions: ['.js', '.mjs', '.cjs', '.ts', '.tsx', '.json'] }
    }
  },
  rules: {
    'import/order': ['warn', { 'newlines-between': 'always' }]
  }
};

