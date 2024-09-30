import requests
from src.helpers import register_new_courier_and_return_login_password
from src.helpers import generate_random_string
import allure
from src.config import Config

class TestLoginCourier:

    @allure.title('Проверяем успешный логин курьера, запрос возвращает код 200')
    def test_success_courier_login_status_code_200(self):
        login, password, response_status_code, response_status_text = register_new_courier_and_return_login_password()
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f"{Config.url}/courier/login", data=payload)
        assert response.status_code == 200

    @allure.title('Проверяем успешный логин курьера, запрос возвращает id курьера')
    def test_success_courier_login_return_id(self):
        login, password, response_status_code, response_status_text = register_new_courier_and_return_login_password()
        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(f"{Config.url}/courier/login", data=payload)
        courier_id = response.json()['id']
        assert response.status_code == 200 and response.json()['id'] == courier_id

    @allure.title('Проверяем, что курьер не может залогиниться с пустым логином, запрос возвращает ошибку с кодом 400')
    def test_courier_login_with_empty_login_error_400(self):
        login, password, response_status_code, response_status_text = register_new_courier_and_return_login_password()
        payload = {
            "login": "",
            "password": password
        }

        response = requests.post(f"{Config.url}/courier/login", data=payload)
        assert (response.status_code == 400 and response.json()['message'] == "Недостаточно данных для входа")

    @allure.title('Проверяем, что курьер не может залогиниться с пустым паролем, запрос возвращает ошибку с кодом 400')
    def test_courier_login_with_empty_password_error_400(self):
        login, password, response_status_code, response_status_text = register_new_courier_and_return_login_password()
        payload = {
            "login": login,
            "password": ""
        }

        response = requests.post(f"{Config.url}/courier/login", data=payload)
        assert (response.status_code == 400 and response.json()['message'] == "Недостаточно данных для входа")

    @allure.title('Проверяем, что курьер не может залогиниться с невалидным логином, запрос возвращает ошибку с кодом 404')
    def test_courier_login_with_invalid_login_error_404(self):
        login, password, response_status_code, response_status_text = register_new_courier_and_return_login_password()
        random_string = generate_random_string(10)
        payload = {
            "login": random_string,
            "password": password
        }

        response = requests.post(f"{Config.url}/courier/login", data=payload)
        assert (response.status_code == 404 and response.json()['message'] == "Учетная запись не найдена")

    @allure.title('Проверяем, что курьер не может залогиниться с невалидным паролем, запрос возвращает ошибку с кодом 404')
    def test_courier_login_with_invalid_password_error_404(self):
        login, password, response_status_code, response_status_text = register_new_courier_and_return_login_password()
        random_string = generate_random_string(10)
        payload = {
            "login": login,
            "password": random_string
        }

        response = requests.post(f"{Config.url}/courier/login", data=payload)
        assert (response.status_code == 404 and response.json()['message'] == "Учетная запись не найдена")

    @allure.title('Проверяем, что курьер не может залогиниться с невалидным логином и паролем, запрос возвращает ошибку с кодом 400')
    def test_courier_login_with_not_existing_user_error_404(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(f"{Config.url}/courier/login", data=payload)
        assert (response.status_code == 404 and response.json()['message'] == "Учетная запись не найдена")
