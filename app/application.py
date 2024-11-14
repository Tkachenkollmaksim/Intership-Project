from pages.base_page import Page
from pages.main_page import MainPage
from pages.log_in import LogIn
from pages.project_page import ProjectPage
from pages.setting_page import SettingPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.log_in = LogIn(driver)
        self.project_page = ProjectPage(driver)
        self.setting_page = SettingPage(driver)

