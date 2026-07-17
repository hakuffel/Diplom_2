class Endpoints:
    BASE_URL = "https://stellarburgers.education-services.ru"
    REGISTER_ENDPOINT = "/api/auth/register"
    LOGIN_ENDPOINT = "/api/auth/login"
    USER_ENDPOINT = "/api/auth/user"
    ORDERS_ENDPOINT = "/api/orders"
    INGREDIENTS_ENDPOINT = "/api/ingredients"


class Messages:
    USER_ALREADY_EXISTS = "User already exists"
    REQUIRED_FIELDS_MISSING = "Email, password and name are required fields"
    LOGIN_INCORRECT = "email or password are incorrect"
    SHOULD_BE_AUTHORISED = "You should be authorised"
    INGREDIENT_IDS_MUST_BE_PROVIDED = "Ingredient ids must be provided"


class Data:
    invalid_ingredients = [
        "000000000000000000000000",
    ]
