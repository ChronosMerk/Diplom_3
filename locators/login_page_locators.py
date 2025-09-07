from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_FIELD = By.XPATH, '//label[text() = "Email"]'
    PASSWORD_FIELD = By.XPATH, '//label[text() = "Пароль"]'
    FORGOT_PASSWORD_FIELD = By.XPATH, '//a[text() = "Восстановить пароль"]'
    INPUT_BUTTON = By.XPATH, '//button[text() = "Войти"]'
