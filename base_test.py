import allure

from playwright.sync_api import Page

class BaseTest:

    def __init__(self, page:Page):
        self.page = page

    #@allure.step
    def fill(self, locator, text, step="Llenar campo"):
        with allure.step(f"{step}: {text}"):
            self.page.locator(locator).fill(text)

    def click(self, locator, step="Click en elemento"):
        with allure.step(step):
            self.page.locator(locator).click()

    def check(self, locator, step="Seleccionar opción"):
        with allure.step(step):
            self.page.locator(locator).check()

    def select_option(self, locator, value, step="Seleccionar opción"):
        with allure.step(f"{step}: {value}"):
            self.page.locator(locator).select_option(value)

    def check_by_label(self, label, step="Seleccionar opción"):
        with allure.step(f"{step}: {label}"):
            self.page.get_by_label(label).check()

    def fill_by_role(self, locator_name, text, step="Llenar campo"):
        with allure.step(f"{step}: {text}"):
            self.page.get_by_role("textbox",name=locator_name).fill(text)

    def click_by_role(self, locator_name, step="Click en elemento"):
        with allure.step(step):
            self.page.get_by_role("button",name=locator_name).click()

    def check_by_role(self, locator_name, step="Seleccionar opción"):
        with allure.step(step):
            self.page.get_by_role("checkbox",name=locator_name).check()

    def select_option_by_role(self, locator_name, value, step="Seleccionar opción"):
        with allure.step(f"{step}: {value}"):
            self.page.get_by_role("combobox",name=locator_name).select_option(value)