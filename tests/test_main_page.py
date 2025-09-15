import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data import URL

@allure.title('Тестовые сценарии главной страницы')
class TestMainPage:

    @allure.title('Проверка перехода на главную страницу (конструктор) с ленты заказов по кнопке')
    @allure.description('Открыть ленты заказов, перейти в конструктор, проверить загрузку главной страницы')
    def test_navigate_to_constructor_success(self, driver):
        mp = MainPage(driver)
        mp.open(URL.ORDER_FEED_PAGE)
        mp.open_page_constructor()

        assert mp.get_current_url() == URL.BASE_URL

    @allure.title('Проверка перехода на ленту заказов с главной странице по кнопке')
    @allure.description('Открыть главную страницу, перейти в ленту заказов, проверить загрузку ленту заказов')
    def test_navigate_to_order_feed_success(self, driver):
        mp = MainPage(driver)
        mp.open(URL.BASE_URL)
        mp.open_page_order_feed()

        assert mp.get_current_url() == URL.ORDER_FEED_PAGE

    @allure.title('Проверка открытие модального окна с ингредиентом')
    @allure.description('Открыть главную страницу, нажать на ингредиент, проверить загрузку модального окна')
    def test_click_ingredient_opens_modal(self, driver):
        mp = MainPage(driver)
        mp.open(URL.BASE_URL)
        response = mp.click_ingredient()

        assert response

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    @allure.description('Открыть главную страницу, нажать на ингредиент, дождаться загрузки модального окна, закрыть модальное окно')
    def test_click_ingredient_opens_modal_and_close(self, driver):
        mp = MainPage(driver)
        mp.open(URL.BASE_URL)
        response = mp.close_ingredient_model_window()

        assert response

    @allure.title('При добавление ингредиента увеличивается счетчик(каунтер) ингредиента')
    @allure.description('Открыть главную страницу, перемести ингредиент в конструктор, проверить что каунтер обновился')
    def test_add_ingredient_increments_counter(self, driver):
        mp = MainPage(driver)
        mp.open(URL.BASE_URL)
        response = mp.add_ingredient()

        assert response == 2

    @allure.title('Залогиненный пользователь может оформить заказ')
    @allure.description('Авторизоваться, открыть главную страницу, перемести ингредиент в конструктор, проверить что каунтер обновился, нажать кнопку Оформить заказ, проверить оформление')
    def test_logged_in_user_can_create_order(self, driver, create_user):
        user = create_user()['payload']
        login = LoginPage(driver)
        login.open(URL.LOGIN_PAGE)
        login.auth_user_page(user)

        mp = MainPage(driver)
        r = mp.create_order()

        assert r