import requests
from data import Endpoints
import allure


class AuthApi:
    @allure.step("Создать пользователя")
    def post_create_user(self, user_data):
        response = requests.post(Endpoints.BASE_URL + Endpoints.REGISTER_ENDPOINT, json=user_data)
        return response

    @allure.step("Создать пользователя с данными уже существующего пользователя")
    def post_already_exists_user(self, user_data):
        self.post_create_user(user_data)
        response = self.post_create_user(user_data)
        return response

    @allure.step("Создать пользователя без обязательного поля")
    def post_user_without_required_field(self, user_data):
        payload = {
            "email": user_data["email"],
            "password": user_data["password"],
        }
        response = requests.post(Endpoints.BASE_URL + Endpoints.REGISTER_ENDPOINT, json=payload)
        return response

    @allure.step("Логин пользователя")
    def post_user_login(self, user_data):
        payload = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        response = requests.post(Endpoints.BASE_URL + Endpoints.LOGIN_ENDPOINT, json=payload)
        return response

    @allure.step("Логин пользователя с неверным логином и паролем")
    def post_user_login_wrong_credentials(self):
        payload = {
            "email": "wrongemail@yandex.ru",
            "password": "wrongpassword"
        }
        response = requests.post(Endpoints.BASE_URL + Endpoints.LOGIN_ENDPOINT, json=payload)
        return response

    @allure.step("Получить accessToken пользователя")
    def get_access_token(self, user_data):
        response = self.post_user_login(user_data)
        if response.status_code == 200:
            return response.json()["accessToken"]
        return None

    @allure.step("Изменить данные пользователя с авторизацией")
    def patch_user_data_with_auth(self, access_token, new_user_data):
        headers = {"Authorization": access_token}
        response = requests.patch(Endpoints.BASE_URL + Endpoints.USER_ENDPOINT, headers=headers, json=new_user_data)
        return response

    @allure.step("Изменить данные пользователя без авторизации")
    def patch_user_data_without_auth(self, new_user_data):
        response = requests.patch(Endpoints.BASE_URL + Endpoints.USER_ENDPOINT, json=new_user_data)
        return response

    @allure.step("Удалить пользователя")
    def delete_user(self, access_token):
        headers = {"Authorization": access_token}
        response = requests.delete(Endpoints.BASE_URL + Endpoints.USER_ENDPOINT, headers=headers)
        return response
