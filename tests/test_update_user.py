from api_methods.auth_api import AuthApi
from helpers import generate_random_string
from data import Messages
import allure


class TestUpdateUser:

    @allure.title("Проверка изменения email с авторизацией")
    def test_update_user_email_with_auth(self, registered_user):
        auth = AuthApi()
        new_value = f"{generate_random_string(10)}@yandex.ru"
        new_data = {"email": new_value}

        response = auth.patch_user_data_with_auth(registered_user["access_token"], new_data)
        body = response.json()
        assert response.status_code == 200
        assert body["success"] is True
        assert body["user"]["email"] == new_value

    @allure.title("Проверка изменения имени с авторизацией")
    def test_update_user_name_with_auth(self, registered_user):
        auth = AuthApi()
        new_value = generate_random_string(10)
        new_data = {"name": new_value}

        response = auth.patch_user_data_with_auth(registered_user["access_token"], new_data)
        body = response.json()
        assert response.status_code == 200
        assert body["success"] is True
        assert body["user"]["name"] == new_value

    @allure.title("Проверка изменения пароля с авторизацией")
    def test_update_user_password_with_auth(self, registered_user):
        auth = AuthApi()
        new_value = generate_random_string(10)
        new_data = {"password": new_value}

        response = auth.patch_user_data_with_auth(registered_user["access_token"], new_data)
        body = response.json()
        assert response.status_code == 200
        assert body["success"] is True

    @allure.title("Проверка изменения данных пользователя без авторизации")
    def test_update_user_without_auth(self, registered_user):
        auth = AuthApi()
        new_data = {"name": generate_random_string(10)}
        response = auth.patch_user_data_without_auth(new_data)
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == Messages.SHOULD_BE_AUTHORISED
