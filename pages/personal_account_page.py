from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from locators.general_locators import GeneralLocators
import allure

class PersonalAccountPage(BasePage):
    @allure.step('Выход из системы')
    def logout(self):
        self.click_element(GeneralLocators.LINK_PROFILE)
        self.click_element(PersonalAccountLocators.BUTTON_LOGOUT)

    @allure.step('Клик по профилю')
    def open_profile_page(self):
        self.click_element(GeneralLocators.LINK_PROFILE)

    @allure.step('Открыть историю заказов')
    def open_history_page(self):
        self.click_element(GeneralLocators.LINK_PROFILE)
        self.click_element(PersonalAccountLocators.LINK_HISTORY)

    @allure.step('Взять id заказа')
    def get_id_order(self):
        return self.get_text_from_element(PersonalAccountLocators.NUMBER_ORDER)
