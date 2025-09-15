from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    EMAIL_FIELD = By.XPATH, './/input[@name="name"]'
    BUTTON_SUBMIT_RESTORE = By.XPATH, ".//button[text()='Восстановить']"
    TEXT_PAGE = By.XPATH, "//h2[text()='Восстановление пароля']"