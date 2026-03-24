from behave import given,when,then
from Pages.login_page import LoginPage

@given(u'el usuario está en la página de login')
def step_login_page(context):
    context.login_page = LoginPage(context.page)
    context.login_page.navigate()

@when(u'ingresa las credenciales de usuario incorrecto "{email}" "{usuario}"')
def step_form_login(context,email,usuario):
    context.login_page.form_login_fill(email,usuario)
    #context.page.pause()

@then(u'debe mostrarse la página de inicio')
def step_validate_home(context):
    context.login_page.validate_form_login_fail()

@when(u'ingresa las credenciales de usuario nuevo "{email}" "{usuario}"')
def step_login_success(context,email,usuario):
    context.login_page.form_login_fill(email,usuario)

@then(u'debe mostrar en la pagina de bienvenida el usuario "{usuariologin}"')
def step_validate_title_login(context,usuariologin):
    context.login_page.validate_form_login_success(usuariologin)