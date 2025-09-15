from selenium.webdriver.common.by import By

class MainPageLocators:
    PERSONAL_ACCOUNT_LOCATOR = By.XPATH, "//p[text()='Личный Кабинет']"
    ORDER_FEED_LOCATOR = By.XPATH, "//p[text()='Лента Заказов']"
    CONSTRUCTOR_LOCATOR = By.XPATH, "//p[text()='Конструктор']"
    INGREDIENT_LOCATOR = By.XPATH, './/img[@alt="Флюоресцентная булка R2-D3"]'
    DETAILS_INGREDIENT_LOCATOR = By.XPATH, "//h2[text()='Детали ингредиента']"
    DETAILS_INGREDIENT_CLOSE_LOCATOR = By.XPATH, ".//section[@class = 'Modal_modal__P3_V5']//h2[text()='Детали ингредиента']"
    CLOSE_MODAL_ORDER = By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//button"
    INPUT_BUN = By.XPATH, "(//a[@class = 'BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8'])[1]"
    SECTION_ORDER = By.XPATH, '//section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]'
    COUNTER_BUN = By.XPATH, "(//a[@class = 'BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8'])[1]//p[@class = 'counter_counter__num__3nue1']"
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text() = "Оформить заказ"]'
    ORDER_LOCATOR = By.XPATH, "//p[text()= 'идентификатор заказа']"
    NUMBER_CREATE_ORDER_LOCATOR = By.XPATH, "//h2[@class = 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"

