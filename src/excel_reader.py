"""Excel input adapter using openpyxl."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from openpyxl import load_workbook


def read_records(path: str | Path) -> list[dict[str, Any]]:
    workbook = load_workbook(path, read_only=True, data_only=True)
    try:
        sheet = workbook.active
        rows = sheet.iter_rows(values_only=True)
        first = next(rows, None)
        if first is None:
            raise ValueError("Spreadsheet requires a header row")
        headers = [str(value).strip() if value is not None else "" for value in first]
        if any(not header for header in headers) or len(headers) != len(set(headers)):
            raise ValueError("Spreadsheet headers must be nonblank and unique")
        return [dict(zip(headers, row)) for row in rows if any(value is not None for value in row)]
    finally:
        workbook.close()
