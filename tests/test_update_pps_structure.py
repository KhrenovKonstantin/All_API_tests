import json
from my_lib.assertions import Assertion
from my_lib.my_requests import MyRequests
from my_lib.base_case import BaseCase


# python -m pytest -s tests\test_update_pps_structure.py -k test_correct_delta_f_demo


# Тестирование загрузки справочника "Значения аналитического признака "СПП-элемент""

class TestUpdatePPStructure(BaseCase):

# Авторизация и получение необходимых cookie и headers

    def setup(self):
        env = 'http://localhost:83'
        auth_data = {
            "UserName": "Supervisor",
            "UserPassword": "Supervisor"
        }
        self.url = "http://localhost:83/0/rest/SapErpIntegrationService/v1/UpdatePPStructure"
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
                    "PBUKR": "IteBUCode 1",
                    "POSID": "main test code 1",
                    "POST1": "IteItemName 1",
                    "ERDAT": "01.01.20",
                    "AEDAT": "31.12.21",
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
                    "PBUKR": "IteBUCode 2",
                    "POSID": "main test code 2",
                    "POST1": "IteItemName 2",
                    "ERDAT": "01.01.20",
                    "AEDAT": "31.12.21",
                    "VERNR": "IteItemResponsible 2",
                    "USR00": "IteFinancingType 2",
                    "USR01": "IteCSSCode 2",
                    "ZZ_NAPRD": "IteActivityDirection 2",
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
                    "PBUKR": "IteBUCode 2",
                    "POSID": "main test code 2",
                    "POST1": "IteItemName 2",
                    "ERDAT": "01.01.20",
                    "AEDAT": "31.12.21",
                    "VERNR": "IteItemResponsible 2",
                    "USR00": "IteFinancingType 2",
                    "USR01": "IteCSSCode 2",
                    "ZZ_NAPRD": "IteActivityDirection 2",
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
                    "PBUKR": "IteBUCode 3",
                    "POSID": "main test code 3",
                    "POST1": "IteItemName 3",
                    "ERDAT": "01.01.20",
                    "AEDAT": "31.12.21",
                    "VERNR": "IteItemResponsible 3",
                    "USR00": "IteFinancingType 3",
                    "USR01": "IteCSSCode 3",
                    "ZZ_NAPRD": "IteActivityDirection 3",
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
                    "PBUKR": "IteBUCode 4",
                    "POSID": "main test code 4",
                    "POST1": "IteItemName 4",
                    "ERDAT": "01.01.20",
                    "AEDAT": "31.12.21",
                    "VERNR": "IteItemResponsible 4",
                    "USR00": "IteFinancingType 4",
                    "USR01": "IteCSSCode 4",
                    "ZZ_NAPRD": "IteActivityDirection 4",
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
                    "PBUKR": "IteBUCode 2",
                    "POSID": "main test code 2",
                    "POST1": "IteItemName 2",
                    "ERDAT": "01.01.20",
                    "AEDAT": "31.12.21",
                    "VERNR": "IteItemResponsible 2",
                    "USR00": "IteFinancingType 2",
                    "USR01": "IteCSSCode 2",
                    "ZZ_NAPRD": "IteActivityDirection 2",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        assert obj['error'] == "Номер страницы превышает количество страниц", f"The value of 'MESSAGE' is not correct"
        assert obj['status'] == 400, f"The status is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "PBUKR")

    def test_null_pbukr_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "PBUKR": "",
                    "POSID": "main test code 5",
                    "POST1": "IteItemName 5",
                    "ERDAT": "01.01.20",
                    "AEDAT": "31.12.21",
                    "VERNR": "IteItemResponsible 5",
                    "USR00": "IteFinancingType 5",
                    "USR01": "IteCSSCode 5",
                    "ZZ_NAPRD": "IteActivityDirection 5",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - PBUKR", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "POSID")

    def test_null_posid_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "PBUKR": "IteBUCode 6",
                    "POSID": "",
                    "POST1": "IteItemName 6",
                    "ERDAT": "01.01.20",
                    "AEDAT": "31.12.21",
                    "VERNR": "IteItemResponsible 6",
                    "USR00": "IteFinancingType 6",
                    "USR01": "IteCSSCode 6",
                    "ZZ_NAPRD": "IteActivityDirection 6",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - POSID", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "VERNR")

    def test_null_vernr_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "PBUKR": "IteBUCode 10",
                    "POSID": "main test code 10",
                    "POST1": "IteItemName 10",
                    "ERDAT": "01.01.20",
                    "AEDAT": "31.12.21",
                    "VERNR": "",
                    "USR00": "IteFinancingType 10",
                    "USR01": "IteCSSCode 10",
                    "ZZ_NAPRD": "IteActivityDirection 10",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - VERNR", f"The value of 'MESSAGE' is not correct"
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
                    "PBUKR": "IteBUCode 2 (new)",
                    "POSID": "main test code 2",
                    "POST1": "IteItemName 2 (new)",
                    "ERDAT": "02.02.20",
                    "AEDAT": "30.11.21",
                    "VERNR": "IteItemResponsible 2 (new)",
                    "USR00": "IteFinancingType 2 (new)",
                    "USR01": "IteCSSCode 2 (new)",
                    "ZZ_NAPRD": "IteActivityDirection 2 (new)",
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
                    "PBUKR": "IteBUCode 2 (new)",
                    "POSID": "main test code 2",
                    "POST1": "IteItemName 2 (new)",
                    "ERDAT": "02.02.20",
                    "AEDAT": "30.11.21",
                    "VERNR": "IteItemResponsible 2 (new)",
                    "USR00": "IteFinancingType 2 (new)",
                    "USR01": "IteCSSCode 2 (new)",
                    "ZZ_NAPRD": "IteActivityDirection 2 (new)",
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
                    "PBUKR": "IteBUCode 3 (new)",
                    "POSID": "main test code 3",
                    "POST1": "IteItemName 3 (new)",
                    "ERDAT": "02.02.20",
                    "AEDAT": "30.11.21",
                    "VERNR": "IteItemResponsible 3 (new)",
                    "USR00": "IteFinancingType 3 (new)",
                    "USR01": "IteCSSCode 3 (new)",
                    "ZZ_NAPRD": "IteActivityDirection 3 (new)",
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
                    "PBUKR": "IteBUCode 3 (new)",
                    "POSID": "main test code 3",
                    "POST1": "IteItemName 3 (new)",
                    "ERDAT": "02.02.20",
                    "AEDAT": "30.11.21",
                    "VERNR": "IteItemResponsible 3 (new)",
                    "USR00": "IteFinancingType 3 (new)",
                    "USR01": "IteCSSCode 3 (new)",
                    "ZZ_NAPRD": "IteActivityDirection 3 (new)",
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
                    "PBUKR": "IteBUCode 3 (new)",
                    "POSID": "main test code 3",
                    "POST1": "IteItemName 3 (new)",
                    "ERDAT": "02.02.20",
                    "AEDAT": "30.11.21",
                    "VERNR": "IteItemResponsible 3 (new)",
                    "USR00": "IteFinancingType 3 (new)",
                    "USR01": "IteCSSCode 3 (new)",
                    "ZZ_NAPRD": "IteActivityDirection 3 (new)",
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
                    "PBUKR": "IteBUCode 3 (new)",
                    "POSID": "main test code 2",
                    "POST1": "IteItemName 3 (new)",
                    "ERDAT": "02.02.20",
                    "AEDAT": "30.11.21",
                    "VERNR": "IteItemResponsible 3 (new)",
                    "USR00": "IteFinancingType 3 (new)",
                    "USR01": "IteCSSCode 3 (new)",
                    "ZZ_NAPRD": "IteActivityDirection 3 (new)",
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
                    "PBUKR": "IteBUCode 3 (new)",
                    "POSID": "main test code 17",
                    "POST1": "IteItemName 3 (new)",
                    "ERDAT": "02.02.20",
                    "AEDAT": "30.11.21",
                    "VERNR": "IteItemResponsible 3 (new)",
                    "USR00": "IteFinancingType 3 (new)",
                    "USR01": "IteCSSCode 3 (new)",
                    "ZZ_NAPRD": "IteActivityDirection 3 (new)",
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
                    "PBUKR": "IteBUCode 3 (new)",
                    "POSID": "main test code 3",
                    "POST1": "IteItemName 3 (new)",
                    "ERDAT": "02.02.20",
                    "AEDAT": "30.11.21",
                    "VERNR": "IteItemResponsible 3 (new)",
                    "USR00": "IteFinancingType 3 (new)",
                    "USR01": "IteCSSCode 3 (new)",
                    "ZZ_NAPRD": "IteActivityDirection 3 (new)",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        assert obj['error'] == "Режим выгрузки справочника не идентифицирован", f"The value of 'MESSAGE' is not correct"



