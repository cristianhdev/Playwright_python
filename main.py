#importamos playwright
#from playwright.sync_api import Page
#from test_page_login import testPage

# 1. ejecutar los test
# pytest

# 2. ejecurtar con interfaz
# pytest --headed

# 3. grabar los pasos
#playwright codegen https://playwright.dev/

# 4. localizadores
"""
| Método                      | ¿Qué localiza?                                                      | Ejemplo de uso                                                  |
|----------------------------|----------------------------------------------------------------------|-----------------------------------------------------------------|
| `page.get_by_role()`       | Elementos por rol ARIA (botón, enlace, etc.)                         | `page.get_by_role("button", name="Enviar").click()`             |
| `page.get_by_text()`       | Elementos por texto visible                                          | `page.get_by_text("Bienvenido").click()`                        |
| `page.get_by_label()`      | Campos de formulario por el texto del `<label>` asociado             | `page.get_by_label("Correo electrónico").fill("ej@ej.com")`     |
| `page.get_by_placeholder()`| Inputs por su atributo `placeholder`                                 | `page.get_by_placeholder("Buscar...").fill("Playwright")`       |
| `page.get_by_alt_text()`   | Imágenes o elementos con atributo `alt`                              | `page.get_by_alt_text("Logo de la empresa").click()`            |
| `page.get_by_title()`      | Elementos con atributo `title`                                       | `page.get_by_title("Tooltip explicativo").hover()`              |
| `page.get_by_test_id()`    | Elementos con atributo `data-testid` (u otro configurado)            | `page.get_by_test_id("login-button").click()`                   |
"""

# 5. prioridad de localizadores recomendados en Playwright

"""
| Prioridad | Método                     | Descripción                                         | ¿Visible para el usuario? | Ejemplo                                              |
|-----------|----------------------------|-----------------------------------------------------|----------------------------|-------------------------------------------------------|
| 🥇 1      | `get_by_role()`            | Rol ARIA + nombre accesible                         | ✅ Sí                      | `page.get_by_role("button", name="Enviar")`          |
| 🥈 2      | `get_by_label()`           | Campo asociado a `<label>`                          | ✅ Sí                      | `page.get_by_label("Correo electrónico")`            |
| 🥉 3      | `get_by_text()`            | Texto visible en el contenido del elemento          | ✅ Sí                      | `page.get_by_text("Enviar")`                         |
| 4         | `get_by_placeholder()`     | Texto de ayuda dentro del input                     | ✅ Sí                      | `page.get_by_placeholder("Buscar...")`               |
| 5         | `get_by_alt_text()`        | Texto alternativo de imágenes                       | ✅ Sí                      | `page.get_by_alt_text("Logo")`                       |
| 6         | `get_by_title()`           | Atributo `title` (tooltip o descripción)            | ⚠️ A veces                 | `page.get_by_title("Tooltip")`                       |
| 7         | `get_by_test_id()`         | Atributo como `data-testid`                         | ❌ No                      | `page.get_by_test_id("login-button")`                |
"""

"""
 playwright show-trace traces/nombre_trace.zip
 playwright show-trace reports/2026-03-15_15-31-13/traces/Registro_existoso_153124.zip  
 playwright codegen -o test_recorded.py https://www.automationexercise.com/signup
 playwright codegen -o Pages/login_page.py https://www.automationexercise.com   
"""

#Reportes behave:
"""
behave features/1. register.feature
behave --tags=@formulario_usuario_register
behave --tags=@formulario_usuario_register -f allure_behave.formatter:AllureFormatter -o allure-results
behave -f allure_behave.formatter:AllureFormatter -o reports
allure serve reports

"""


#test = testPage(page=Page)
#test.test_register()