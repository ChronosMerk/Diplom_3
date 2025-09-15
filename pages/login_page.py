import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    @allure.step('Переход на страницу восстановление пароля')
    def forgot_password_page(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_FIELD)

    @allure.step('Авторизация пользователя')
    def auth_user_page(self, user):
        self.set_text_to_element(LoginPageLocators.EMAIL_FIELD, user['email'])
        self.set_text_to_element(LoginPageLocators.PASSWORD_FIELD, user['password'])
        self.click_element(LoginPageLocators.INPUT_BUTTON)
