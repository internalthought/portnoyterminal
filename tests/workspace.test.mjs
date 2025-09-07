import assert from 'node:assert/strict';
import { test } from 'node:test';
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();

function readJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

test('root package.json declares workspaces packages/*', () => {
  const pkgPath = path.join(root, 'package.json');
  assert.ok(fs.existsSync(pkgPath), 'root package.json missing');
  const pkg = readJson(pkgPath);
  assert.ok(Array.isArray(pkg.workspaces), 'workspaces must be an array');
  assert.ok(pkg.workspaces.includes('packages/*'), 'workspaces must include packages/*');
});

test('workspace folders exist: packages/api and packages/web', () => {
  const apiDir = path.join(root, 'packages', 'api');
  const webDir = path.join(root, 'packages', 'web');
  assert.ok(fs.existsSync(apiDir), 'packages/api should exist');
  assert.ok(fs.existsSync(webDir), 'packages/web should exist');
});

test('each workspace has a package.json', () => {
  for (const name of ['api', 'web']) {
    const dir = path.join(root, 'packages', name);
    const pkgPath = path.join(dir, 'package.json');
    assert.ok(fs.existsSync(pkgPath), `${name} package.json missing`);
    const pkg = readJson(pkgPath);
    assert.equal(pkg.name, `@portnoy/${name}`);
    assert.equal(pkg.type, 'module');
  }
});

