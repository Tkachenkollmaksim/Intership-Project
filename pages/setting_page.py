from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

from pages.base_page import Page

class SettingPage(Page):
    CLICK_PROJECT = (By.XPATH, "//div[@class='setting-text' and text()='Add a project']")


    def click_add_project(self):
        self.click(*self.CLICK_PROJECT)
        sleep(3)
