from selenium.webdriver.common.by import By

class ResetPasswordLocators:
    BUTTON_SAFE = By.XPATH, './/button[text()="Сохранить"]'
    SHOW_HIDE_PASSWORD = By.XPATH, './/div[contains(@class, "input__icon input__icon-action")]'
    INPUT_ACTIVE_FIELD_PASSWORD = By.XPATH, '//div[contains(@class, "input_status_active")]'