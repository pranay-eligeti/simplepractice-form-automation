# 📋 Spreadsheet-Driven Browser Automation

> A sanitized, runnable Python + Playwright portfolio project demonstrating Excel-driven data mapping, browser form automation, validation, success verification, and structured logging.

[![Python CI](https://github.com/pranay-eligeti/simplepractice-form-automation/actions/workflows/ci.yml/badge.svg)](https://github.com/pranay-eligeti/simplepractice-form-automation/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)
![Playwright](https://img.shields.io/badge/Playwright-browser%20automation-green)
![openpyxl](https://img.shields.io/badge/openpyxl-Excel-brightgreen)

## What this repository demonstrates

I have built spreadsheet-driven browser automation for repetitive healthcare operations workflows.

This repository is the **public, sanitized implementation of that engineering pattern**. It uses synthetic XLSX and HTML fixtures so the workflow can be tested without exposing client data, PHI, credentials, private URLs, or proprietary production selectors.

### Engineering capabilities

- Excel ingestion with **openpyxl**
- Field mapping and required-field validation
- Async browser automation with **Playwright**
- Stable `data-testid` selectors
- Per-record failure handling
- Success-state verification
- Structured logging
- Automated tests and GitHub Actions CI

## Architecture

~~~text
Synthetic XLSX
     |
     v
openpyxl reader
     |
     v
field mapping + validation
     |
     v
Playwright browser
     |
     v
form field filling
     |
     v
submit + success verification
     |
     v
structured logging
~~~

See docs/architecture.md for design notes.

## Repository structure

~~~text
simplepractice-form-automation/
├── .github/workflows/ci.yml
├── docs/architecture.md
├── sample_data/intake_fixture.html
├── src/
│   ├── __init__.py
│   ├── excel_reader.py
│   ├── field_mapper.py
│   ├── form_filler.py
│   ├── logger.py
│   └── main.py
├── tests/test_automation.py
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
~~~

## Quick start

~~~bash
git clone https://github.com/pranay-eligeti/simplepractice-form-automation.git
cd simplepractice-form-automation
python -m venv .venv

# Windows
.venv\\Scripts\\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
playwright install chromium
~~~

## Run tests

~~~bash
pytest -q
~~~

## Run the synthetic end-to-end demo

Generate the synthetic XLSX first:

~~~bash
python scripts/create_demo_xlsx.py
~~~

Then run the browser workflow:

~~~bash
python -m src.main --input sample_data/demo_clients.xlsx --fixture sample_data/intake_fixture.html
~~~

The public fixture does not connect to SimplePractice. It exercises the same engineering pattern against a local synthetic page.

## Design details

**Validation before automation**  
Required fields are checked before opening the browser for a record.

**Selector isolation**  
Browser selectors are kept in `form_filler.py`, making UI changes easier to test and maintain.

**Failure isolation**  
A failed record is logged and counted without silently terminating the remaining batch.

**Reproducibility**  
CI uses synthetic fixtures instead of a live third-party application.

## Privacy and security

Never commit real client records, PHI, credentials, session cookies, screenshots containing sensitive information, or private application URLs.

The repository intentionally does not contain production credentials or live SimplePractice selectors. Any real deployment must use approved access and comply with the organization's data-handling requirements and the target application's terms.

## Portfolio note

Professional implementations can contain additional multi-page workflows, dropdowns, date pickers, consent steps, retries, resume checkpoints, and application-specific selectors. This repository makes the underlying engineering pattern **visible, reproducible, testable, and explainable** without publishing private production automation.

## Author

**Pranay Eligeti**

[LinkedIn](https://www.linkedin.com/in/pranay-eligeti) · [GitHub](https://github.com/pranay-eligeti)
