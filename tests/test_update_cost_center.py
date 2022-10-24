import json
from my_lib.assertions import Assertion
from my_lib.my_requests import MyRequests
from my_lib.base_case import BaseCase


# python -m pytest -s tests\test_update_cost_center.py -k test_correct_delta_f


# Тестирование загрузки справочника "Значения аналитического признака "Место возникновения затрат""

class TestUpdateLogisticStructure(BaseCase):

# Авторизация и получение необходимых cookie и headers

    def setup(self):
        env = 'http://localmail.itexpert.ru:5057'
        auth_data = {
            "UserName": "a.zvezdin",
            "UserPassword": "123"
        }
        self.url = "http://localmail.itexpert.ru:5057/rest/SapErpIntegrationService/v1/UpdateCostCenter"
        self.jar, self.header = MyRequests.user_auth(self, auth_data, env)


    """
    def test_correct_delta_f_demo(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "4",
                    "PBUKR": "IteBUCode 1",
                    "POSID": "main test code 1",
                    "POST1": "IteItemName 1",
                    "ERDAT": "01.01.01",
                    "AEDAT": "01.01.01",
                    "VERNR": "IteItemResponsible 1",
                    "USR00": "IteFinancingType 1",
                    "USR01": "IteCSSCode 1",
                    "ZZ_NAPRD": "IteActivityDirection 1",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        print(response.text)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"
    """


# Загрузка справочника в режиме полной выгрузки (delta = "F") корректный запрос

    def test_correct_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "main test code 125",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "0",
                    "KOKRS": "IteCSControllingUnit 1",
                    "BUKRS": "IteBUCode 1",
                    "GSBER": "IteCSBusinessArea 1",
                    "KOSAR": "IteCSKind 1",
                    "VERAK": "IteICSResponsible 1",
                    "VERAK_USER": "IteCSResponsibleUser 1",
                    "KHINR": "IteCSPartOfHierarchy 1",
                    "KTEXT": "IteCSName 1",
                    "LTEXT": "IteCSDescription 1",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"


