
import json
from my_lib.assertions import Assertion
from my_lib.my_requests import MyRequests
from my_lib.base_case import BaseCase


# python -m pytest -s tests\test_update_cost_type.py -k test_correct_delta_f_demo


# Тестирование загрузки справочника "Виды затрат"

class TestUpdateCostType(BaseCase):

# Авторизация и получение необходимых cookie и headers

    def setup(self):
        env = 'http://localhost:83'
        auth_data = {
            "UserName": "Supervisor",
            "UserPassword": "Supervisor"
        }
        self.url = "http://localhost:83/0/rest/SapErpIntegrationService/v1/UpdateCostType"
        self.jar, self.header = MyRequests.user_auth(self, auth_data, env)



# Загрузка справочника в режиме полной выгрузки (delta = "F") корректный запрос

    def test_correct_delta_f(self):
        test_name = 'Загрузка справочника в режиме полной выгрузки (delta = "F") корректный запрос'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 1",
                    "BUKRS": "IteBUCode 1",
                    "SAKNR": "IteCTNumAccount 1",
                    "KSTAR": "main test code 1",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.211",
                    "KATYP": "IteCTCostElementType 1",
                    "SPRAS": "IteCTLanguageCode 1",
                    "KTOPL": "IteCTChartOfAccounts 1",
                    "KTEXT": "IteCTCommonName 1",
                    "LTEXT": "IteCTDescription 1",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"


