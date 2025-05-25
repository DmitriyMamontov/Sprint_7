import allure
from data import *


class TestCourierLogin:

    @allure.title("Успешный вход с корректными данными")
    def test_login_success(self, registered_courier, courier_api):
        login_data = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }
        response = courier_api.login_courier(login_data)
        with allure.step("Проверка статус кода"):
            assert response.status_code == 200
        json_response = response.json()
        with allure.step("Проверка id в ответе"):
            assert "id" in json_response

    @allure.title("Ошибка при входе с несуществующими данными")
    def test_error_login_with_not_registered_courier(self, courier_api):
        login_data = DataForLoginCourier.INVALID_LOGIN_COURIER
        response = courier_api.login_courier(login_data)
        with allure.step("Проверка статус кода"):
            assert response.status_code == 404
        with allure.step("Проверка сообщения в ответе"):
            assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Ошибка при входе с пустым полем пароль")
    def test_error_login_empty_password(self, registered_courier, courier_api):
        login_data = {
            "login": registered_courier["login"],
            "password": ""
        }
        response = courier_api.login_courier(login_data)
        with allure.step("Проверка статус кода"):
            assert response.status_code == 400
        with allure.step("Проверка сообщения в ответе"):
            assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Ошибка при входе с пустым полем логин")
    def test_error_login_empty_login(self, registered_courier, courier_api):
        login_data = {
            "login": "",
            "password": registered_courier["password"]
        }
        response = courier_api.login_courier(login_data)
        with allure.step("Проверка статус кода"):
            assert response.status_code == 400
        with allure.step("Проверка сообщения в ответе"):
            assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Ошибка при входе с пустыми полями")
    def test_error_login_empty_fields(self, registered_courier, courier_api):
        login_data = {
            "login": "",
            "password": ""
        }
        response = courier_api.login_courier(login_data)
        with allure.step("Проверка статус кода"):
            assert response.status_code == 400
        with allure.step("Проверка сообщения в ответе"):
            assert response.json()["message"] == "Недостаточно данных для входа"