# Automation

This folder contains data agent scripts and scheduling utilities. The main agent
provided is `fetch_aipac_donations.py`, which downloads AIPAC PAC disbursements
to congressional candidates from the FEC API.

## Scheduled Runs

Use GitHub Actions or cron on your server to execute the agents regularly. The
included CI workflow runs unit tests on every push or pull request.
