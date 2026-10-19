# Vercel CI/CD Demo

A minimal static website demonstrating GitHub-driven deployment on Vercel, with automated HTML and documentation checks.

[![Verify](https://github.com/fizaamjd/vercel-ci-cd-demo/actions/workflows/verify.yml/badge.svg)](https://github.com/fizaamjd/vercel-ci-cd-demo/actions/workflows/verify.yml)

## Overview

A plain HTML page is deployed by the existing Vercel Git integration. GitHub Actions checks source validity separately; it does not own or prove the Vercel deployment configuration.

## Getting started

```sh
git clone https://github.com/fizaamjd/vercel-ci-cd-demo.git
cd vercel-ci-cd-demo
python3 scripts/check-site.py
python3 scripts/check-docs.py
```

## Preview and deployment

```sh
python3 -m http.server 8000
```

Open http://localhost:8000. Vercel serves the root directory as a static site with no build command. Connect the repository in Vercel to deploy pushes; this requires an existing authorized integration. The displayed deployment label is public. No dotenv, Node runtime, account or secret is needed.

## Maintenance

- [Architecture](docs/architecture.md)
- [Configuration](docs/configuration.md)
- [Verification](docs/testing.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)
- [Support](SUPPORT.md)
- [License scope](docs/license-scope.md)

Original coursework history and contributors are preserved.
