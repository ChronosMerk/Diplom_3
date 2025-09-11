import allure
import random
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.common.by import By

class OrderFeedPage(BasePage):

    def _get_random_order_locator(self):
        orders_locator = OrderFeedLocators.LINK_ORDERS
        self.wait_for_visibility(orders_locator)  # Подождать появления списка заказов
        orders = self.driver.find_elements(*orders_locator)  # Получить все элементы списка заказов
        orders_count = len(orders)  #
        # Если список заказов не пустой, то выбрать случайный
        if orders_count > 0:
            index = random.randint(1, orders_count)
            random_locator = orders_locator[0], f'{orders_locator[1]}[{index}]'  # Дополнить локатор
            return random_locator
        else:
            raise AssertionError

    @allure.step('Нажатие на случайный ингредиент из списка')
    def click_random_order(self):
        locator = self._get_random_order_locator()
        self.wait_for_visibility(locator)
        self.click_element(locator)

    @allure.step('Статус проверки отображения всплывающего окна')
    def is_details_popup_displayed(self):
        try:
            self.wait_for_visibility(OrderFeedLocators.SECTION_ORDER_DETAILS)
            return True
        except:
            return False

    @allure.step('Поиск заказа в ленте заказов')
    def search_order(self, number_order):
        xpath = OrderFeedLocators.SEARCH_ORDER_LOCATOR.replace("{number}", number_order)
        self.wait_for_visibility((By.XPATH, xpath))
        return self.get_text_from_element(xpath)

    @allure.step('Получение количества заказов из поля "Выполнено за все время:"')
    def get_completed_for_all_time(self):
        return self.get_text_from_element(OrderFeedLocators.ORDERS_GLOBAL_COUNTER)

    @allure.step('Получение количества заказов из поля "Выполнено за сегодня:"')
    def get_completed_today(self):
        return self.get_text_from_element(OrderFeedLocators.ORDERS_TODAY_COUNTER)

    @allure.step('Поиск созданного заказа в поле "В работе"')
    def search_order_at_word(self, number_order):
        xpath = OrderFeedLocators.SEARCH_ORDER_AT_WORD_LOCATOR.replace("{number}", number_order)
        self.wait_for_visibility((By.XPATH, xpath))
        return self.get_text_from_element(xpath)
