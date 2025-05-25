class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
    LOGIN_URL = '/courier/login'
    CREATE_COUR_URL = '/courier'
    DELETE_COUR_URL = '/courier'
    CREATE_ORDER_URL = '/orders'
    GET_ORDERS_LIST_URL = '/orders'
    CANCEL_ORDER = '/orders/cancel'
    GET_ORDERS_BY_TRACK_URL = '/orders/track'


class DataForCreateCourier:
    CREATED_COURIER = {
    "login": "dmitriyninja",
    "password": "1234",
    "firstName": "saske"
}
class DataForCreateOrder:
    CREATE_ORDER = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}
class DataForLoginCourier:
    LOGIN_COURIER = {
    "login": "dmitriyninja",
    "password": "1234"
    }
    INVALID_LOGIN_COURIER = {
    "login": "sssaaa#@#",
    "password": "1234"
    }