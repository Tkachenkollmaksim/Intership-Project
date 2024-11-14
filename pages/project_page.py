from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

from pages.base_page import Page

class ProjectPage(Page):
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


    def right_page_opening(self):
        self.find_element(*self.RIGHT_PAGE)
        sleep(3)

    def input_information(self):
        name = self.find_element(*self.NAME)
        name.click()
        name.send_keys("Test")
        sleep(2)

        company = self.find_element(*self.COMPANY)
        company.click()
        company.send_keys("OpConnect")
        sleep(2)

        role = self.find_element(*self.ROLE)
        role.click()
        role.send_keys("DEV")
        sleep(2)

        age = self.find_element(*self.AGE)
        age.click()
        age.send_keys("2")
        sleep(2)

        country = self.find_element(*self.COUNTRY)
        country.click()
        country.send_keys("USA")
        sleep(2)

        name_project = self.find_element(*self.NAME_PROJECT)
        name_project.click()
        name_project.send_keys("TestOp")
        sleep(2)

        phone = self.find_element(*self.PHONE)
        phone.click()
        phone.send_keys("3603469554")
        sleep(2)

        email_input = self.find_element(*self.EMAIL_INPUT)
        email_input.click()
        email_input.send_keys("tkachenkollmaksim+1@gmail.com")
        sleep(2)

    def verify_info(self):
        self.find_element(*self.VERIFY_INFO)
        sleep(3)

    def verify_button_is_clickable(self, *locator):
        self.find_element(*self.SEND_APPLICATION_BTN)
        # self.wait.until(
        #     EC.visibility_of_element_located(self.SEND_APPLICATION_BTN),  # Do not unpack here
        #     message=f'Element by {self.SEND_APPLICATION_BTN} did not appear'
        # )

