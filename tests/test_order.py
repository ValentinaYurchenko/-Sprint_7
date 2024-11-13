import json
import allure
import pytest
import requests
from data.static_data import OrderData, ResponseData
from helpers.endpoints import Endpoints
from helpers.urls import Urls


class TestCreateOrder:
    @allure.title('Заказ с использованием корректных данных возможен')
    @allure.description('Создать заказ с любым допустимым цветом возможно, ожидается ответ - 201')
    @pytest.mark.parametrize('color', [{"color": ["BLACK"]}, {"color": ["GREY"]},
                                       {"color": ["BLACK", "GRAY"]}, {"color": [""]}])
    def test_create_order_success(self, color):
        headers = {'Content-type': 'application/json'}
        data = OrderData.data
        data.update(color)
        data_dump = json.dumps(data)
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.order_make}', headers=headers, data=data_dump)
        assert response.status_code == 201 and ResponseData.track_in_order_list in response.text
