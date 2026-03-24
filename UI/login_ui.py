from playwright.sync_api import Page

class LoginUI:

    def __init__(self,page:Page):
        self.page = page

    @property
    def email_input(self)->str:
        return "[data-qa='login-email']"

    @property
    def password_input(self)->str:
        return "[data-qa='login-password']"

    @property
    def send_form_button(self)->str:
        return "[data-qa='login-button']"