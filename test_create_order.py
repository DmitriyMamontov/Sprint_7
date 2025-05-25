import pytest
import allure

@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с цветом {color}")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        None  # без цвета
    ])
    def test_create_order(self, order_data, color):
        response = order_data(color=color)

        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 201
        with allure.step("Проверка track в ответе"):
            assert "track" in response.json()
