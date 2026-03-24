from behave.api.pending_step import StepNotImplementedError
from behave import given,then,when
from Pages.form_register_page import FormRegisterPage


@when(u'ingresa la informacion del usuario')
def step_fill_form_page_register(context):

    context.form_register_page = FormRegisterPage(context.page)
    context.form_register_page.fill_form_register_form()
    context.page.pause()
    context.form_register_page.validate_page_form()



@then(u'debe mostrar el mensaje de confirmación de registro')
def step_validate_menssage_succes_register(context):
    context.form_register_page.validate_confirm_account()
    ##context.page.pause()
