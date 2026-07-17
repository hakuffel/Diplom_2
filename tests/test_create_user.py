from api_methods.auth_api import AuthApi
from data import Messages
import allure


class TestCreateUser:
    @allure.title("Проверка на успешное создание уникального пользователя")
    def test_success_create_user(self, create_user_data):
        auth = AuthApi()
        response = auth.post_create_user(create_user_data)
        body = response.json()
        assert response.status_code == 200
        assert body["success"] is True
        assert body["user"]["email"] == create_user_data["email"]
        assert body["user"]["name"] == create_user_data["name"]
        assert "accessToken" in body
        assert "refreshToken" in body

    @allure.title("Проверка создания пользователя, который уже зарегистрирован")
    def test_create_already_exists_user(self, create_user_data):
        auth = AuthApi()
        response = auth.post_already_exists_user(create_user_data)
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == Messages.USER_ALREADY_EXISTS

    @allure.title("Проверка создания пользователя без обязательного поля name")
    def test_create_user_without_required_field(self, create_user_data):
        auth = AuthApi()
        response = auth.post_user_without_required_field(create_user_data)
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == Messages.REQUIRED_FIELDS_MISSING
