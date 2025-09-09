import allure
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


