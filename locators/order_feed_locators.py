from selenium.webdriver.common.by import By


class OrderFeedLocators:
    LINK_ORDER_FEED_ACTIVE = By.XPATH, ".//a[@aria-current='page']/p[text()='Лента Заказов']"
    LINK_ORDERS = By.XPATH, "(.//a[contains(@class, 'OrderHistory_link')])"
    SECTION_ORDER_DETAILS = By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]"
    LI_ORDERS_IN_PROGRESS = By.XPATH, "(.//ul[contains(@class, 'OrderFeed_orderListReady')]/li)[1]"
    SEARCH_ORDER_LOCATOR = '//p[text()="{number}"]'
    SEARCH_ORDER_AT_WORD_LOCATOR = '//li[text()="{number}"]'
    ORDERS_GLOBAL_COUNTER = By.XPATH, "//div[@class = 'undefined mb-15']//p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large']"
    ORDERS_TODAY_COUNTER = By.XPATH, "(//p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large'])[2]"