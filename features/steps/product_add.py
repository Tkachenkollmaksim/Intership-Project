from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CLICK_SETTING = (By.XPATH, "//div[@class='menu-button-text' and text()='Settings']")
EMAIL = (By.ID, "email-2")
PASSWORD = (By.ID, 'field')
CONTINUE = (By.CSS_SELECTOR, "a.login-button[wized='loginButton']")
CLICK_PROJECT = (By.XPATH, "//div[@class='setting-text' and text()='Add a project']")
RIGHT_PAGE = (By.XPATH, "//div[@class='text-img-block']")
NAME = (By.CSS_SELECTOR, "input.input.book.w-input[name='Your-name']")
COMPANY = (By.CSS_SELECTOR, "input.input.book.w-input[name='Your-company-name']")
ROLE = (By.CSS_SELECTOR, "input.input.book.w-input[name='Role']")
AGE = (By.CSS_SELECTOR, "input.input.book.w-input[name='Age-of-the-company']")
COUNTRY = (By.CSS_SELECTOR, "input.input.book.w-input[name='Country']")
NAME_PROJECT = (By.CSS_SELECTOR, "input.input.book.w-input[name='Name-project']")
PHONE = (By.CSS_SELECTOR, "input.input.book.w-input[name='Phone']")
EMAIL_INPUT = (By.CSS_SELECTOR, "input.input.book.w-input[name='Email-add-project']")
VERIFY_INFO = (By.ID, "wf-form-Add-a-project")
SEND_APPLICATION_BTN = (By.XPATH, '//input[@type="submit" and @value="Send an application"]')


@given('Open the main page')
def open_reelly(context):
    context.driver.get('https://soft.reelly.io/')
    sleep(5)

@when('Log in to the page')
def log_in(context):

    email_field = context.driver.find_element(*EMAIL)
    email_field.click()
    email_field.send_keys("Tkachenkollmaksim@gmail.com")
    sleep(7)

    password_field = context.driver.find_element(*PASSWORD)
    password_field.click()
    password_field.send_keys("Borshch.001")
    sleep(5)


    context.driver.find_element(*CONTINUE).click()
    sleep(7)

@when('Click on settings option')
def click_setting_option(context):
    context.driver.find_element(*CLICK_SETTING).click()
    sleep(5)


@then('Click on Add a project')
def click_add_project(context):
    context.driver.find_element(*CLICK_PROJECT).click()
    sleep(5)


@then('Verify the right page opens')
def right_page_opening(context):
    context.driver.find_element(*RIGHT_PAGE)
    sleep(5)


@then('Add some test information to the input fields')
def input_information(context):

    name = context.driver.find_element(*NAME)
    name.click()
    name.send_keys("Test")
    sleep(2)

    company = context.driver.find_element(*COMPANY)
    company.click()
    company.send_keys("OpConnect")
    sleep(2)

    role = context.driver.find_element(*ROLE)
    role.click()
    role.send_keys("DEV")
    sleep(2)

    age = context.driver.find_element(*AGE)
    age.click()
    age.send_keys("2")
    sleep(2)

    country = context.driver.find_element(*COUNTRY)
    country.click()
    country.send_keys("USA")
    sleep(2)

    name_project = context.driver.find_element(*NAME_PROJECT)
    name_project.click()
    name_project.send_keys("TestOp")
    sleep(2)

    phone = context.driver.find_element(*PHONE)
    phone.click()
    phone.send_keys("3603469554")
    sleep(2)

    email_input = context.driver.find_element(*EMAIL_INPUT)
    email_input.click()
    email_input.send_keys("tkachenkollmaksim+1@gmail.com")
    sleep(2)


@then('Verify the right information is present in the input fields')
def verify_info(context):
    context.driver.find_element(*VERIFY_INFO)
    sleep(5)


@then('Verify “Send an application” button is available and clickable')
def verify_button_is_clickable(context,):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(SEND_APPLICATION_BTN)
    )
    sleep(5)




