import allure
from data import URL
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage

@allure.title('Тестовые сценарии страницы профиля')
class TestProfilePage:

    @allure.title('Проверка перехода на страницу профиля')
    @allure.title('Войти в аккаунт, нажать на кнопку Личный кабинет и проверить что был переход на страницу')
    def test_open_profile_page(self, driver, create_user):
        login = LoginPage(driver)
        login.open(URL.LOGIN_PAGE)

        user = create_user()['payload']
        login.auth_user_page(user)

        pa = PersonalAccountPage(driver)
        pa.open_profile_page()
        assert pa.get_current_url(expected_part="/account/profile") == URL.PROFILE_PAGE

    @allure.title('Проверка перехода в историю заказов')
    @allure.description('Создать пользователя, перейти на страницу логина, авторизоваться под созданным пользователем, перейти на страницу профиля, перейти в историю заказов')
    def test_profile_page_show_orders_history_success(self, driver, create_user):
        user = create_user()['payload']
        login = LoginPage(driver)
        login.open(URL.LOGIN_PAGE)
        login.auth_user_page(user)

        pa = PersonalAccountPage(driver)
        pa.open_history_page()

        assert pa.get_current_url() == URL.ORDER_HISTORY

    @allure.title('Проверка выхода из профиля')
    @allure.description('Создать пользователя, перейти на страницу логина, авторизоваться под созданным пользователем, перейти на страницу профиля, выйти из профиля по кнопке выхода, проверить загрузку страницы логина')
    def test_profile_page_logout_success(self, driver, create_user):
        user = create_user()['payload']
        login = LoginPage(driver)
        login.open(URL.LOGIN_PAGE)
        login.auth_user_page(user)

        pa = PersonalAccountPage(driver)
        pa.logout()

        assert pa.get_current_url(expected_part="/login") == URL.LOGIN_PAGE