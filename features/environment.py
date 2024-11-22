from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options



from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    # """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # # # ## BROWSERSTACK ###
    # bs_user = 'maksimtkachenko_XKOec4'
    # bs_key = 'WGyzDu7xCQpSdXN5LZcY'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os": "Windows",
    #     "osVersion": "10",
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # # ## Mobile Test - Chrome Simulator ###
    # mobile_emulation = {
    #     "deviceName": "iPhone 14 Pro Max"  # Choose a mobile device
    # }
    #
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # # Initialize WebDriver with mobile emulation
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=options)

    # # ## BROWSERSTACK Mobile###
    bs_user = 'maksimtkachenko_XKOec4'
    bs_key = 'WGyzDu7xCQpSdXN5LZcY'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'platformName': 'iOS',
        "deviceName": "iPhone 14",
        "osVersion": "18",
        'browserName': 'safari',
        'sessionName': scenario_name,
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)




    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()


import logging

# Configure logging
logging.basicConfig(
    filename="test_report.log",  # The file where logs will be saved
    filemode="w",                # 'w' mode overwrites the file each run; use 'a' to append
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO           # Set the default logging level to INFO
)

# # Example logging statements
# logging.info("Starting the test suite")
#
# def log_start_test(test_name):
#     logging.info(f"Starting test: {test_name}")
#
# def log_test_step(step_description):
#     logging.info(f"Step: {step_description}")
#
# def log_test_result(test_name, status):
#     logging.info(f"Test Result for '{test_name}': {status}")
#
# def log_error(test_name, error_message):
#     logging.error(f"Error in '{test_name}': {error_message}")
