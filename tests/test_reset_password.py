import allure
from pages.reset_password_page import ResetPasswordPage
from data import URL

@allure.title('Тест страницы сброса пароля')
class TestResetPassword:
    @allure.title('При заполнении Email после нажатия кнопки переход на другую страницу')
    @allure.description('Открыть страницу восстановления пароля,вписывает Email, нажать на кнопку восстановить, проверка что произошел переход на другую страницу')
    def test_password_recovery_submit_email(self, driver, auth_user):
        forgot_passwort = ResetPasswordPage(driver)
        forgot_passwort.open(URL.FORGOT_PASSWORD_PAGE)

        email = auth_user.json()['user']['email']

        forgot_passwort.input_email(email)
        forgot_passwort.click_the_restore_button_to_go_to_the_reset_password_page(URL.RESET_PASSWORD_PAGE)

        assert forgot_passwort.get_current_url() == URL.RESET_PASSWORD_PAGE

    @allure.title('Проверка функции показать/скрыть пароль и подсвечивание')
    @allure.description('Открытие страницы, пишем пароль в поле пароль, нажимает глазок в поле и проверяем что пароль отобразился и подсвечивается')
    def test_toggle_password_visibility_focus_field(self, driver, auth_user):
        reset_password = ResetPasswordPage(driver)
        reset_password.open(URL.FORGOT_PASSWORD_PAGE)

        email = auth_user.json()['user']['email']

        reset_password.input_email(email)
        reset_password.click_the_restore_button_to_go_to_the_reset_password_page(URL.RESET_PASSWORD_PAGE)

        result = reset_password.is_password_input_activate_by_click()

        assert result
