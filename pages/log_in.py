from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

from pages.base_page import Page


class LogIn(Page):
    EMAIL = (By.ID, "email-2")
    PASSWORD = (By.ID, 'field')
    CONTINUE = (By.CSS_SELECTOR, "a.login-button[wized='loginButton']")



    def open_log_in_page(self):
        self.open('https://soft.reelly.io/')
        sleep(7)


    def log_in(self):
        email_field = self.find_element(*self.EMAIL)
        email_field.click()
        email_field.send_keys("Tkachenkollmaksim@gmail.com")
        sleep(7)

        password_field = self.find_element(*self.PASSWORD)
        password_field.click()
        password_field.send_keys("Borshch.001")
        sleep(5)

        self.wait_to_be_clickable_click(*self.CONTINUE)
        sleep(7)