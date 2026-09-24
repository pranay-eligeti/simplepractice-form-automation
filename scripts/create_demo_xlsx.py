"""Create a synthetic XLSX input file for the local demo."""

from pathlib import Path
from openpyxl import Workbook

OUTPUT = Path(__file__).resolve().parents[1] / "sample_data" / "demo_clients.xlsx"

workbook = Workbook()
sheet = workbook.active
headers = [
    "first_name", "last_name", "dob", "phone", "email",
    "address", "city", "state", "zip"
]
sheet.append(headers)
sheet.append([
    "Alex", "Example", "1990-05-15", "555-123-4567", "alex@example.com",
    "100 Example Ave", "Columbus", "OH", "43215"
])
workbook.save(OUTPUT)
print(f"Created {OUTPUT}")
