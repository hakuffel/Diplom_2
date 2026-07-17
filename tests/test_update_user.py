import pytest
from api_methods.auth_api import AuthApi
from helpers import generate_random_string
from data import Messages
import allure


class TestUpdateUser:
    @allure.title("Проверка изменения поля {field} с авторизацией")
    @pytest.mark.parametrize("field", ["email", "name", "password"])
    def test_update_user_field_with_auth(self, registered_user, field):
        auth = AuthApi()
        if field == "email":
            new_value = f"{generate_random_string(10)}@yandex.ru"
        else:
            new_value = generate_random_string(10)
        new_data = {field: new_value}

        response = auth.patch_user_data_with_auth(registered_user["access_token"], new_data)
        body = response.json()
        assert response.status_code == 200
        assert body["success"] is True
        if field != "password":
            assert body["user"][field] == new_value

    @allure.title("Проверка изменения данных пользователя без авторизации")
    def test_update_user_without_auth(self, registered_user):
        auth = AuthApi()
        new_data = {"name": generate_random_string(10)}
        response = auth.patch_user_data_without_auth(new_data)
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == Messages.SHOULD_BE_AUTHORISED
