"""import pytest
from playwright.sync_api import Page
from Pages.RegisterPage import RegisterPage


@pytest.mark.parametrize("user,email", [
    ("Camilo", "Camilor1234@hotmail.com"),
    ("Cristian", "CristianHernandez@hotmail.com"),
])
def test_register(page:Page, user,email):

    register_page=  RegisterPage(page)

    try:
        register_page.navidate()

        #Validamos si la pagina contiene el titulo "Automation Exercise"
        register_page.validate_title_page()

        #Ingresamos información en el formulario.
        register_page.form_regiter_fill(user,email)

        register_page.validate_title_register()

    except Exception as error:
        page.screenshot(path="screenshots/register_error.png")
        raise AssertionError(f"Test register falló: {error}")"""