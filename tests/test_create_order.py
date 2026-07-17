from api_methods.orders_api import OrdersApi
from data import Data, Messages
import allure


class TestCreateOrder:
    @allure.title("Проверка создания заказа с авторизацией и ингредиентами")
    def test_create_order_with_auth(self, registered_user, valid_ingredients):
        orders = OrdersApi()
        response = orders.post_order_with_auth(registered_user["access_token"], valid_ingredients)
        body = response.json()
        assert response.status_code == 200
        assert body["success"] is True
        assert "name" in body["order"] or "name" in body

    @allure.title("Проверка создания заказа без авторизации")
    def test_create_order_without_auth(self, valid_ingredients):
        orders = OrdersApi()
        response = orders.post_order_without_auth(valid_ingredients)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Проверка создания заказа без ингредиентов")
    def test_create_order_without_ingredients(self, registered_user):
        orders = OrdersApi()
        response = orders.post_order_with_auth(registered_user["access_token"], [])
        assert response.status_code == 400
        assert response.json()["success"] is False
        assert response.json()["message"] == Messages.INGREDIENT_IDS_MUST_BE_PROVIDED

    @allure.title("Проверка создания заказа с неверным хешем ингредиента")
    def test_create_order_with_invalid_ingredient_hash(self, registered_user):
        orders = OrdersApi()
        response = orders.post_order_with_auth(registered_user["access_token"], Data.invalid_ingredients)
        assert response.status_code == 400
        assert response.json()["success"] is False
