from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.general_locators import GeneralLocators

class BasePage:
    def __init__(self, driver, timeout=15):
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
        try:
            #я не знаю как это работает, но без этого firefox не проходит тест
            WebDriverWait(self.driver, 3).until_not(
                ec.presence_of_element_located(GeneralLocators.MODAL_OVERLAY)
            )
        except TimeoutException:
            pass

        element = self.wait.until(ec.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        element.click()

    def set_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def wait_for_url(self, received_url):
        self.wait.until(ec.url_contains(received_url))

    def get_current_url(self, expected_part=None, wait_for_element=None):
        if expected_part:
            WebDriverWait(self.driver, self.timeout).until(
                lambda d: expected_part in d.current_url
            )
        elif wait_for_element:
            WebDriverWait(self.driver, self.timeout).until(
                ec.presence_of_element_located(wait_for_element)
            )
        else:
            WebDriverWait(self.driver, self.timeout).until(
                lambda d: d.current_url != ""
            )

        return self.driver.current_url

    def wait_for_visibility(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))