# Загрузка справочника в режиме обновления (delta = "D", deleted == "") корректный запрос
    def test_correct_delta_d_without_x(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "main test code 2",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "0",
                    "KOKRS": "IteCSControllingUnit 2",
                    "BUKRS": "IteBUCode 2",
                    "GSBER": "IteCSBusinessArea 2",
                    "KOSAR": "IteCSKind 2",
                    "VERAK": "IteICSResponsible 2",
                    "VERAK_USER": "IteCSResponsibleUser 2",
                    "KHINR": "IteCSPartOfHierarchy 2",
                    "KTEXT": "IteCSName 2",
                    "LTEXT": "IteCSDescription 2",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Загрузка справочника в режиме обновления - деактивация записи (delta = "D", deleted == "X") корректный запрос

    def test_correct_delta_d_with_x(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "main test code 2",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "0",
                    "KOKRS": "IteCSControllingUnit 2",
                    "BUKRS": "IteBUCode 2",
                    "GSBER": "IteCSBusinessArea 2",
                    "KOSAR": "IteCSKind 2",
                    "VERAK": "IteICSResponsible 2",
                    "VERAK_USER": "IteCSResponsibleUser 2",
                    "KHINR": "IteCSPartOfHierarchy 2",
                    "KTEXT": "IteCSName 2",
                    "LTEXT": "IteCSDescription 2",
                    "deleted": "X"
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Проверка граничных значений полей "currentPage" и "pageCount" ("currentPage":"1", "pageCount":"3",)

    def test_boundary_values_p1_c3(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "3",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "main test code 3",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "1",
                    "KOKRS": "IteCSControllingUnit 3",
                    "BUKRS": "IteBUCode 3",
                    "GSBER": "IteCSBusinessArea 3",
                    "KOSAR": "IteCSKind 3",
                    "VERAK": "IteICSResponsible 3",
                    "VERAK_USER": "IteCSResponsibleUser 3",
                    "KHINR": "IteCSPartOfHierarchy 3",
                    "KTEXT": "IteCSName 3",
                    "LTEXT": "IteCSDescription 3",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Проверка граничных значений полей "currentPage" и "pageCount" ("currentPage":"3", "pageCount":"3",)
    def test_boundary_values_p3_c3(self):
        json_data = {
            "currentPage": "3",
            "pageCount": "3",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "main test code 4",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "0",
                    "KOKRS": "IteCSControllingUnit 4",
                    "BUKRS": "IteBUCode 4",
                    "GSBER": "IteCSBusinessArea 4",
                    "KOSAR": "IteCSKind 4",
                    "VERAK": "IteICSResponsible 4",
                    "VERAK_USER": "IteCSResponsibleUser 4",
                    "KHINR": "IteCSPartOfHierarchy 4",
                    "KTEXT": "IteCSName 4",
                    "LTEXT": "IteCSDescription 4",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Проверка граничных значений полей "currentPage" и "pageCount" -- выход из диапазона ("currentPage":"4", "pageCount":"3",)

    def test_boundary_values_p4_c3(self):
        json_data = {
            "currentPage": "4",
            "pageCount": "3",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "main test code 4",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "0",
                    "KOKRS": "IteCSControllingUnit 4",
                    "BUKRS": "IteBUCode 4",
                    "GSBER": "IteCSBusinessArea 4",
                    "KOSAR": "IteCSKind 4",
                    "VERAK": "IteICSResponsible 4",
                    "VERAK_USER": "IteCSResponsibleUser 4",
                    "KHINR": "IteCSPartOfHierarchy 4",
                    "KTEXT": "IteCSName 4",
                    "LTEXT": "IteCSDescription 4",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        assert obj['error'] == "Номер страницы превышает количество страниц", f"The value of 'MESSAGE' is not correct"
        assert obj['status'] == 400, f"The status is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "KOSTL")

    def test_null_kostl_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "0",
                    "KOKRS": "IteCSControllingUnit 5",
                    "BUKRS": "IteBUCode 5",
                    "GSBER": "IteCSBusinessArea 5",
                    "KOSAR": "IteCSKind 5",
                    "VERAK": "IteICSResponsible 5",
                    "VERAK_USER": "IteCSResponsibleUser 5",
                    "KHINR": "IteCSPartOfHierarchy 5",
                    "KTEXT": "IteCSName 5",
                    "LTEXT": "IteCSDescription 5",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - KOSTL", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "BUKRS")

    def test_null_bukrs_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "main test code 10",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "1",
                    "KOKRS": "IteCSControllingUnit 10",
                    "BUKRS": "",
                    "GSBER": "IteCSBusinessArea 10",
                    "KOSAR": "IteCSKind 10",
                    "VERAK": "IteICSResponsible 10",
                    "VERAK_USER": "IteCSResponsibleUser 10",
                    "KHINR": "IteCSPartOfHierarchy 10",
                    "KTEXT": "IteCSName 10",
                    "LTEXT": "IteCSDescription 10",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - BUKRS", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"



# Проверка возможности создания записи без обязательных полей режим "F" (пустой "KOSAR")

    def test_null_kosar_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "main test code 12",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "1",
                    "KOKRS": "IteCSControllingUnit 12",
                    "BUKRS": "IteBUCode 12",
                    "GSBER": "IteCSBusinessArea 12",
                    "KOSAR": "",
                    "VERAK": "IteICSResponsible 12",
                    "VERAK_USER": "IteCSResponsibleUser 12",
                    "KHINR": "IteCSPartOfHierarchy 12",
                    "KTEXT": "IteCSName 12",
                    "LTEXT": "IteCSDescription 12",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - KOSAR", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"



# Загрузка уже существующей записи (изменение записи) в режиме полной выгрузки (delta = "F") корректный запрос

    def test_changing_an_existing_record_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "main test code 1",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "0",
                    "KOKRS": "IteCSControllingUnit 2 (new)",
                    "BUKRS": "IteBUCode 2 (new)",
                    "GSBER": "IteCSBusinessArea 2 (new)",
                    "KOSAR": "IteCSKind 2 (new)",
                    "VERAK": "IteICSResponsible 2 (new)",
                    "VERAK_USER": "IteCSResponsibleUser 2 (new)",
                    "KHINR": "IteCSPartOfHierarchy 2 (new)",
                    "KTEXT": "IteCSName 2 (new)",
                    "LTEXT": "IteCSDescription 2 (new)",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Загрузка уже существующей записи (запись актуальна) в режиме полной выгрузки (delta = "F") корректный запрос

    def test_changing_actual_record_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "main test code 1",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "0",
                    "KOKRS": "IteCSControllingUnit 2 (new)",
                    "BUKRS": "IteBUCode 2 (new)",
                    "GSBER": "IteCSBusinessArea 2 (new)",
                    "KOSAR": "IteCSKind 2 (new)",
                    "VERAK": "IteICSResponsible 2 (new)",
                    "VERAK_USER": "IteCSResponsibleUser 2 (new)",
                    "KHINR": "IteCSPartOfHierarchy 2 (new)",
                    "KTEXT": "IteCSName 2 (new)",
                    "LTEXT": "IteCSDescription 2 (new)",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Запись актуальна", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "I", f"The value of 'TYPE' is not correct"


# Загрузка уже существующей записи (Изменение записи) в режиме обновления (delta = "D") корректный запрос

    def test_changing_an_existing_record_delta_d(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "main test code 3",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "1",
                    "KOKRS": "IteCSControllingUnit 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "GSBER": "IteCSBusinessArea 3 (new)",
                    "KOSAR": "IteCSKind 3 (new)",
                    "VERAK": "IteICSResponsible 3 (new)",
                    "VERAK_USER": "IteCSResponsibleUser 3 (new)",
                    "KHINR": "IteCSPartOfHierarchy 3 (new)",
                    "KTEXT": "IteCSName 3 (new)",
                    "LTEXT": "IteCSDescription 3 (new)",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Загрузка уже существующей записи (запись актуальна) в режиме обновления (delta = "D") корректный запрос

    def test_changing_actual_record_delta_d(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "main test code 3",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "1",
                    "KOKRS": "IteCSControllingUnit 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "GSBER": "IteCSBusinessArea 3 (new)",
                    "KOSAR": "IteCSKind 3 (new)",
                    "VERAK": "IteICSResponsible 3 (new)",
                    "VERAK_USER": "IteCSResponsibleUser 3 (new)",
                    "KHINR": "IteCSPartOfHierarchy 3 (new)",
                    "KTEXT": "IteCSName 3 (new)",
                    "LTEXT": "IteCSDescription 3 (new)",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Изменений в обновляемой записи не обнаружено", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "I", f"The value of 'TYPE' is not correct"

# Деактивация существующей записи в режиме обновления (delta = "D") корректный запрос

    def test_deactivate_record_delta_d(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "main test code 4",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "0",
                    "KOKRS": "IteCSControllingUnit 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "GSBER": "IteCSBusinessArea 3 (new)",
                    "KOSAR": "IteCSKind 3 (new)",
                    "VERAK": "IteICSResponsible 3 (new)",
                    "VERAK_USER": "IteCSResponsibleUser 3 (new)",
                    "KHINR": "IteCSPartOfHierarchy 3 (new)",
                    "KTEXT": "IteCSName 3 (new)",
                    "LTEXT": "IteCSDescription 3 (new)",
                    "deleted": "X"
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Деактивация существующей записи в режиме полной выгрузки (delta = "F") корректный запрос

    def test_deactivate_record_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "main test code 1",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "0",
                    "KOKRS": "IteCSControllingUnit 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "GSBER": "IteCSBusinessArea 3 (new)",
                    "KOSAR": "IteCSKind 3 (new)",
                    "VERAK": "IteICSResponsible 3 (new)",
                    "VERAK_USER": "IteCSResponsibleUser 3 (new)",
                    "KHINR": "IteCSPartOfHierarchy 3 (new)",
                    "KTEXT": "IteCSName 3 (new)",
                    "LTEXT": "IteCSDescription 3 (new)",
                    "deleted": "X"
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Деактивация несуществующей записи в режиме полной выгрузки (delta = "D") корректный запрос

    def test_deactivate_not_exist_record_delta_d(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "main test code 23",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "0",
                    "KOKRS": "IteCSControllingUnit 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "GSBER": "IteCSBusinessArea 3 (new)",
                    "KOSAR": "IteCSKind 3 (new)",
                    "VERAK": "IteICSResponsible 3 (new)",
                    "VERAK_USER": "IteCSResponsibleUser 3 (new)",
                    "KHINR": "IteCSPartOfHierarchy 3 (new)",
                    "KTEXT": "IteCSName 3 (new)",
                    "LTEXT": "IteCSDescription 3 (new)",
                    "deleted": "X"
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Удаляемая запись отсутствует в справочнике", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

# Запрос с некорректным параметром (delta = "М")

    def test_uncorrect_delta(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "М",
            "item": [
                {
                    "row": "1",
                    "KOSTL": "main test code 3",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "BKZKP": "0",
                    "KOKRS": "IteCSControllingUnit 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "GSBER": "IteCSBusinessArea 3 (new)",
                    "KOSAR": "IteCSKind 3 (new)",
                    "VERAK": "IteICSResponsible 3 (new)",
                    "VERAK_USER": "IteCSResponsibleUser 3 (new)",
                    "KHINR": "IteCSPartOfHierarchy 3 (new)",
                    "KTEXT": "IteCSName 3 (new)",
                    "LTEXT": "IteCSDescription 3 (new)",
                    "deleted": "X"
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        assert obj['error'] == "Режим выгрузки справочника не идентифицирован", f"The value of 'MESSAGE' is not correct"



