import json
from my_lib.assertions import Assertion
from my_lib.my_requests import MyRequests
from my_lib.base_case import BaseCase


# python -m pytest -s tests\test_update_fm_structure.py -k test_correct_delta_f_demo


# Тестирование загрузки справочника "Подразделения финансового менеджмента"

class TestUpdatePurchaseGroups(BaseCase):

# Авторизация и получение необходимых cookie и headers

    def setup(self):
        env = 'http://localhost:83'
        auth_data = {
            "UserName": "Supervisor",
            "UserPassword": "Supervisor"
        }
        self.url = "http://localhost:83/0/rest/SapErpIntegrationService/v1/UpdateFMStructure"
        self.jar, self.header = MyRequests.user_auth(self, auth_data, env)


# Загрузка справочника в режиме полной выгрузки (delta = "F") корректный запрос
    def test_correct_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "BUKRS": "main test code 1",
                    "FICTR": "FMUCode 1",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
                    "BOSSNAME": "FMU Responsible 1",
                    "BEZEICH": "FMU Name 1",
                    "BESCHR": "FMU description 1",
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
                    "BUKRS": "main test code 2",
                    "FICTR": "FMUCode 2",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
                    "BOSSNAME": "FMU Responsible 2",
                    "BEZEICH": "FMU Name 2",
                    "BESCHR": "FMU description 2",
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
                    "BUKRS": "main test code 2",
                    "FICTR": "FMUCode 2",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
                    "BOSSNAME": "FMU Responsible 2",
                    "BEZEICH": "FMU Name 1",
                    "BESCHR": "FMU description 2",
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
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "BUKRS": "main test code 3",
                    "FICTR": "FMUCode 3",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
                    "BOSSNAME": "FMU Responsible 3",
                    "BEZEICH": "FMU Name 1",
                    "BESCHR": "FMU description 3",
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
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "BUKRS": "main test code 4",
                    "FICTR": "FMUCode 4",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
                    "BOSSNAME": "FMU Responsible 4",
                    "BEZEICH": "FMU Name 1",
                    "BESCHR": "FMU description 4",
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
                    "BUKRS": "main test code 1",
                    "FICTR": "FMUCode 1",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
                    "BOSSNAME": "FMU Responsible 1",
                    "BEZEICH": "FMU Name 1",
                    "BESCHR": "FMU description 5",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        assert obj['error'] == "Номер страницы превышает количество страниц", f"The value of 'MESSAGE' is not correct"
        assert obj['status'] == 400, f"The status is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "BUKRS")

    def test_null_bukrs_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "BUKRS": "",
                    "FICTR": "FMUCode 1",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
                    "BOSSNAME": "FMU Responsible 1",
                    "BEZEICH": "FMU Name 1",
                    "BESCHR": "FMU description 6",
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

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "FICTR")

    def test_null_fictr_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "BUKRS": "main test code 4",
                    "FICTR": "",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
                    "BOSSNAME": "FMU Responsible 1",
                    "BEZEICH": "FMU Name 1",
                    "BESCHR": "FMU description 7",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - FICTR", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "DATBIS")

    def test_null_datbis_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "BUKRS": "main test code 4",
                    "FICTR": "FMUCode 4",
                    "DATAB": "01.01.20",
                    "DATBIS": "",
                    "BOSSNAME": "FMU Responsible 4",
                    "BEZEICH": "FMU Name 1",
                    "BESCHR": "FMU description 4",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - DATBIS", f"The value of 'MESSAGE' is not correct"
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
                    "BUKRS": "main test code 4",
                    "FICTR": "FMUCode 1 (new)",
                    "DATAB": "02.01.20",
                    "DATBIS": "30.12.21",
                    "BOSSNAME": "FMU Responsible 1 (new)",
                    "BEZEICH": "FMU Name 1 (new)",
                    "BESCHR": "FMU description 10 (new)",
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
                    "BUKRS": "main test code 4",
                    "FICTR": "FMUCode 1 (new)",
                    "DATAB": "02.01.20",
                    "DATBIS": "30.12.21",
                    "BOSSNAME": "FMU Responsible 1 (new)",
                    "BEZEICH": "FMU Name 1 (new)",
                    "BESCHR": "FMU description 10 (new)",
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
                    "BUKRS": "main test code 5",
                    "FICTR": "FMUCode 5 (new)",
                    "DATAB": "02.02.20",
                    "DATBIS": "30.12.21",
                    "BOSSNAME": "FMU Responsible 5 (new)",
                    "BEZEICH": "FMU Name 5 (new)",
                    "BESCHR": "FMU description 5 (new)",
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
                    "BUKRS": "main test code 5",
                    "FICTR": "FMUCode 5",
                    "DATAB": "02.02.20",
                    "DATBIS": "30.12.21",
                    "BOSSNAME": "FMU Responsible 5 (new)",
                    "BEZEICH": "FMU Name 5 (new)",
                    "BESCHR": "FMU description 5 (new)",
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
                    "BUKRS": "main test code 5",
                    "FICTR": "FMUCode 1",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
                    "BOSSNAME": "FMU Responsible 1",
                    "BEZEICH": "FMU Name 1",
                    "BESCHR": "FMU description 14",
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

# Деактивация существующей записи в режиме полной выгрузки (delta = "F") корректный запрос

    def test_deactivate_record_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "BUKRS": "main test code 1",
                    "FICTR": "FMUCode 1",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
                    "BOSSNAME": "FMU Responsible 1",
                    "BEZEICH": "FMU Name 1",
                    "BESCHR": "FMU description 15",
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

# Деактивация несуществующей записи в режиме полной выгрузки (delta = "D") корректный запрос

    def test_deactivate_not_exist_record_delta_d(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "BUKRS": "main test code 18",
                    "FICTR": "FMUCode 1",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
                    "BOSSNAME": "FMU Responsible 1",
                    "BEZEICH": "FMU Name 1",
                    "BESCHR": "FMU description 17",
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
                    "BUKRS": "main test code 18",
                    "FICTR": "FMUCode 1",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
                    "BOSSNAME": "FMU Responsible 1",
                    "BEZEICH": "FMU Name 1",
                    "BESCHR": "FMU description 17",
                    "deleted": "X"
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        assert obj['error'] == "Режим выгрузки справочника не идентифицирован", f"The value of 'MESSAGE' is not correct"
