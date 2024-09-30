import requests
import allure
from config import Config


class TestListOrders:

    @allure.title("Проверяем, что запрос возвращает список заказов")
    def test_create_order_return_track_id(self):

        response = requests.get(f"{Config.url}/orders")
        orders_list = response.json()['orders']
        print(response.status_code)
        print(response.text)
        assert response.status_code == 200 and len(orders_list) > 0
