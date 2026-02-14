from behave import given, when, then
from pages.login_page import LoginPage


@given("user launches browser")
def step_launch(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.load()


@when("user enters valid username and password")
def step_valid_login(context):
    context.login_page.login("dummy", "dummy")


@then("user should see dashboard")
def step_dashboard(context):
    assert context.login_page.is_login_page_loaded()


@then("user logs out")
def step_logout(context):
    context.login_page.logout()


@when("user enters invalid username and password")
def step_invalid_login(context):
    context.login_page.login("wrong", "wrong")


@then("login should fail")
def step_fail(context):
    assert context.login_page.is_login_page_loaded()
