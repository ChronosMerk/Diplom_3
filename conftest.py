from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from api_methods.user_methods import UserMethods
from data import URL
import pytest
import allure
import helpers


@allure.step('Фикстура: инициализация драйвера браузера')
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    elif request.param == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unknown browser: {request.param}")

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def user_methods():
    user_url = f'{URL.BASE_URL_API}'
    user_methods = UserMethods(user_url)
    return user_methods

@allure.step('Фиктсура создание нового пользователя')
@pytest.fixture
def create_user(user_methods):
    users_to_delete = []

    def _create_user(email=None, password=None, name=None):
        payload = helpers.register_new_user()
        if email:    payload["email"] = email
        if password: payload["password"] = password
        if name:     payload["name"] = name

        resp = user_methods.registration_user(payload)
        users_to_delete.append({"email": payload["email"], "password": payload["password"]})

        return {"response": resp, "payload": payload}

    yield _create_user

    for creds in users_to_delete:
        login_resp = user_methods.auth_user({"email": creds["email"], "password": creds["password"]})
        if login_resp.status_code == 200:
            token = login_resp.json()["accessToken"]
            user_methods.delete_user(token)

@pytest.fixture
def auth_user(create_user, user_methods):
    user = create_user()["payload"]
    login = user_methods.auth_user(user)
    return login

