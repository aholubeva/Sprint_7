import requests
from src.helpers import register_new_courier_and_return_login_password
import pytest
import allure


class TestCreateCourier:

    @allure.title('Проверяем успешное создание курьера, запрос возвращает код ответа 201')
    def test_create_courier_status_code_201(self):
        login, password, response_status_code, response_status_text = register_new_courier_and_return_login_password()
        assert response_status_code == 201

    @allure.title('Проверяем успешное создание курьера, запрос возвращает ok:true')
    def test_create_courier_response_text(self):
        login, password, response_status_code, response_status_text = register_new_courier_and_return_login_password()
        assert response_status_text == '{"ok":true}'

    @allure.title('Проверяем, что нельзя создать курьера с существующим логином, запрос возвращает ошибку с кодом 409')
    def test_create_courier_with_existing_login_error_409(self):
        login, password, response_status_code, response_status_text = register_new_courier_and_return_login_password()
        payload = {
            "login": login,
            "password": password,
            "firstName": "Анастасия"
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert (response.status_code == 409 and response.json()['message'] == "Этот логин уже используется. Попробуйте другой.")

    @allure.title('Проверяем, что нельзя создать курьера с пустым логином, запрос возвращает ошибку с кодом 400')
    def test_create_courier_with_empty_login_error_400(self):

        payload = {
            "login": "",
            "password": "password",
            "firstName": "Анастасия"
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert (response.status_code == 400 and response.json()['message'] == "Недостаточно данных для создания учетной записи")

    @allure.title('Проверяем, что нельзя создать курьера с пустым паролем, запрос возвращает ошибку с кодом 400')
    def test_create_courier_with_empty_password_error_400(self):

        payload = {
            "login": "login",
            "password": "",
            "firstName": "Анастасия"
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert (response.status_code == 400 and response.json()['message'] == "Недостаточно данных для создания учетной записи")

    @allure.title('Проверяем, что нельзя создать курьера с именем, запрос возвращает ошибку с кодом 400')
    @pytest.mark.xfailed # можно создать курьера с пустым "firstName", что противоречит документации
    def test_create_courier_with_empty_first_name_error_400(self):

        payload = {
            "login": "login",
            "password": "password",
            "firstName": ""
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert (response.status_code == 400 and response.json()['message'] == "Недостаточно данных для создания учетной записи")
