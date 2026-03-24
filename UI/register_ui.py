from playwright.sync_api import Page

class RegisterPageUI:

    def __init__(self,page:Page):
        self.page = page

    @property
    def name_input(self):
        # en el  nombre en el campo name del formulario de registro.
        return "[data-qa='signup-name']"

    @property
    def email_input(self):
        return "[data-qa='signup-email']"

    @property
    def send_button(self):
        return "[data-qa='signup-button']"

    @property
    def title_validate_register(self):
        return self.page.get_by_role("heading",name="Enter Account Information")