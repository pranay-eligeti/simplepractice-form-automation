"""CLI for the sanitized spreadsheet-to-browser automation demo."""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from .excel_reader import read_records
from .field_mapper import map_row, missing_required
from .form_filler import fill_intake, submit
from .logger import get_logger


async def run(input_path: str, fixture_path: str) -> int:
    logger = get_logger()
    records = [map_row(row) for row in read_records(input_path)]
    failures = 0

    from playwright.async_api import async_playwright

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        try:
            for index, record in enumerate(records, start=2):
                missing = missing_required(record)
                if missing:
                    failures += 1
                    logger.error("row=%s status=validation_failed missing=%s", index, missing)
                    continue

                page = await browser.new_page()
                try:
                    await page.goto(Path(fixture_path).resolve().as_uri())
                    await fill_intake(page, record)
                    await submit(page)
                    await page.get_by_test_id("success").wait_for()
                    logger.info("row=%s status=success", index)
                except Exception as exc:
                    failures += 1
                    logger.exception("row=%s status=browser_failed error=%s", index, exc)
                finally:
                    await page.close()
        finally:
            await browser.close()

    logger.info("run_complete records=%s failures=%s", len(records), failures)
    return failures


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the sanitized intake automation demo.")
    parser.add_argument("--input", required=True, help="Synthetic XLSX input")
    parser.add_argument("--fixture", required=True, help="Local HTML form fixture")
    args = parser.parse_args()
    failures = asyncio.run(run(args.input, args.fixture))
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
