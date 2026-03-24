import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.automationexercise.com/")
    page.get_by_role("link", name=" Signup / Login").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill("calosperez@hotmail.com")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("Tab")
    page.get_by_role("textbox", name="Password").fill("121167")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Login").click()
    page.locator("form").filter(has_text="Login").click()
    page.get_by_role("button", name="Login").click()
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("1234568")
    page.get_by_role("button", name="Login").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("ArrowLeft")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("ArrowLeft")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("ArrowLeft")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("ArrowLeft")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("ArrowLeft")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("ArrowLeft")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("ArrowLeft")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("ArrowLeft")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("ArrowLeft")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("ArrowRight")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill("crishernandez10@hotmail.com")
    page.get_by_role("button", name="Login").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
