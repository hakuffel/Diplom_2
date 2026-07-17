import requests
from data import Endpoints
import allure


class IngredientsApi:
    @allure.step("Получить список ингредиентов")
    def get_ingredients(self):
        response = requests.get(Endpoints.BASE_URL + Endpoints.INGREDIENTS_ENDPOINT)
        return response
