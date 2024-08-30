Feature: Valid Login
  Scenario: Login with valid username and password
    Given the browser is launched
    When the user enters a valid username and password
    And the user clicks the login button
    Then the user should be successfully logged in