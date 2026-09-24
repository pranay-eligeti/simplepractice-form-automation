"""Playwright form-filling adapter for an approved target page.

The public implementation uses stable data-testid selectors and is intended
for a local/synthetic fixture. It does not contain login credentials or
production-site selectors.
"""

from __future__ import annotations

from playwright.async_api import Page


async def fill_intake(page: Page, record: dict[str, str]) -> None:
    await page.get_by_test_id("first-name").fill(record["first_name"])
    await page.get_by_test_id("last-name").fill(record["last_name"])
    await page.get_by_test_id("dob").fill(record["dob"])
    await page.get_by_test_id("phone").fill(record["phone"])
    await page.get_by_test_id("email").fill(record["email"])

    if record.get("address"):
        await page.get_by_test_id("address").fill(record["address"])
    if record.get("city"):
        await page.get_by_test_id("city").fill(record["city"])
    if record.get("state"):
        await page.get_by_test_id("state").fill(record["state"])
    if record.get("zip"):
        await page.get_by_test_id("zip").fill(record["zip"])


async def submit(page: Page) -> None:
    await page.get_by_test_id("submit").click()
