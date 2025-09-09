from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_FIELD = By.NAME, "name"
    PASSWORD_FIELD = By.NAME, "Пароль"
    FORGOT_PASSWORD_FIELD = By.XPATH, '//a[text() = "Восстановить пароль"]'
    INPUT_BUTTON = By.XPATH, '//button[text() = "Войти"]'
