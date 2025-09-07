import assert from 'node:assert/strict';
import { test } from 'node:test';
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const root = process.cwd();

function hasScript(name) {
  const pkg = JSON.parse(fs.readFileSync(path.join(root, 'package.json'), 'utf8'));
  return Boolean(pkg.scripts && pkg.scripts[name]);
}

test('shared config files exist', () => {
  assert.ok(fs.existsSync(path.join(root, 'tsconfig.base.json')), 'tsconfig.base.json missing');
  assert.ok(
    fs.existsSync(path.join(root, '.eslintrc.cjs')) || fs.existsSync(path.join(root, '.eslintrc.json')),
    'ESLint config missing'
  );
  assert.ok(
    fs.existsSync(path.join(root, 'prettier.config.cjs')) || fs.existsSync(path.join(root, '.prettierrc')) || fs.existsSync(path.join(root, '.prettierrc.json')),
    'Prettier config missing'
  );
});

test('package scripts defined for tooling', () => {
  for (const s of ['typecheck', 'lint', 'format', 'format:check']) {
    assert.ok(hasScript(s), `script ${s} missing`);
  }
});

test('typecheck script runs successfully', () => {
  const res = spawnSync('npm', ['run', '-s', 'typecheck'], { cwd: root, encoding: 'utf8' });
  assert.equal(res.status, 0, `typecheck failed: ${res.stderr || res.stdout}`);
});

