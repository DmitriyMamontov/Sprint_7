import pytest
from faker import Faker
from generators import *
from courier_methods import CourierMethods
from order_methods import OrderMethods

fake = Faker()
created_couriers = []


@pytest.fixture(scope="session")
def courier_api():
    return CourierMethods()

@pytest.fixture
def order_api():
    return OrderMethods()

@pytest.fixture
def new_courier_data():
    """Генерирует новые данные для создания курьера"""
    return generate_new_courier()

@pytest.fixture
def new_order_data():
    """Генерирует новые данные для создания заказа"""
    return generate_new_order()

@pytest.fixture
def registered_courier(courier_api, cleanup_registered_couriers):
    data = generate_new_courier()
    create_response = courier_api.create_courier(data)
    login_response = courier_api.login_courier(data)

    courier_id = login_response.json().get("id")
    courier_info = {
        "login": data["login"],
        "password": data["password"],
        "id": courier_id
    }

    cleanup_registered_couriers.append(courier_info)
    yield courier_info
@pytest.fixture
def order_data():
    created_tracks = []

    def create(color=None):
        data = generate_new_order()
        if color is not None:
            data["color"] = color
        response = OrderMethods.create_order(data)
        track = response.json().get("track")
        created_tracks.append(track)
        return response
    yield create
    for track in created_tracks:
        OrderMethods.cancel_order(track)


@pytest.fixture(scope="session", autouse=True)
def cleanup_registered_couriers(courier_api):
    created = []
    yield created

    for courier in created:
        if courier.get("id"):
            courier_api.delete_courier_by_id(courier["id"])