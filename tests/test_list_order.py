import requests
import allure


class TestListOrders:

    @allure.title("Проверяем, что запрос возвращает список заказов")
    def test_create_order_return_track_id(self):

        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
        orders_list = response.json()['orders']
        print(response.status_code)
        print(response.text)
        assert response.status_code == 200 and len(orders_list) > 0
