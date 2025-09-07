import assert from 'node:assert/strict';
import { test } from 'node:test';
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const root = process.cwd();
const apiDir = path.join(root, 'packages', 'api');

test('api package files and scripts exist', () => {
  assert.ok(fs.existsSync(path.join(apiDir, 'tsconfig.json')), 'api tsconfig.json missing');
  assert.ok(fs.existsSync(path.join(apiDir, 'src', 'server.ts')), 'api src/server.ts missing');
  const pkg = JSON.parse(fs.readFileSync(path.join(apiDir, 'package.json'), 'utf8'));
  for (const s of ['build', 'start', 'dev']) {
    assert.ok(pkg.scripts && pkg.scripts[s], `api script ${s} missing`);
  }
});

test('api builds to dist/server.js', () => {
  const res = spawnSync('npm', ['run', '-w', '@portnoy/api', '-s', 'build'], { cwd: root, encoding: 'utf8' });
  assert.equal(res.status, 0, `api build failed: ${res.stderr || res.stdout}`);
  assert.ok(fs.existsSync(path.join(apiDir, 'dist', 'server.js')), 'dist/server.js missing');
});

