import allure
from helpers.helper_data import Courier
from data.static_data import ResponseData


class TestDeleteCourier:
    @allure.title('Удаление курьера')
    @allure.description('Удаление курьера, ожидание подтверждения сервером')
    def test_courier_delete_success(self, courier):
        courier_id = courier
        courier_login = Courier().login_and_retrieve_courier_id(courier_id["data"])
        response = Courier().delete_courier(courier_login["id"])
        assert response["status_code"] == 200
        assert ResponseData.courier_successful_response in response['response_text']

    @allure.title('Удаление курьера с невалидным ID')
    @allure.description('Удаление курьера с несуществующим в системе ID, ожидаемый ответ - 404 Not Found')
    def test_courier_with_invalid_id_deletion_failed(self):
        invalid_id = '111111'
        response = Courier().delete_courier(invalid_id)
        assert response['status_code'] == 404
        assert ResponseData.invalid_id_response in response['response_text']

    @allure.title('Удаление курьера без ID')
    @allure.description('Удаление курьера без ID, ожидаемый ответ - 500 Internal Server Error')
    def test_delete_courier_without_id_failed(self):
        courier_id = None
        response = Courier().delete_courier(courier_id)
        assert response['status_code'] == 500
        assert ResponseData.null_id_response in response['response_text']
        