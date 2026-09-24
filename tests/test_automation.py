from openpyxl import Workbook
from src.excel_reader import read_records
from src.field_mapper import map_row, missing_required


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
