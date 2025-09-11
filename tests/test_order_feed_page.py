import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage
from data import URL

@allure.title('Тестовые сценарии ленты заказов')
class TestOrderFeedPage:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('Открыть страницу ленту заказов, нажать на заказ и проверить что отобразились детали заказа')
    def test_click_order_opens_details_modal(self, driver):
        ofp = OrderFeedPage(driver)
        ofp.open(URL.ORDER_FEED_PAGE)
        ofp.click_random_order()
        order_feed_page = ofp.is_details_popup_displayed()

        assert order_feed_page

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Создать юзера, за логиться, создать заказ, взять номер заказа в «История заказов», найти заказ в «Лента заказов»')
    def test_user_orders_history_visible_in_feed(self,driver, create_user):
        user = create_user()['payload']
        login = LoginPage(driver)
        login.open(URL.LOGIN_PAGE)
        login.auth_user_page(user)

        mp = MainPage(driver)
        mp.create_order()

        pap = PersonalAccountPage(driver)
        pap.open(URL.BASE_URL)
        pap.open_history_page()
        number_order = pap.get_id_order()

        main = MainPage(driver)
        main.open_page_order_feed()

        ofp = OrderFeedPage(driver)
        assert ofp.search_order(number_order)

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.description('Создать юзера, записать число заказов, создать новый заказ, убедиться что счетчик увеличился')
    def test_create_order_increments_total_done_counter(self, driver, create_user):
        user = create_user()['payload']
        ofp = OrderFeedPage(driver)
        ofp.open(URL.ORDER_FEED_PAGE)
        number_order_global = ofp.get_completed_for_all_time()

        login = LoginPage(driver)
        login.open(URL.LOGIN_PAGE)
        login.auth_user_page(user)

        mp = MainPage(driver)
        mp.create_order()

        ofp.open(URL.ORDER_FEED_PAGE)
        number_order_global_after = ofp.get_completed_for_all_time()

        assert number_order_global < number_order_global_after

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description('Создать юзера, записать число заказов за сегодня, создать новый заказ, убедиться что счетчик увеличился')
    def test_create_order_increments_today_done_counter(self, driver, create_user):
        user = create_user()['payload']
        ofp = OrderFeedPage(driver)
        ofp.open(URL.ORDER_FEED_PAGE)
        number_order_today = ofp.get_completed_today()

        login = LoginPage(driver)
        login.open(URL.LOGIN_PAGE)
        login.auth_user_page(user)

        mp = MainPage(driver)
        mp.create_order()

        ofp.open(URL.ORDER_FEED_PAGE)
        number_order_today_after = ofp.get_completed_today()

        assert number_order_today < number_order_today_after
