from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def open(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_text_from_element(self, locator):
        text = self.find_element_with_wait(locator).text
        return text

    def click_element(self, locator):
        self.find_element_with_wait(locator).click()

    def set_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def wait_for_url(self, received_url):
        self.wait.until(ec.url_contains(received_url))

    def get_current_url(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
        return self.driver.current_url

    def find_element_with_click(self, locator):
        option = WebDriverWait(self.driver, self.timeout).until(
            ec.element_to_be_clickable(locator))
        option.click()

    def wait_for_visibility(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))