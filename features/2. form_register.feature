Feature: Formulario regiter Usuario

  #HU descripcion:
  Background: Registro existoso
    Given el usuario está en la página de registro
    When ingresa las credenciales de usuario


  @formulario_usuario_register
  Scenario: formulario registro usuario nuevo
    And ingresa la informacion del usuario
    Then debe mostrar el mensaje de confirmación de registro