from api_methods.auth_api import AuthApi
from data import Messages
import allure


class TestLoginUser:
    @allure.title("Проверка на успешный логин под существующим пользователем")
    def test_success_login_user(self, registered_user):
        auth = AuthApi()
        response = auth.post_user_login(registered_user["user_data"])
        body = response.json()
        assert response.status_code == 200
        assert body["success"] is True
        assert body["user"]["email"] == registered_user["user_data"]["email"]
        assert "accessToken" in body
        assert "refreshToken" in body

    @allure.title("Проверка логина с неверным логином и паролем")
    def test_login_wrong_credentials(self):
        auth = AuthApi()
        response = auth.post_user_login_wrong_credentials()
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == Messages.LOGIN_INCORRECT
