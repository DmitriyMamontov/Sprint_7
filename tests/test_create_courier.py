import allure

class TestCourierCreation:

    @allure.title("Тест кода успешного создания курьера, все поля заполнены")
    def test_successful_creation_code(self, new_courier_data, courier_api):
        response = courier_api.create_courier(new_courier_data)
        with allure.step("Проверка статус кода"):
            assert response.status_code == 201
        with allure.step("Проверка сообщения в ответе"):
            assert response.json()["ok"] is True

    @allure.title("Тест кода ошибки при создании дубликата курьера")
    def test_duplicate_creation(self, registered_courier, courier_api):
        duplicate_response = courier_api.create_courier(registered_courier)
        with allure.step("Проверка статус кода"):
            assert duplicate_response.status_code == 409
        with allure.step("Проверка сообщения в ответе"):
            assert duplicate_response.json()["message"] == "Этот логин уже используется. Попробуйте другой."


    @allure.title("Тест ошибки создания курьера, с пустым полем login")
    def test_error_create_courier_empty_login(self, new_courier_data, courier_api):
        invalid_login = new_courier_data.copy()
        del invalid_login["login"]
        response = courier_api.create_courier(invalid_login)
        with allure.step("Проверка статус кода"):
            assert response.status_code == 400
        with allure.step("Проверка сообщения в ответе"):
            assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Тест успешного создания курьера, с пустым полем firstName")
    def test_create_courier_empty_firstname(self, new_courier_data, courier_api):
        invalid_firstname = new_courier_data.copy()
        del invalid_firstname["firstName"]
        response = courier_api.create_courier(invalid_firstname)
        with allure.step("Проверка статус кода"):
            assert response.status_code == 201
        with allure.step("Проверка сообщения в ответе"):
            assert response.json()["ok"] is True


    @allure.title("Тест ошибки создания курьера, с пустым полем password")
    def test_error_create_courier_empty_password(self, new_courier_data, courier_api):
        invalid_password = new_courier_data.copy()
        del invalid_password["password"]
        response = courier_api.create_courier(invalid_password)
        with allure.step("Проверка статус кода"):
            assert response.status_code == 400
        with allure.step("Проверка сообщения в ответе"):
            assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Тест ошибки создания курьера, с пустыми полями login и password")
    def test_error_create_courier_empty_password_login(self, new_courier_data, courier_api):
        invalid_password_login = new_courier_data.copy()
        del invalid_password_login["password"]
        del invalid_password_login["login"]
        response = courier_api.create_courier(invalid_password_login)
        with allure.step("Проверка статус кода"):
            assert response.status_code == 400
        with allure.step("Проверка сообщения в ответе"):
            assert response.json()["message"] == "Недостаточно данных для создания учетной записи"