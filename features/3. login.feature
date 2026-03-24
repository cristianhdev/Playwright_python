Feature: Login Usuario

  """ HU:
  como usuario nuevo de la aplicación
  quiero poder crear una cuenta nueva
  para realizar mis compras"""

  @LoginCredencialesCorrectas
  Scenario Outline: Login con credenciales correctas
    Given el usuario está en la página de login
    When ingresa las credenciales de usuario nuevo "<email>" "<usuario>"
    Then debe mostrar en la pagina de bienvenida el usuario "<usuariologin>"

    Examples:
      | email                       | usuario      | usuariologin |
      | crishernandez10@hotmail.com | $Crusto2009$ | Crusto2009   |


  @LoginInvalidCredencial
  Scenario Outline: Login con credenciales incorrectas
    Given el usuario está en la página de login
    When ingresa las credenciales de usuario incorrecto "<email>" "<usuario>"
    Then debe mostrarse la página de inicio

    Examples:
      | email                       | usuario  |
      | crishernandez20@hotmail.com | $123456$ |

