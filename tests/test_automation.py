from openpyxl import Workbook
from src.excel_reader import read_records
from src.field_mapper import map_row, missing_required
import pytest


def test_mapping_and_required_validation(tmp_path):
    path = tmp_path / "clients.xlsx"
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(["first_name", "last_name", "dob", "phone", "email"])
    sheet.append(["Alex", "Example", "1990-05-15", "555-123-4567", "alex@example.com"])
    workbook.save(path)
    record = map_row(read_records(path)[0])
    assert record["first_name"] == "Alex"
    assert missing_required(record) == []


def test_missing_required_field_is_reported():
    record = map_row({"first_name": "Alex", "last_name": "", "dob": "", "phone": "", "email": ""})
    assert "last_name" in missing_required(record)


@pytest.mark.parametrize("headers", [[], ["first_name", "first_name"], ["first_name", None]])
def test_invalid_headers_fail_clearly(tmp_path, headers):
    workbook = Workbook()
    if headers:
        workbook.active.append(headers)
    path = tmp_path / "bad.xlsx"
    workbook.save(path)
    workbook.close()
    with pytest.raises(ValueError, match="header"):
        read_records(path)


def test_browser_batch_continues_after_invalid_row(tmp_path, monkeypatch, caplog):
    import asyncio
    import logging
    from pathlib import Path
    from src import main

    workbook = Workbook()
    sheet = workbook.active
    sheet.append(["first_name", "last_name", "dob", "phone", "email"])
    sheet.append(["Alex", None, "1990-05-15", "555-0100", "alex@example.com"])
    sheet.append(["Alex", "Example", "1990-05-15", "555-0100", "alex@example.com"])
    sheet.append(["Failure", "Example", "1990-05-15", "555-0100", "alex@example.com"])
    source = tmp_path / "synthetic.xlsx"
    workbook.save(source)
    workbook.close()
    monkeypatch.setattr(main, "get_logger", lambda: logging.getLogger("offline-test"))
    original_fill = main.fill_intake

    async def fill(page, record):
        if record["first_name"] == "Failure":
            raise RuntimeError("dummy private submitted fields")
        await original_fill(page, record)

    monkeypatch.setattr(main, "fill_intake", fill)
    fixture = Path(__file__).resolve().parents[1] / "sample_data/intake_fixture.html"
    with caplog.at_level(logging.INFO):
        assert asyncio.run(main.run(str(source), str(fixture))) == 2
    assert "row=3 status=success" in caplog.text
    assert "row=4 status=browser_failed type=RuntimeError" in caplog.text
    assert "dummy private submitted fields" not in caplog.text
