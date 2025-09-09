import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step('Переход на главную страницу конструктора')
    def open_page_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_LOCATOR)

    @allure.step('Переход на страницу ленты заказа')
    def open_page_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_LOCATOR)
