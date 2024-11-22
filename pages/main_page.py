from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

from pages.base_page import Page

class MainPage(Page):
    # BLACK_FRIDAY_DEAL =
    CLICK_SETTING = (By.XPATH, "//div[@class='circle-gradient']")
    # CLICK_SETTING = (By.XPATH, "//div[@class='menu-button-text' and text()='Settings']")

    def click_setting_option(self):
        self.click(*self.CLICK_SETTING)
        sleep(5)


