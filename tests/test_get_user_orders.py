from api_methods.orders_api import OrdersApi
from data import Messages
import allure


class TestGetUserOrders:
    @allure.title("Проверка получения заказов авторизованным пользователем")
    def test_get_orders_authorized(self, registered_user, valid_ingredients):
        orders = OrdersApi()
        orders.post_order_with_auth(registered_user["access_token"], valid_ingredients)
        response = orders.get_user_orders(registered_user["access_token"])
        body = response.json()
        assert response.status_code == 200
        assert body["success"] is True
        assert "orders" in body
        assert "total" in body
        assert "totalToday" in body

    @allure.title("Проверка получения заказов неавторизованным пользователем")
    def test_get_orders_unauthorized(self):
        orders = OrdersApi()
        response = orders.get_user_orders()
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == Messages.SHOULD_BE_AUTHORISED
