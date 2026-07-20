import pytest
from helpers import generate_data_for_user
from api_methods.auth_api import AuthApi
from api_methods.ingredients_api import IngredientsApi


@pytest.fixture
def create_user_data():
    user_data = generate_data_for_user()
    auth = AuthApi()
    yield user_data
    access_token = auth.get_access_token(user_data)
    if access_token:
        auth.delete_user(access_token)


@pytest.fixture
def registered_user(create_user_data):
    auth = AuthApi()
    response = auth.post_create_user(create_user_data)
    access_token = response.json()["accessToken"]
    return {"user_data": create_user_data, "access_token": access_token}


@pytest.fixture
def valid_ingredients():
    ingredients = IngredientsApi()
    response = ingredients.get_ingredients()
    ingredient_ids = [item["_id"] for item in response.json()["data"][:2]]
    return ingredient_ids
