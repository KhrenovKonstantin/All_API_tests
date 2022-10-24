import json
from my_lib.assertions import Assertion
from my_lib.my_requests import MyRequests
from my_lib.base_case import BaseCase


# python -m pytest -s tests\test_update_logistic_structure.py -k test_correct_delta_f_demo


# Тестирование загрузки справочника "Организационная структура в части закупочной логистики"

class TestUpdateLogisticStructure(BaseCase):

# Авторизация и получение необходимых cookie и headers

    def setup(self):
        env = 'http://localhost:83'
        auth_data = {
            "UserName": "Supervisor",
            "UserPassword": "Supervisor"
        }
        self.url = "http://localhost:83/0/rest/SapErpIntegrationService/v1/UpdateLogisticStructure"
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
                    "BUTXT": "IteBUName 1",
                    "WERKS": "ItePlantCode 1",
                    "NAME1": "ItePlantName 1",
                    "EKORG": "ItePOCode 1",
                    "LGORT": "IteWHCode 1",
                    "LGOBE": "IteWHName 1",
                    "LGORT1": "IteSOCode 1",
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
                    "BUTXT": "IteBUName 2",
                    "WERKS": "ItePlantCode 2",
                    "NAME1": "ItePlantName 2",
                    "EKORG": "ItePOCode 2",
                    "LGORT": "IteWHCode 2",
                    "LGOBE": "IteWHName 2",
                    "LGORT1": "IteSOCode 2",
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
                    "BUTXT": "IteBUName 2",
                    "WERKS": "ItePlantCode 2",
                    "NAME1": "ItePlantName 2",
                    "EKORG": "ItePOCode 2",
                    "LGORT": "IteWHCode 2",
                    "LGOBE": "IteWHName 2",
                    "LGORT1": "IteSOCode 2",
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
                    "BUKRS": "main test code 3",
                    "BUTXT": "IteBUName 3",
                    "WERKS": "ItePlantCode 3",
                    "NAME1": "ItePlantName 3",
                    "EKORG": "ItePOCode 3",
                    "LGORT": "IteWHCode 3",
                    "LGOBE": "IteWHName 3",
                    "LGORT1": "IteSOCode 3",
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
                    "BUKRS": "main test code 4",
                    "BUTXT": "IteBUName 4",
                    "WERKS": "ItePlantCode 4",
                    "NAME1": "ItePlantName 4",
                    "EKORG": "ItePOCode 4",
                    "LGORT": "IteWHCode 4",
                    "LGOBE": "IteWHName 4",
                    "LGORT1": "IteSOCode 4",
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
                    "BUKRS": "main test code 3",
                    "BUTXT": "IteBUName 3",
                    "WERKS": "ItePlantCode 3",
                    "NAME1": "ItePlantName 3",
                    "EKORG": "ItePOCode 3",
                    "LGORT": "IteWHCode 3",
                    "LGOBE": "IteWHName 3",
                    "LGORT1": "IteSOCode 3",
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
                    "BUTXT": "IteBUName 3",
                    "WERKS": "ItePlantCode 3",
                    "NAME1": "ItePlantName 3",
                    "EKORG": "ItePOCode 3",
                    "LGORT": "IteWHCode 3",
                    "LGOBE": "IteWHName 3",
                    "LGORT1": "IteSOCode 3",
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

# Загрузка уже существующей записи (изменение записи) в режиме полной выгрузки (delta = "F") корректный запрос

    def test_changing_an_existing_record_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "BUKRS": "main test code 3",
                    "BUTXT": "IteBUName 3 (new)",
                    "WERKS": "ItePlantCode 3",
                    "NAME1": "ItePlantName 3",
                    "EKORG": "ItePOCode 3",
                    "LGORT": "IteWHCode 3",
                    "LGOBE": "IteWHName 3",
                    "LGORT1": "IteSOCode 3 (new)",
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
                    "BUKRS": "main test code 3",
                    "BUTXT": "IteBUName 3 (new)",
                    "WERKS": "ItePlantCode 3",
                    "NAME1": "ItePlantName 3",
                    "EKORG": "ItePOCode 3",
                    "LGORT": "IteWHCode 3",
                    "LGOBE": "IteWHName 3",
                    "LGORT1": "IteSOCode 3 (new)",
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
                    "BUKRS": "main test code 3",
                    "BUTXT": "IteBUName 3 (new)",
                    "WERKS": "ItePlantCode 3",
                    "NAME1": "ItePlantName 3 (new)",
                    "EKORG": "ItePOCode 3",
                    "LGORT": "IteWHCode 3",
                    "LGOBE": "IteWHName 3 (new)",
                    "LGORT1": "IteSOCode 3 (new)",
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
                    "BUKRS": "main test code 3",
                    "BUTXT": "IteBUName 3 (new)",
                    "WERKS": "ItePlantCode 3",
                    "NAME1": "ItePlantName 3 (new)",
                    "EKORG": "ItePOCode 3",
                    "LGORT": "IteWHCode 3",
                    "LGOBE": "IteWHName 3 (new)",
                    "LGORT1": "IteSOCode 3 (new)",
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
                    "BUKRS": "main test code 3",
                    "BUTXT": "IteBUName 3 (new)",
                    "WERKS": "ItePlantCode 3",
                    "NAME1": "ItePlantName 3 (new)",
                    "EKORG": "ItePOCode 3",
                    "LGORT": "IteWHCode 3",
                    "LGOBE": "IteWHName 3 (new)",
                    "LGORT1": "IteSOCode 3 (new)",
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
                    "BUKRS": "main test code 2",
                    "BUTXT": "IteBUName 2",
                    "WERKS": "ItePlantCode 2",
                    "NAME1": "ItePlantName 2",
                    "EKORG": "ItePOCode 2",
                    "LGORT": "IteWHCode 2",
                    "LGOBE": "IteWHName 2",
                    "LGORT1": "IteSOCode 2",
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
                    "BUKRS": "main test code 17",
                    "BUTXT": "IteBUName 2",
                    "WERKS": "ItePlantCode 2",
                    "NAME1": "ItePlantName 2",
                    "EKORG": "ItePOCode 2",
                    "LGORT": "IteWHCode 2",
                    "LGOBE": "IteWHName 2",
                    "LGORT1": "IteSOCode 2",
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
                    "BUKRS": "main test code 17",
                    "BUTXT": "IteBUName 2",
                    "WERKS": "ItePlantCode 2",
                    "NAME1": "ItePlantName 2",
                    "EKORG": "ItePOCode 2",
                    "LGORT": "IteWHCode 2",
                    "LGOBE": "IteWHName 2",
                    "LGORT1": "IteSOCode 2",
                    "deleted": "X"
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        assert obj['error'] == "Режим выгрузки справочника не идентифицирован", f"The value of 'MESSAGE' is not correct"



