import requests
from data import Endpoints
import allure


class OrdersApi:
    @allure.step("Создать заказ с авторизацией")
    def post_order_with_auth(self, access_token, ingredients):
        headers = {"Authorization": access_token}
        payload = {"ingredients": ingredients}
        response = requests.post(Endpoints.BASE_URL + Endpoints.ORDERS_ENDPOINT, headers=headers, json=payload)
        return response

    @allure.step("Создать заказ без авторизации")
    def post_order_without_auth(self, ingredients):
        payload = {"ingredients": ingredients}
        response = requests.post(Endpoints.BASE_URL + Endpoints.ORDERS_ENDPOINT, json=payload)
        return response

    @allure.step("Получить заказы конкретного пользователя")
    def get_user_orders(self, access_token=None):
        headers = {"Authorization": access_token} if access_token else {}
        response = requests.get(Endpoints.BASE_URL + Endpoints.ORDERS_ENDPOINT, headers=headers)
        return response
