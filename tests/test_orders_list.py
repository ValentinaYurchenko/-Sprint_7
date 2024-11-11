import allure
import requests
from helpers.endpoints import Endpoints
from helpers.urls import Urls
from data.static_data import ResponseData


class TestOrderList:
    @allure.title('Получить список заказов')
    @allure.description('Запрос списка заказов')
    def test_get_list_of_orders(self):
        response = requests.get(f'{Urls.SCOOTER_URL}{Endpoints.order_list}')
        assert response.status_code == 200
        assert ResponseData.track_in_order_list in response.text
