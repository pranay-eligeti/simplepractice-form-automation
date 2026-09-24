"""Map spreadsheet records to normalized form fields."""

from __future__ import annotations

from datetime import datetime
from typing import Any

REQUIRED_FIELDS = ["first_name", "last_name", "dob", "phone", "email"]


def normalize_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d")
    return " ".join(str(value).strip().split())


def map_row(row: dict[str, Any]) -> dict[str, str]:
    return {key: normalize_value(value) for key, value in row.items()}


def missing_required(record: dict[str, str]) -> list[str]:
    return [field for field in REQUIRED_FIELDS if not record.get(field)]
