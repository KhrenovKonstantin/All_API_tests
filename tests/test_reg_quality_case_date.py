import json
import uuid

from my_lib.assertions import Assertion
from my_lib.base_case import BaseCase
from my_lib.my_requests import MyRequests
import allure


# python -m pytest -s test_reg_quality_case_date.py -k Test_reg_quality_case_date
# py.test --alluredir=allure_result_folder ./test_reg_quality_case_date.py
# allure serve allure_result_folder

# Интеграция с ОЖУР. Регистрация Инцидента КачД на основании данных из ОЖУР
@allure.epic("Интеграция с ОЖУР. Регистрация Инцидента КачД на основании данных из ОЖУР")
class Test_reg_quality_case_date(BaseCase):

    # Авторизация и получение необходимых cookie и headers
    @allure.description('Авторизация и получение необходимых cookie и headers')
    def setup(self):
        env = 'http://localmail.itexpert.ru:5057'
        auth_data = {
            "UserName": "Supervisor",
            "UserPassword": "!Supervisor123Test!"
        }
        self.url = "http://localmail.itexpert.ru:5057/rest/IteIncidentDQService/IncidentDQReg"
        self.jar, self.header = MyRequests.user_auth(self, auth_data, env)

    @allure.description('Заполнен логин исполнителя Состояние = В работе')
    # Заполнен логин исполнителя Состояние = В работе
    def test_incbaseondate_one(self):
        myuuid = uuid.uuid4()
        strmyuid = (str(myuuid))
        json_data = {
            "externalSystemId": f"{strmyuid}",  # //id обращения из ОЖУР (ОБЯЗАТЕЛЬНОЕ)
            "executerLogin": "Хренов Константин",  # //Логин AD Исполнителя
            # "confItemCode": "string",  # //Код ЕСИС Конфигурационной единицы (ОБЯЗАТЕЛЬНОЕ) Зачеркнуто в постановке
            "priority": "3",  # //Номер приоритета: 1 - Высокий, 2 - Средний, 3 - Низкий
            "ownerLogin": "",  # //Логин AD Ответственного
            "monitoringSystemCode": "220760",  # //Код ЕСИС Системы мониторинга КачД (ОБЯЗАТЕЛЬНОЕ)
            "subject": "Автотест инцидент КАчд",  # //Тема инцидента (ОБЯЗАТЕЛЬНОЕ)
            "symptoms": "Тестовое описание инцидента",  # //Описание инцидента, признаки (ОБЯЗАТЕЛЬНОЕ)
            "businessRuleId": "0a0743db-b6f2-4939-be4b-0b1cecf687cd",
            # //id Бизнес-правила из внешней системы (ОБЯЗАТЕЛЬНОЕ)
            "notes": "Тестовое примечание инцидента",  # //Примечания
            "businessKey": "111111",  # //Бизнес-ключ (ОБЯЗАТЕЛЬНОЕ)
            "groupName": "",  # //группа ответственных
            "account": "Компания 1",  # //Название ДО в Creatio
            # "accountCode": "Компания 1" # //"Код СДО" ДО в Creatio /// Было добавленов рамках таска https://jira.itexpert.ru/browse/IT4ITMVP-6415
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        print(response.text)
        obj = json.loads(response.text)
        assert obj['error'] is None, obj['error']

    @allure.description('Заполнен Логин AD Ответственного Состояние = Назначен специалист')
    # Заполнен Логин AD Ответственного Состояние = Назначен специалист
    def test_incbaseondate_two(self):
        myuuid = uuid.uuid4()
        strmyuid = (str(myuuid))
        json_data = {
            "externalSystemId": f"{strmyuid}",  # //id обращения из ОЖУР (ОБЯЗАТЕЛЬНОЕ)
            "executerLogin": "",  # //Логин AD Исполнителя
            # "confItemCode": "string",  # //Код ЕСИС Конфигурационной единицы (ОБЯЗАТЕЛЬНОЕ) Зачеркнуто в постановке
            "priority": "3",  # //Номер приоритета: 1 - Высокий, 2 - Средний, 3 - Низкий
            "ownerLogin": "Хренов Константин",  # //Логин AD Ответственного
            "monitoringSystemCode": "220760",  # //Код ЕСИС Системы мониторинга КачД (ОБЯЗАТЕЛЬНОЕ)
            "subject": "Автотест инцидент КАчд",  # //Тема инцидента (ОБЯЗАТЕЛЬНОЕ)
            "symptoms": "Тестовое описание инцидента",  # //Описание инцидента, признаки (ОБЯЗАТЕЛЬНОЕ)
            "businessRuleId": "0a0743db-b6f2-4939-be4b-0b1cecf687cd",
            # //id Бизнес-правила из внешней системы (ОБЯЗАТЕЛЬНОЕ)
            "notes": "Тестовое примечание инцидента",  # //Примечания
            "businessKey": "111111",  # //Бизнес-ключ (ОБЯЗАТЕЛЬНОЕ)
            "groupName": "",  # //группа ответственных
            "account": "Компания 1",  # //Название ДО в Creatio
            # "accountCode": "Компания 1" # //"Код СДО" ДО в Creatio /// Было добавленов рамках таска https://jira.itexpert.ru/browse/IT4ITMVP-6415
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        print(response.text)
        obj = json.loads(response.text)
        assert obj['error'] is None, obj['error']

    @allure.description('Заполнена группа ответственных Состояние = Назначен в группу')
    # Заполнена группа ответственных Состояние = Назначен в группу
    def test_incbaseondate_tree(self):
        myuuid = uuid.uuid4()
        strmyuid = (str(myuuid))
        json_data = {
            "externalSystemId": f"{strmyuid}",  # //id обращения из ОЖУР (ОБЯЗАТЕЛЬНОЕ)
            "executerLogin": "",  # //Логин AD Исполнителя
            # "confItemCode": "string",  # //Код ЕСИС Конфигурационной единицы (ОБЯЗАТЕЛЬНОЕ) Зачеркнуто в постановке
            "priority": "3",  # //Номер приоритета: 1 - Высокий, 2 - Средний, 3 - Низкий
            "ownerLogin": "",  # //Логин AD Ответственного
            "monitoringSystemCode": "220760",  # //Код ЕСИС Системы мониторинга КачД (ОБЯЗАТЕЛЬНОЕ)
            "subject": "Автотест инцидент КАчд",  # //Тема инцидента (ОБЯЗАТЕЛЬНОЕ)
            "symptoms": "Тестовое описание инцидента",  # //Описание инцидента, признаки (ОБЯЗАТЕЛЬНОЕ)
            "businessRuleId": "0a0743db-b6f2-4939-be4b-0b1cecf687cd",
            # //id Бизнес-правила из внешней системы (ОБЯЗАТЕЛЬНОЕ)
            "notes": "Тестовое примечание инцидента",  # //Примечания
            "businessKey": "111111",  # //Бизнес-ключ (ОБЯЗАТЕЛЬНОЕ)
            "groupName": "ТЕСТ",  # //группа ответственных
            "account": "Компания 1",  # //Название ДО в Creatio
            # "accountCode": "Компания 1" # //"Код СДО" ДО в Creatio /// Было добавленов рамках таска https://jira.itexpert.ru/browse/IT4ITMVP-6415
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        print(response.text)
        obj = json.loads(response.text)
        assert obj['error'] is None, obj['error']
