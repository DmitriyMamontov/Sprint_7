import allure


@allure.feature("Получение списка заказов")
class TestGetOrdersList:

    @allure.title("Проверка, что сервер возвращает список заказов")
    def test_get_orders_list_returns_array(self, order_api):
        with allure.step("Отправляем запрос на получение списка заказов"):
            response = order_api.get_orders_list()
        with allure.step("Проверка статус кода"):
            assert response.status_code == 200
        with allure.step("Проверка, что в теле ответа есть список заказов"):
            json_response = response.json()
            assert isinstance(json_response, dict)
        with allure.step("Проверка, что в теле ответа есть ключ orders с массивом"):
            assert "orders" in json_response
            assert isinstance(json_response["orders"], list)