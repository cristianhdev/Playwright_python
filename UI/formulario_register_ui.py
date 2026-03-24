from playwright.sync_api import Page

class FormRegisterUI:

    #Input password
    @property
    def input_password(self):
        return "[data-qa='password']"

    #Select data birt - day
    @property
    def select_data_birt_day(self):
        return "[data-qa='days']"

    #Select data birt - months
    @property
    def select_data_month(self):
        return "[data-qa='months']"

    #Select data birt - years
    @property
    def select_data_years(self):
        return "[data-qa='years']"

    #Checkbox Sing Up newsletter
    @property
    def checkbox_sing_up(self):
        return "Sign up for our newsletter!"

    #Checkbox Receive special offers from our partners!
    @property
    def checkbox_offers(self):
        return "Receive special offers from our partners!"

    #Input first_name
    @property
    def input_first_name(self):
        return "[data-qa='first_name']"

    #Input last_name
    @property
    def input_last_name(self):
        return "[data-qa='last_name']"

    #Input company
    @property
    def input_company(self):
        return "[data-qa='company']"

    #Select country
    @property
    def select_data_country(self):
        return "[data-qa='country']"

    #Input address
    @property
    def input_address(self):
        return "[data-qa='address']"

    #Input state
    @property
    def input_state(self):
        return "[data-qa='state']"

    #Input city
    @property
    def input_city(self):
        return "[data-qa='city']"

    #Input zip_code
    @property
    def input_zip_code(self):
        return "[data-qa='zipcode']"

    #Input zip_code
    @property
    def input_mobile_number(self):
        return "[data-qa='mobile_number']"