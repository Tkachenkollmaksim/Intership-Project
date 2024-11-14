import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture
def driver():
    # Setup for WebDriver (using Chrome)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_example_com(driver):
    # Start test case: Open a website and check for a specific element
    driver.get("https://example.com")

    try:
        element = driver.find_element(By.ID, "element_id")  # Replace 'element_id' with the actual element ID
        assert element.is_displayed(), "Element is not visible"
    except NoSuchElementException:
        pytest.fail("Element not found")