import allure
from locators.forgot_password_page_locators import ForgotPasswordLocators
from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators

class ResetPasswordPage(BasePage):
    @allure.step('Ввод адреса электронной почты')
    def input_email(self, email):
        self.set_text_to_element(ForgotPasswordLocators.EMAIL_FIELD, email)

    @allure.step('Нажатие кнопки восстановить, переход на страницу reset-password')
    def click_the_restore_button_to_go_to_the_reset_password_page(self, url):
        self.click_element(ForgotPasswordLocators.BUTTON_SUBMIT_RESTORE)
        self.wait_for_url(url)

    @allure.step('Нажатие на кнопку показать/скрыть пароль, отображается пароль и подсвечивается')
    def is_password_input_activate_by_click(self):
        self.click_element(ResetPasswordLocators.SHOW_HIDE_PASSWORD)
        result = self.wait_for_visibility(ResetPasswordLocators.INPUT_ACTIVE_FIELD_PASSWORD)
        if result:
            return True
        return False
