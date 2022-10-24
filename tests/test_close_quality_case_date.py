import json
from my_lib.assertions import Assertion
from my_lib.my_requests import MyRequests
from my_lib.base_case import BaseCase
import allure
import pytest


# python -m pytest -s test_close_quality_case_date.py -k Test_close_quality_case_date
# py.test --alluredir=allure_result_folder ./test_close_quality_case_date.py
# allure serve allure_result_folder

# Интеграция с ОЖУР. Закрытие Инцидента КачД на основании данных из ОЖУР
@allure.epic("Интеграция с ОЖУР. Закрытие Инцидента КачД на основании данных из ОЖУР")
class Test_close_quality_case_date(BaseCase):

    # Авторизация и получение необходимых cookie и headers
    @allure.description('Авторизация и получение необходимых cookie и headers')
    def setup(self):
        env = 'http://localmail.itexpert.ru:5057'
        auth_data = {
            "UserName": "Supervisor",
            "UserPassword": "!Supervisor123Test!"
        }
        self.url = "http://localmail.itexpert.ru:5057/rest/IteIncidentDQService/IncidentDQClose"
        self.jar, self.header = MyRequests.user_auth(self, auth_data, env)

# Закрытие Инцидента КачД на основании данных из ОЖУР
    @allure.description('Закрытие Инцидента КачД на основании данных из ОЖУР')
    def test_incbaseondate(self):
        json_data = {
            "externalSystemId": "41a83d9b-3b74-4909-80d3-7b30ef066f73",  # //id обращения из ОЖУР (ОБЯЗАТЕЛЬНОЕ)
            "solution": "тестовое закрытие",  # //Решение для пользователя

        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        print(response.text)
        obj = json.loads(response.text)
        assert obj['error'] is None, obj['error']
        assert obj['status'] != 0, obj['status']

