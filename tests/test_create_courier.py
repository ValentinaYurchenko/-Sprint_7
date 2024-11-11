import allure
import pytest
import requests
from helpers.helper_data import CourierData, Courier
from helpers.endpoints import Endpoints
from helpers.urls import Urls
from data.static_data import ResponseData


class TestCourierCreate:
    @allure.title('Создание курьера')
    @allure.description('Создать курьера, убедиться в получении положительного ответа сервера')
    def test_registration_successful(self, courier):
        courier_data = courier
        assert courier_data['status_code'] == 201
        assert ResponseData.courier_successful_response in courier_data['response_text']
        courier_login = Courier().login_and_retrieve_courier_id(courier_data["data"])
        Courier().delete_courier(courier_login["id"])

    @allure.title('Повторное использование данных для регистрации курьера')
    @allure.description('Повторное создание курьера, получение ожидаемой ошибки, удаление исходного курьера')
    def test_double_registration_failed(self, courier):
        courier_data = courier
        first_courier_id = Courier().login_and_retrieve_courier_id(courier_data["data"])
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.courier_create}', data=courier_data["data"])
        assert response.status_code == 409
        assert ResponseData.same_login in response.text
        Courier().delete_courier(first_courier_id["id"])

    @allure.title('Невозможность регистрации без логина или пароля')
    @allure.description('Создать курьера без логина или пароля и убедиться в невозможности регистрации')
    @pytest.mark.parametrize('courier_data', [CourierData.no_login_data,
                                              CourierData.no_password_data])
    def test_registration_without_params_failed(self, courier_data):
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.courier_create}', data=courier_data)
        assert response.status_code == 400
        assert ResponseData.not_enough_reg_data_response in response.text
