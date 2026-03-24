from behave import when,then,given
from Pages.register_page import RegisterPage
from utils.step import step

@step("Abrir Url")
@given(u'el usuario está en la página de registro')
def step_navigate_to(context):
    context.register_page =  RegisterPage(context.page)
    context.register_page.navidate()

    #Validamos si la pagina contiene el titulo "Automation Exercise"
    context.register_page.validate_title_page()

@when(u'ingresa las credenciales de usuario')
def step_fill_form_register(context):

    #Ingresamos información en el formulario.
    context.register_page.form_regiter_fill()


@then(u'debe mostrarse la página de registro')
def step_validate_page_register(context):
    context.register_page.validate_title_register()