# Загрузка справочника в режиме обновления (delta = "D", deleted == "") корректный запрос
    def test_correct_delta_d_without_x(self):
        test_name = 'Загрузка справочника в режиме обновления (delta = "D", deleted == "") корректный запрос'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 2",
                    "BUKRS": "IteBUCode 2",
                    "SAKNR": "IteCTNumAccount 2",
                    "KSTAR": "main test code 2",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 2",
                    "SPRAS": "IteCTLanguageCode 2",
                    "KTOPL": "IteCTChartOfAccounts 2",
                    "KTEXT": "IteCTCommonName 2",
                    "LTEXT": "IteCTDescription 2",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Загрузка справочника в режиме обновления - деактивация записи (delta = "D", deleted == "X") корректный запрос

    def test_correct_delta_d_with_x(self):
        test_name = 'Загрузка справочника в режиме обновления - деактивация записи (delta = "D", deleted == "X") корректный запрос'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 2",
                    "BUKRS": "IteBUCode 2",
                    "SAKNR": "IteCTNumAccount 2",
                    "KSTAR": "main test code 2",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 2",
                    "SPRAS": "IteCTLanguageCode 2",
                    "KTOPL": "IteCTChartOfAccounts 2",
                    "KTEXT": "IteCTCommonName 2",
                    "LTEXT": "IteCTDescription 2",
                    "deleted": "X"
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Проверка граничных значений полей "currentPage" и "pageCount" ("currentPage":"1", "pageCount":"3")

    def test_boundary_values_p1_c3(self):
        test_name = 'Проверка граничных значений полей "currentPage" и "pageCount" ("currentPage":"1", "pageCount":"3",)'
        json_data = {
            "currentPage": "1",
            "pageCount": "3",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 3",
                    "BUKRS": "IteBUCode 3",
                    "SAKNR": "IteCTNumAccount 3",
                    "KSTAR": "main test code 3",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 3",
                    "SPRAS": "IteCTLanguageCode 3",
                    "KTOPL": "IteCTChartOfAccounts 3",
                    "KTEXT": "IteCTCommonName 3",
                    "LTEXT": "IteCTDescription 3",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Проверка граничных значений полей "currentPage" и "pageCount" ("currentPage":"3", "pageCount":"3")
    def test_boundary_values_p3_c3(self):
        test_name = 'Проверка граничных значений полей "currentPage" и "pageCount" ("currentPage":"3", "pageCount":"3",)'
        json_data = {
            "currentPage": "3",
            "pageCount": "3",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 4",
                    "BUKRS": "IteBUCode 4",
                    "SAKNR": "IteCTNumAccount 4",
                    "KSTAR": "main test code 4",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 4",
                    "SPRAS": "IteCTLanguageCode 4",
                    "KTOPL": "IteCTChartOfAccounts 4",
                    "KTEXT": "IteCTCommonName 4",
                    "LTEXT": "IteCTDescription 4",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Проверка граничных значений полей "currentPage" и "pageCount" -- выход из диапазона ("currentPage":"4", "pageCount":"3",)

    def test_boundary_values_p4_c3(self):
        test_name = 'Проверка граничных значений полей "currentPage" и "pageCount" -- выход из диапазона ("currentPage":"4", "pageCount":"3",)'
        json_data = {
            "currentPage": "4",
            "pageCount": "3",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 2",
                    "BUKRS": "IteBUCode 2",
                    "SAKNR": "IteCTNumAccount 2",
                    "KSTAR": "main test code 2",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 2",
                    "SPRAS": "IteCTLanguageCode 2",
                    "KTOPL": "IteCTChartOfAccounts 2",
                    "KTEXT": "IteCTCommonName 2",
                    "LTEXT": "IteCTDescription 2",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        assert obj['error'] == "Номер страницы превышает количество страниц", f"The value of 'MESSAGE' is not correct"
        assert obj['status'] == 400, f"The status is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "KSTAR")

    def test_null_kstar_value_delta_f(self):
        test_name = 'Проверка возможности создания записи без обязательных полей режим "F" (пустой "KSTAR")'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 8",
                    "BUKRS": "IteBUCode 8",
                    "SAKNR": "IteCTNumAccount 8",
                    "KSTAR": "",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 8",
                    "SPRAS": "IteCTLanguageCode 8",
                    "KTOPL": "IteCTChartOfAccounts 8",
                    "KTEXT": "IteCTCommonName 8",
                    "LTEXT": "IteCTDescription 8",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - KSTAR", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Загрузка уже существующей записи (изменение записи) в режиме полной выгрузки (delta = "F") корректный запрос

    def test_changing_an_existing_record_delta_f(self):
        test_name = 'Загрузка уже существующей записи (изменение записи) в режиме полной выгрузки (delta = "F") корректный запрос'
        json_data = {
            "currentPage": "1",
            "pageCount": "2",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 4 (new)",
                    "BUKRS": "IteBUCode 4 (new)",
                    "SAKNR": "IteCTNumAccount 4",
                    "KSTAR": "main test code 4 (new)",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 4 (new)",
                    "SPRAS": "IteCTLanguageCode 4 (new)",
                    "KTOPL": "IteCTChartOfAccounts 4 (new)",
                    "KTEXT": "IteCTCommonName 4 (new)",
                    "LTEXT": "IteCTDescription 4 (new)",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Загрузка уже существующей записи (запись актуальна) в режиме полной выгрузки (delta = "F") корректный запрос

    def test_changing_actual_record_delta_f(self):
        test_name = 'Загрузка уже существующей записи (запись актуальна) в режиме полной выгрузки (delta = "F") корректный запрос'
        json_data = {
            "currentPage": "1",
            "pageCount": "2",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 4 (new)",
                    "BUKRS": "IteBUCode 4 (new)",
                    "SAKNR": "IteCTNumAccount 4",
                    "KSTAR": "main test code 4 (new)",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 4 (new)",
                    "SPRAS": "IteCTLanguageCode 4 (new)",
                    "KTOPL": "IteCTChartOfAccounts 4 (new)",
                    "KTEXT": "IteCTCommonName 4 (new)",
                    "LTEXT": "IteCTDescription 4 (new)",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Запись актуальна", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "I", f"The value of 'TYPE' is not correct"


# Загрузка уже существующей записи (Изменение записи) в режиме обновления (delta = "D") корректный запрос

    def test_changing_an_existing_record_delta_d(self):
        test_name = 'Загрузка уже существующей записи (Изменение записи) в режиме обновления (delta = "D") корректный запрос'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "SAKNR": "IteCTNumAccount 3",
                    "KSTAR": "main test code 3 (new)",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 3 (new)",
                    "SPRAS": "IteCTLanguageCode 3 (new)",
                    "KTOPL": "IteCTChartOfAccounts 3 (new)",
                    "KTEXT": "IteCTCommonName 3 (new)",
                    "LTEXT": "IteCTDescription 3 (new)",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Загрузка уже существующей записи (запись актуальна) в режиме обновления (delta = "D") корректный запрос

    def test_changing_actual_record_delta_d(self):
        test_name = 'Загрузка уже существующей записи (Изменение записи) в режиме обновления (delta = "D") корректный запрос'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "SAKNR": "IteCTNumAccount 3",
                    "KSTAR": "main test code 3 (new)",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 3 (new)",
                    "SPRAS": "IteCTLanguageCode 3 (new)",
                    "KTOPL": "IteCTChartOfAccounts 3 (new)",
                    "KTEXT": "IteCTCommonName 3 (new)",
                    "LTEXT": "IteCTDescription 3 (new)",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Изменений в обновляемой записи не обнаружено", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "I", f"The value of 'TYPE' is not correct"

# Деактивация существующей записи в режиме обновления (delta = "D") корректный запрос

    def test_deactivate_record_delta_d(self):
        test_name = 'Деактивация существующей записи в режиме обновления (delta = "D") корректный запрос'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "SAKNR": "IteCTNumAccount 3",
                    "KSTAR": "main test code 3 (new)",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 3 (new)",
                    "SPRAS": "IteCTLanguageCode 3 (new)",
                    "KTOPL": "IteCTChartOfAccounts 3 (new)",
                    "KTEXT": "IteCTCommonName 3 (new)",
                    "LTEXT": "IteCTDescription 3 (new)",
                    "deleted": "X"
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Деактивация существующей записи в режиме полной выгрузки (delta = "F") корректный запрос

    def test_deactivate_record_delta_f(self):
        test_name = 'Деактивация существующей записи в режиме полной выгрузки (delta = "F") корректный запрос'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "SAKNR": "IteCTNumAccount 4",
                    "KSTAR": "main test code 3 (new)",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 3 (new)",
                    "SPRAS": "IteCTLanguageCode 3 (new)",
                    "KTOPL": "IteCTChartOfAccounts 3 (new)",
                    "KTEXT": "IteCTCommonName 3 (new)",
                    "LTEXT": "IteCTDescription 3 (new)",
                    "deleted": "X"
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Деактивация несуществующей записи в режиме полной выгрузки (delta = "D")

    def test_deactivate_not_exist_record_delta_d(self):
        test_name = 'Деактивация несуществующей записи в режиме полной выгрузки (delta = "D")'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "SAKNR": "IteCTNumAccount 3 (new)",
                    "KSTAR": "main test code 31",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 3 (new)",
                    "SPRAS": "IteCTLanguageCode 3 (new)",
                    "KTOPL": "IteCTChartOfAccounts 3 (new)",
                    "KTEXT": "IteCTCommonName 3 (new)",
                    "LTEXT": "IteCTDescription 3 (new)",
                    "deleted": "X"
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Удаляемая запись отсутствует в справочнике", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

# Запрос с некорректным параметром (delta = "М")

    def test_uncorrect_delta(self):
        test_name = 'Запрос с некорректным параметром (delta = "М")'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "М",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "SAKNR": "IteCTNumAccount 31",
                    "KSTAR": "main test code 3 (new)",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 3 (new)",
                    "SPRAS": "IteCTLanguageCode 3 (new)",
                    "KTOPL": "IteCTChartOfAccounts 3 (new)",
                    "KTEXT": "IteCTCommonName 3 (new)",
                    "LTEXT": "IteCTDescription 3 (new)",
                    "deleted": "X"
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        assert obj['error'] == "Режим выгрузки справочника не идентифицирован", f"The value of 'MESSAGE' is not correct"



