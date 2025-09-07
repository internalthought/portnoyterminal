import assert from 'node:assert/strict';
import { test } from 'node:test';
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const root = process.cwd();

test('vitest config files exist', () => {
  const apiCfg = path.join(root, 'packages', 'api', 'vitest.config.ts');
  const webCfg = path.join(root, 'packages', 'web', 'vitest.config.ts');
  assert.ok(fs.existsSync(apiCfg), 'api vitest.config.ts missing');
  assert.ok(fs.existsSync(webCfg), 'web vitest.config.ts missing');
});

test('vitest runs in api and web', () => {
  const api = spawnSync('npm', ['run', '-w', '@portnoy/api', '-s', 'test:unit'], { cwd: root, encoding: 'utf8' });
  assert.equal(api.status, 0, `api vitest failed: ${api.stderr || api.stdout}`);
  const web = spawnSync('npm', ['run', '-w', '@portnoy/web', '-s', 'test:unit'], { cwd: root, encoding: 'utf8' });
  assert.equal(web.status, 0, `web vitest failed: ${web.stderr || web.stdout}`);
});

