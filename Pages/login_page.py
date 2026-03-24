
from playwright.sync_api import Page,expect
from base_test  import BaseTest
from UI.login_ui import LoginUI

class LoginPage(LoginUI,BaseTest):

     _ERROR_LOGIN = "Your email or password is incorrect!"

     def __init__(self, page: Page):
         super().__init__(page)


     def navigate(self):
         self.page.goto("https://www.automationexercise.com/login")


     def form_login_fill(self,email,password):
         self.fill(self.email_input,email)
         self.fill(self.password_input,password)
         self.click(self.send_form_button)

     def validate_form_login_success(self,usuariologin):
         expect(self.page.get_by_text(usuariologin)).to_be_visible(timeout=40000)

     def validate_form_login_fail(self):
         expect(self.page.get_by_text(self._ERROR_LOGIN)).to_be_visible(timeout=40000)