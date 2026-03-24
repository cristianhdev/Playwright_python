Feature:Register Usuario

  #HU descripcion:

  @RegisterUser
  Scenario: Registro existoso
    Given el usuario está en la página de registro
    When ingresa las credenciales de usuario
    Then debe mostrarse la página de registro