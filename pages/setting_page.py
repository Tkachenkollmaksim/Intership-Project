from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

from pages.base_page import Page

class SettingPage(Page):
    # CLICK_PROJECT = (By.XPATH, "//a[@href='/add-a-project']")
    CLICK_PROJECT = (By.XPATH, "//a[@href='/add-a-project' and @class='page-button-menu w-inline-block']")


    def click_add_project(self):
        self.wait_to_be_clickable_click(*self.CLICK_PROJECT)
        sleep(3)
