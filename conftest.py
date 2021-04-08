from selenium import webdriver
import pytest
from data_type.data import MAIN_PAGE_URL


@pytest.fixture(scope="session")
def chrome_drv():
    print("\nstart chrome browser for test..")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(MAIN_PAGE_URL)
    yield driver
    print("\nquit browser..")
    driver.quit()
    return driver





