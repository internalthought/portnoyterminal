import assert from 'node:assert/strict';
import { test } from 'node:test';
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const root = process.cwd();
const webDir = path.join(root, 'packages', 'web');

test('web package files and scripts exist', () => {
  const pkgPath = path.join(webDir, 'package.json');
  assert.ok(fs.existsSync(pkgPath), 'web package.json missing');
  assert.ok(fs.existsSync(path.join(webDir, 'tsconfig.json')), 'web tsconfig.json missing');
  assert.ok(fs.existsSync(path.join(webDir, 'vite.config.ts')), 'web vite.config.ts missing');
  assert.ok(fs.existsSync(path.join(webDir, 'index.html')), 'web index.html missing');
  assert.ok(fs.existsSync(path.join(webDir, 'src', 'main.tsx')), 'web src/main.tsx missing');
  assert.ok(fs.existsSync(path.join(webDir, 'src', 'App.tsx')), 'web src/App.tsx missing');
  const pkg = JSON.parse(fs.readFileSync(pkgPath, 'utf8'));
  for (const s of ['dev', 'build', 'preview']) {
    assert.ok(pkg.scripts && pkg.scripts[s], `web script ${s} missing`);
  }
});

test('web builds with Vite', () => {
  const res = spawnSync('npm', ['run', '-w', '@portnoy/web', '-s', 'build'], { cwd: root, encoding: 'utf8' });
  assert.equal(res.status, 0, `web build failed: ${res.stderr || res.stdout}`);
  assert.ok(fs.existsSync(path.join(webDir, 'dist', 'index.html')), 'web dist/index.html missing');
});

