import re

from playwright.sync_api import Page,expect
from UI.formulario_register_ui import FormRegisterUI
from utils.data_reader import DataReader
from base_test import BaseTest


class FormRegisterPage(FormRegisterUI,BaseTest):

    _path:str = "register_user.json"


    def fill_form_register_form(self):

        global gender,password,birt_day,month,year,first_name,last_name,company,country,address,state,city,zip_code,mobile_number

        #data = DataReader.read_json(f"resources/{self._path}")
        data = DataReader.read_excel(f"resources/data/usuarios.xlsx")

        print(data)

        for fila in data:
            print(fila)
            #get Data json
            gender = fila["gender"]
            password = fila["password"]
            """birt_day = int(fila["birt_day"])
            month = fila["month"]"""
            year = fila["year"]
            first_name = fila["first_name"]
            last_name = fila["last_name"]
            company = fila["company"]
            country = fila["country"]
            address = fila["address"]
            state = fila["state"]
            city = fila["city"]
            zip_code = fila["zip_code"]
            mobile_number = fila["mobile_number"]


        self.check_by_label(gender)
        self.fill(self.input_password,password)
        """self.select_option(self.select_data_birt_day,birt_day)
        self.select_option(self.select_data_month,month)"""
        self.select_option(self.select_data_years,year)
        self.check_by_label(self.checkbox_sing_up)
        self.check_by_label(self.checkbox_offers)
        self.fill(self.input_first_name,first_name)
        self.fill(self.input_last_name,last_name)
        self.fill(self.input_company,company)
        self.fill(self.input_address,address)
        self.select_option(self.select_data_country,country)
        self.fill(self.input_state,state)
        self.fill(self.input_city,city)
        self.fill(self.input_zip_code,zip_code)
        self.fill(self.input_mobile_number,mobile_number)
        self.click_by_role("Create Account")

    def validate_page_form(self):
        expect(self.page).to_have_url(re.compile("https://www.automationexercise.com/signup"))

    def validate_confirm_account(self):
        expect(self.page).to_have_url(re.compile("https://www.automationexercise.com/account_created"))
        #Validamos mensaje creacion de cuenta
        expect(self.page.get_by_role("heading",name="Congratulations! Your new account has been successfully created!")).to_be_visible()
