# AIPAC Transparency Platform

This repository hosts the code and data for the AIPAC Transparency Platform. It follows the directory layout and Docker-based workflows described in `AGENTS.md`.

## Repository Structure

```
/data/                 - Input and output datasets
  /raw/
  /processed/
/profiles/             - Per-official data and profiles
/site/                 - Frontend application
/api/                  - Backend API services
/automation/           - Data agent scripts and workers
/docker/               - Docker configuration and entrypoints
/tests/                - Unit and integration tests
```

Use `docker compose up --build -d` to start all services.

See `AGENTS.md` for full project guidelines.
