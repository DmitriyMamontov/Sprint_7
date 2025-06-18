import requests
from data import Url


class OrderMethods:
    @staticmethod
    def create_order(body):
        return requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER_URL}', json=body)

    @staticmethod
    def get_orders_list():
        return requests.get(f"{Url.BASE_URL}{Url.GET_ORDERS_LIST_URL}")

    @staticmethod
    def cancel_order(track):
        return requests.put(f"{Url.BASE_URL}{Url.CANCEL_ORDER}", json={"track": track})

    def get_order_by_track(track):
        return requests.get(f"{Url.BASE_URL}/orders/{track}")