## OpenAI Codex Agents for AIPAC Transparency Platform

---

### **Table of Contents**

1. [Overview](#overview)
2. [Agent Roles](#agent-roles)
3. [Data Collection Agent](#data-collection-agent)
4. [Data Processing & Enrichment Agent](#data-processing--enrichment-agent)
5. [Profile Generation Agent](#profile-generation-agent)
6. [Web Interface Agent](#web-interface-agent)
7. [Testing & Validation Agent](#testing--validation-agent)
8. [Automation & Scheduling Agent](#automation--scheduling-agent)
9. [Contribution Guidelines](#contribution-guidelines)
10. [Best Practices](#best-practices)
11. [Extending & Customizing Agents](#extending--customizing-agents)
12. [References](#references)

---

## 1. **Overview**

This project leverages OpenAI Codex and modern AI coding agents to automate the development and upkeep of the **AIPAC Transparency Platform**. Each agent is specialized for a key workflow, enabling efficient, auditable, and scalable progress.

All code, data, and agent configurations should be stored in the `aipac.marad.trade` GitHub repository.

---

## 2. **Agent Roles**

Each agent is a Python or JS script, notebook, or API interface, designed to run **standalone or as part of a CI/CD pipeline**.

* **Data Collection Agent:** Gathers campaign finance and voting records from public sources.
* **Data Processing Agent:** Cleans, deduplicates, enriches, and normalizes raw data.
* **Profile Generation Agent:** Compiles per-official profiles (Markdown/JSON/HTML).
* **Web Interface Agent:** Generates/upgrades static site front-end code.
* **Testing Agent:** Validates data integrity, code correctness, and site usability.
* **Automation Agent:** Schedules and orchestrates all pipelines.

---

## 3. **Data Collection Agent**

**Purpose:**
Automate data gathering from:

* FEC, OpenSecrets, state campaign finance portals
* Congressional and state legislature roll-call records
* Public official directories

**Instructions:**

* Use APIs where available (e.g., [FEC API](https://api.open.fec.gov/), [OpenSecrets API](https://www.opensecrets.org/open-data/api)).
* For non-API sites, use legal scraping (BeautifulSoup/Selenium), always respecting robots.txt.
* Save raw data as versioned CSV/JSON in `/data/raw/`.
* Log source, timestamp, query parameters, and script version for every extraction.
* Example:

  ```python
  # Codex Prompt: Write a Python script to download all AIPAC donations to US Senators from the FEC API for 2020-2024.
  ```

**Output:**

* `donations_raw_YYYYMMDD.csv`
* `votes_raw_YYYYMMDD.csv`
* Metadata logs

---

## 4. **Data Processing & Enrichment Agent**

**Purpose:**
Transform raw data into clean, joined datasets suitable for analysis and publishing.

**Instructions:**

* Deduplicate by recipient and cycle.
* Standardize names and offices.
* Link donation records to biographical info (name, photo, state/district, tenure).
* Flag ambiguous or incomplete data for human review.
* Enrich voting records: match roll calls to bills of interest (AIPAC priorities).
* Validate against source (FEC/OpenSecrets).
* Output normalized CSV/JSON to `/data/processed/`.

**Output:**

* `officials_cleaned.json`
* `donations_cleaned.json`
* `votes_tagged.json`
* `profile_data.json`

---

## 5. **Profile Generation Agent**

**Purpose:**
Generate detailed profile pages for each official, combining all relevant data.

**Instructions:**

* For each official, compile:

  * Photo
  * Office, state/district, tenure
  * All AIPAC-related donations (with source links)
  * Voting record on tagged bills
  * Notable public statements (with citations)
* Render profile to Markdown and/or HTML (for static site).
* Store in `/profiles/[official_id].md` and/or `/site/profiles/[official_id].html`
* Link all data to source URLs for auditability.

**Output:**

* Individual profile files, eg: `/profiles/john-doe.md`
* Table of all officials for web front-end

---

## 6. **Web Interface Agent**

**Purpose:**
Automate static site generation and front-end upgrades using Next.js, Jekyll, or similar.

**Instructions:**

* Parse processed data and profiles into site pages.
* Ensure search, filtering, and state/district navigation.
* Keep site structure modular and accessible.
* For design changes, generate or update Tailwind/React/HTML as needed.
* Push preview builds to GitHub Pages or the target host.

**Output:**

* `/site/` static files
* `/site/index.html`
* Updated `/site/profiles/`

---

## 7. **Testing & Validation Agent**

**Purpose:**
Enforce quality, consistency, and legal compliance.

**Instructions:**

* Run test suites on all data and code.
* Validate:

  * Data accuracy (sample checks)
  * Proper linking/citations
  * No personal addresses/contact info present
  * ADA/accessibility checks
* Lint and format all scripts, HTML, and Markdown.

**Output:**

* Test logs in `/logs/`
* Issue tickets for any failures

---

## 8. **Automation & Scheduling Agent**

**Purpose:**
Automate the execution of all agents and update the repository/site on schedule.

**Instructions:**

* Set up GitHub Actions, cron jobs, or similar to:

  * Fetch new data (weekly or on major campaign finance releases)
  * Re-run processing and site build pipelines
  * Notify contributors of required human review
* Document all automation workflows in `/automation/README.md`

---

## 9. **Contribution Guidelines**

* **Code:**

  * Use clear, commented scripts and notebooks.
  * Submit via pull requests; require code review for merges.
  * Maintain changelogs and versioning.
* **Data:**

  * All sources must be publicly available and legally accessible.
  * No scraping of personal/private information.
  * Always cite the exact URL and retrieval date.
* **Ethics:**

  * Do not harass or enable harassment of officials.
  * Remove any data if proven inaccurate or nonpublic.

---

## 10. **Best Practices**

* Use environment variables for API keys (never commit credentials).
* Modularize all scripts—one agent per file/module.
* Store raw and processed data separately.
* Regularly archive and backup all data.
* Foster community input—make everything verifiable and auditable.

---

## 11. **Extending & Customizing Agents**

* Add new agents for social media monitoring, FOIA request tracking, or other sources as needed.
* Modularize data models to support local/state/federal levels.
* Encourage contributions from transparency, legal, and data science communities.

---

## 12. **References**

* [FEC API Documentation](https://api.open.fec.gov/developers/)
* [OpenSecrets API Docs](https://www.opensecrets.org/open-data/api)
* [GitHub Actions Docs](https://docs.github.com/en/actions)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* [Next.js Static Site Generation](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)
* [Contributor Covenant](https://www.contributor-covenant.org/)

---

## **Appendix: Example Codex Prompts**

```plaintext
# Codex Prompt: Write a script to fetch all AIPAC PAC donations to any congressional candidate from OpenSecrets for 2022, save as CSV.
```

```plaintext
# Codex Prompt: Generate a Markdown profile for Rep. Jane Smith, including all donation and voting data, with links to each source.
```

```plaintext
# Codex Prompt: Create a React component for displaying an official's profile card, taking JSON input for all fields.
```

---

## **End of agents.md**
