# 📋 SimplePractice Client Intake Form Automation

> A Python + Playwright browser automation tool that reads client data from Excel and automatically fills out SimplePractice multi-page intake forms — eliminating all repetitive manual data entry during client onboarding.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Playwright](https://img.shields.io/badge/Playwright-Browser%20Automation-green)
![openpyxl](https://img.shields.io/badge/openpyxl-Excel-brightgreen)

---

## What It Does

Reads structured client onboarding data from an Excel file and uses Playwright to navigate SimplePractice's multi-page intake forms, filling in all fields automatically — including text inputs, dropdowns, date pickers, checkboxes, and multi-step form navigation — with full error recovery and structured logging.

---

## The Problem It Solves

Client intake in SimplePractice requires filling out 5-10 pages of forms per client. With multiple new clients per week, this becomes hours of repetitive copy-paste work. This automation:

- Reads any number of client rows from Excel
- Completes each intake form end-to-end in minutes
- Handles errors gracefully without losing progress
- Logs every action for audit trail

---

## How It Works

```
Excel File (client data)
        │
        ▼
openpyxl reader
  → Reads each client row
  → Maps columns to form fields
  → Validates required fields before starting
        │
        ▼
Playwright browser automation
  → Navigates to SimplePractice intake URL
  → Page 1: Personal Information
      - First/Last name, DOB, gender
      - Address, phone, email
  → Page 2: Insurance Information
      - Payer name, member ID, group number
  → Page 3: Emergency Contact
      - Contact name, relationship, phone
  → Page 4: Consent Forms
      - Checkbox acknowledgements
  → Page 5: Signature / Submit
      - Final review and submission
        │
        ▼
Structured Log Output
  → Success / failure per client
  → Field-level error reporting
  → Resume from last failed row
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core automation logic |
| Playwright | Browser automation (Chromium) |
| openpyxl | Excel file reading |
| asyncio | Async page interactions |
| logging | Structured audit trail |

---

## Key Features

- **Multi-page handling** — navigates across all form pages automatically
- **Dropdown selection** — handles dynamic dropdowns with search and select
- **Date picker support** — formats and enters dates into calendar widgets
- **Error recovery** — skips failed clients, logs errors, continues with next row
- **Headless mode** — runs silently in the background without opening a visible browser
- **Resume capability** — restarts from the last failed client row

---

## Project Structure

```
simplepractice-form-automation/
├── src/
│   ├── main.py              # Entry point
│   ├── excel_reader.py      # openpyxl data extraction
│   ├── form_filler.py       # Playwright form automation
│   ├── field_mapper.py      # Excel column → form field mapping
│   └── logger.py            # Structured logging
├── templates/
│   └── client_data_template.xlsx   # Excel template for client data
├── .env.example
├── requirements.txt
└── README.md
```

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/pranay-eligeti/simplepractice-form-automation.git
cd simplepractice-form-automation
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Prepare your Excel file
Use the template in `templates/client_data_template.xlsx` and fill in your client data.

### 4. Configure environment
```bash
cp .env.example .env
# Add your SimplePractice credentials
```

### 5. Run the automation
```bash
python src/main.py --input data/clients.xlsx
```

---

## Environment Variables

```env
# .env.example
SIMPLEPRACTICE_EMAIL=your_login_email
SIMPLEPRACTICE_PASSWORD=your_login_password
SIMPLEPRACTICE_PRACTICE_ID=your_practice_id
HEADLESS=true
OUTPUT_LOG=./logs/run.log
```

---

## Excel Template Format

| Column | Required | Example |
|--------|----------|---------|
| first_name | ✅ | John |
| last_name | ✅ | Doe |
| dob | ✅ | 1990-05-15 |
| gender | ✅ | Male |
| phone | ✅ | 555-123-4567 |
| email | ✅ | john@email.com |
| address | ✅ | 123 Main St |
| city | ✅ | Columbus |
| state | ✅ | OH |
| zip | ✅ | 43215 |
| insurance_payer | ⬜ | Aetna |
| member_id | ⬜ | MEM123456 |
| emergency_contact_name | ⬜ | Jane Doe |
| emergency_contact_phone | ⬜ | 555-987-6543 |

---

## Requirements

```
playwright>=1.40.0
openpyxl>=3.1.0
python-dotenv>=1.0.0
```

---

## ⚠️ Important Note

This tool automates interactions with SimplePractice's web interface. Ensure your usage complies with SimplePractice's Terms of Service and your organization's data handling policies. Never commit real client data to this repository — all PHI must remain local.

---

## Author

**Pranay Eligeti** — [linkedin.com/in/pranay-eligeti](https://linkedin.com/in/pranay-eligeti)
