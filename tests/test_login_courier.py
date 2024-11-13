import allure
import pytest
import requests
from helpers.helper_data import CourierData, Courier
from helpers.endpoints import Endpoints
from helpers.urls import Urls
from data.static_data import ResponseData


class TestCourierLogin:
    @allure.title('Логин с корректными данными')
    @allure.description('Логин курьера, подтверждение логина, удаление курьера')
    def test_courier_login(self, courier):
        courier_data = courier
        response = Courier().login_and_retrieve_courier_id(courier_data['data'])
        assert response['status_code'] == 200
        assert response.get('id')
        Courier().delete_courier(response["id"])

    @allure.title('Авторизация без логина или пароля невозможна')
    @allure.description('Авторизация курьера без логина или пароля, ожидается ошибка')
    @pytest.mark.parametrize('courier_data', [CourierData.no_login_data,
                                              CourierData.no_password_data])
    def test_courier_login_params_missing(self, courier_data):
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.courier_login}', data=courier_data)
        assert response.status_code == 400
        assert ResponseData.not_enough_login_data_response in response.text

    @allure.title('Авторизация с null-данными')
    @allure.description('Невозможность авторизации с null-данными')
    def test_courier_login_null_data(self):
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.courier_login}', data=CourierData.null_courier_data)
        assert response.status_code == 404
        assert ResponseData.profile_404_response in response.text
