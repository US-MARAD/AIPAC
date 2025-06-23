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

## Setup

1. Copy `.env.example` to `.env` and add your API keys.
2. Install dependencies and run tests:

```bash
python -m pip install -r requirements.txt
pytest -v
```

Use `docker compose up --build -d` to start all services.

The `automation/fetch_aipac_donations.py` script downloads AIPAC PAC disbursements from the FEC API and saves them under `data/raw/`.

See `AGENTS.md` for full project guidelines.
