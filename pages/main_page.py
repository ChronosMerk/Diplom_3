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

    @allure.step('Проверка модального окна на отображение')
    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_LOCATOR)
        if self.wait_for_visibility(MainPageLocators.DETAILS_INGREDIENT_LOCATOR):
            return True
        return False

    @allure.step('Закрытие модального окна')
    def close_ingredient_model_window(self):
        self.click_ingredient()
        self.click_element(MainPageLocators.CLOSE_MODAL_ORDER)

        if self.wait_for_visibility(MainPageLocators.DETAILS_INGREDIENT_CLOSE_LOCATOR):
            return True
        return False

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient(self):
        counter_ingredient = self.get_text_from_element(MainPageLocators.COUNTER_BUN)
        self.drag_and_drop_smart(MainPageLocators.INPUT_BUN, MainPageLocators.SECTION_ORDER)
        counter_ingredient_add = self.get_text_from_element(MainPageLocators.COUNTER_BUN)

        if counter_ingredient and counter_ingredient_add:
            return int(counter_ingredient_add) - int(counter_ingredient)
        else:
            raise AssertionError

    @allure.step('Оформление заказа')
    def create_order(self):
        self.add_ingredient()
        self.click_element(MainPageLocators.CREATE_ORDER_BUTTON)
        self.wait_for_visibility(MainPageLocators.ORDER_LOCATOR)
        return True