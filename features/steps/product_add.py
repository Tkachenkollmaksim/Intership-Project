from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_log_in_page(context):
    context.app.log_in.open_log_in_page()


@when('Log in to the page')
def log_in(context):
    context.app.log_in.log_in()


@when('Click on settings option')
def click_setting_option(context):
    context.app.main_page.click_setting_option()


@then('Click on Add a project')
def click_add_project(context):
    context.app.setting_page.click_add_project()


@then('Verify the right page opens')
def right_page_opening(context):
    context.app.project_page.right_page_opening()


@then('Add some test information to the input fields')
def input_information(context):
    context.app.project_page.input_information()


@then('Verify the right information is present in the input fields')
def verify_info(context):
    context.app.project_page.verify_info()


@then('Verify “Send an application” button is available and clickable')
def verify_button_is_clickable(context,):
    context.app.project_page.verify_button_is_clickable()




