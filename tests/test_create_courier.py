import requests
from helpers import register_new_courier_and_return_login_password
import pytest
import allure
from config import Config


class TestCreateCourier:

    @allure.title('Проверяем успешное создание курьера, запрос возвращает код ответа 201, ok:true')
    def test_success_create_courier_code_201(self):
        login, password, response_status_code, response_status_text = register_new_courier_and_return_login_password()
        assert response_status_code == 201 and response_status_text == '{"ok":true}'

    @allure.title('Проверяем, что нельзя создать курьера с существующим логином, запрос возвращает ошибку с кодом 409')
    def test_create_courier_with_existing_login_error_409(self):
        login, password, response_status_code, response_status_text = register_new_courier_and_return_login_password()
        payload = {
            "login": login,
            "password": password,
            "firstName": "Анастасия"
        }

        response = requests.post(f"{Config.url}/courier", data=payload)
        assert (response.status_code == 409 and response.json()['message'] == "Этот логин уже используется. Попробуйте другой.")

    @pytest.mark.parametrize(
        "payload_data",
        [
            {"login": "", "password": "password", "firstName": "Анастасия"},
            {"login": "login", "password": "", "firstName": "Анастасия"},
            {"login": "login", "password": "password", "firstName": ""}

        ]
    )
    @allure.title('Проверяем, что нельзя создать курьера с пустым логином/или паролем/или именем, запрос возвращает ошибку с кодом 400')
    def test_create_courier_with_empty_login_error_400(self, payload_data):

        payload = payload_data
        response = requests.post(f"{Config.url}/courier", data=payload)
        assert (response.status_code == 400 and response.json()['message'] == "Недостаточно данных для создания учетной записи")

