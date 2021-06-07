from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from ui.locators.pages_locators import BasesPageLocators

CLICK_RETRY = 3
BASE_TIMEOUT = 5


class BasePage:

    locators = BasesPageLocators

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=BASE_TIMEOUT):
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=BASE_TIMEOUT):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click_on_element(self, locator, timeout=BASE_TIMEOUT):
        for i in range(CLICK_RETRY):
            try:
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def send_keys_to_input(self, input_locator, query, timeout=BASE_TIMEOUT):
        element = self.wait(timeout=timeout).until(EC.element_to_be_clickable(input_locator))
        element.clear()
        element.send_keys(query)
        return

    def scroll_to_elem(self, locator):
        where_to_scroll = self.find(locator)
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", where_to_scroll)
