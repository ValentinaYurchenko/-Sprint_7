from faker import Faker
import requests
from helpers.endpoints import Endpoints
from helpers.urls import Urls
import allure


class DataCreateCourier:
    @staticmethod
    @allure.step("Подготовка данных для создания курьера")
    def generate_data_to_create_a_courier():
        fake = Faker('ru_RU')
        login = fake.user_name()
        password = fake.password()
        first_name = fake.first_name()
        data = {
            'login': login,
            'firstname': first_name,
            'password': password
        }

        return data

    @staticmethod
    @allure.step("Подготовка данных для создания курьера без логина")
    def generate_data_to_create_courier_without_login():
        fake = Faker('ru_RU')
        password = fake.password()
        first_name = fake.first_name()
        data = {
            'login': "",
            'firstname': first_name,
            'password': password
        }

        return data

    @staticmethod
    @allure.step("Подготовка данных для создания курьера без пароля")
    def generate_data_to_create_courier_without_password():
        fake = Faker('ru_RU')
        login = fake.user_name()
        first_name = fake.first_name()
        data = {
            'login': login,
            'firstname': first_name,
            'password': ""
        }

        return data

    @staticmethod
    @allure.step("Получение данных о несуществующем курьере")
    def generate_null_data_for_courier():
        data = {
            'login': 'test',
            'password': 'test'
        }

        return data


class CourierData:
    valid_login_data = DataCreateCourier.generate_data_to_create_a_courier()
    no_login_data = DataCreateCourier.generate_data_to_create_courier_without_login()
    no_password_data = DataCreateCourier.generate_data_to_create_courier_without_password()
    null_courier_data = DataCreateCourier.generate_null_data_for_courier()


class Courier:
    @staticmethod
    @allure.step("Сгенерировать данные, зарегистрировать курьера, получить его данные")
    def registration_and_courier_data_acquiring():
        data = DataCreateCourier.generate_data_to_create_a_courier()
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.courier_create}', data=data)
        return {"response_text": response.text, "status_code": response.status_code, "data": data}

    @staticmethod
    @allure.step("Авторизовать курьера, получить его ID")
    def login_and_retrieve_courier_id(data):
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.courier_login}', data=data)
        return {"id": response.json()["id"], "response_text": response.text, "status_code": response.status_code}

    @staticmethod
    @allure.step("Удалить курьера")
    def delete_courier(id):
        response = requests.delete(f'{Urls.SCOOTER_URL}{Endpoints.courier_delete}{id}')
        return {'response_text': response.text, 'status_code': response.status_code}
