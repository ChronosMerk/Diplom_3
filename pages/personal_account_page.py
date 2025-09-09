from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from locators.general_locators import GeneralLocators
import allure

class PersonalAccountPage(BasePage):
    @allure.step('Выход из системы')
    def logout(self):
        self.click_element(GeneralLocators.LINK_PROFILE)
        self.click_element(PersonalAccountLocators.BUTTON_LOGOUT)

    def open_profile_page(self):
        self.click_element(GeneralLocators.LINK_PROFILE)

    def open_history_page(self):
        self.click_element(GeneralLocators.LINK_PROFILE)
        self.click_element(PersonalAccountLocators.LINK_HISTORY)
