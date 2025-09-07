import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    @allure.step('Переход на страницу восстановление пароля')
    def forgot_password_page(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_FIELD)
