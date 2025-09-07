import allure
from pages.login_page import LoginPage
from data import URL

@allure.title('Тестовые сценарии страницы восстановления пароля')
class TestForgotPassword:
    @allure.title('Открыть страницу логина, перейти на страницу восстановления пароля')
    @allure.description('Открыть страницу логина, нажать на кнопку восстановить пароль, проверить переход страницы')
    def test_navigate_to_password_recovery_page(self, driver):
        forgot_passwort = LoginPage(driver)
        forgot_passwort.open(URL.LOGIN_PAGE)
        forgot_passwort.forgot_password_page()

        assert forgot_passwort.get_current_url() == URL.FORGOT_PASSWORD_PAGE
