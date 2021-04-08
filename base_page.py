from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver,  timeout=10):
        """

        :param driver: call website
        :param timeout: waiting
        """
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def get_element_present(self, how, what):
        """

        :param how: find method (XBy.CLASS_NAME, By.XPATH)
        :param what: what are you looking for
        :return:
        """
        try:
            object = self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return object

    def is_not_element_present(self, how, what, timeout=10):

        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False



