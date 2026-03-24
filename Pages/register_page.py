import re
from playwright.sync_api import Page,expect
from base import *
from base_test  import BaseTest
from UI.register_ui import RegisterPageUI
from utils.data_reader import DataReader


class RegisterPage(RegisterPageUI,BaseTest):

    _path:str = "credenciales_user.json"


    def navidate(self):
        self.page.goto(base_url)
        self.page.get_by_role("link",name="Signup / Login").click()

    def form_regiter_fill(self):


        data = DataReader.read_json(f"resources/{self._path}")

        self.fill(self.name_input,data["user"])
        # Dar tab
        self.page.keyboard.press("Tab")
        self.fill(self.email_input,data["email"])
        #Clic en el boton Signup
        self.click(self.send_button)

    def validate_title_page(self):
        expect(self.page).to_have_title(re.compile(title_page))

        #Validamos que el titulo del formulario de registro este visible
        expect(self.page.get_by_role("heading",name="New User Signup!")).to_be_visible()

    def validate_title_register(self):
        expect(self.title_validate_register).to_be_visible()






