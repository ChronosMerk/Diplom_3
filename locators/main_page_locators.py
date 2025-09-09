from selenium.webdriver.common.by import By

class MainPageLocators:
    PERSONAL_ACCOUNT_LOCATOR = By.XPATH, "//p[text()='Личный Кабинет']"
    ORDER_FEED_LOCATOR = By.XPATH, "//p[text()='Лента Заказов']"
    CONSTRUCTOR_LOCATOR = By.XPATH, "//p[text()='Конструктор']"

