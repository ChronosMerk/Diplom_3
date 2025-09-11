from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    LINK_PROFILE = By.XPATH, ".//a[text()='Профиль']"
    LINK_HISTORY = By.XPATH, ".//a[text()='История заказов']"
    BUTTON_LOGOUT = By.XPATH, ".//button[text()='Выход']"
    NUMBER_ORDER = By.XPATH, "//a[@class = 'OrderHistory_link__1iNby']//p[@class = 'text text_type_digits-default']"
