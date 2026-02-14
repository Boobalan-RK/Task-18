Feature: Zen Portal Login

  Scenario: Successful login
    Given user launches browser
    When user enters valid username and password
    Then user should see dashboard
    And user logs out

  Scenario: Invalid login
    Given user launches browser
    When user enters invalid username and password
    Then login should fail
