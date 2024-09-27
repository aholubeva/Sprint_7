import requests
import pytest
import allure


class TestCreateOrder:

    @pytest.mark.parametrize(
        "payload_data",
        [
            {"firstName": "test", "lastName": "test", "address": "Konoha", "metroStation": 7, "phone": "+78003553530", "rentTime": 3, "deliveryDate": "2024-10-06", "comment": "Saske", "color": ["BLACK"]},
            {"firstName": "test", "lastName": "test", "address": "Konoha", "metroStation": 7, "phone": "+78003553530", "rentTime": 3, "deliveryDate": "2024-10-06", "comment": "Saske", "color": ["GREY"]},
            {"firstName": "test", "lastName": "test", "address": "Konoha", "metroStation": 7, "phone": "+78003553530", "rentTime": 3, "deliveryDate": "2024-10-06", "comment": "Saske", "color": ["BLACK", "GREY"]},
            {"firstName": "test", "lastName": "test", "address": "Konoha", "metroStation": 7, "phone": "+78003553530", "rentTime": 3, "deliveryDate": "2024-10-06", "comment": "Saske", "color": [""]}

        ]
    )
    @allure.title("Проверяем создание заказа с разными опциями поля color, запрос возвращает track_id")
    def test_create_order_return_track_id(self, payload_data):

        payload = payload_data
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=payload)
        track_id = response.json()['track']
        assert response.status_code == 201 and response.json()['track'] == track_id
