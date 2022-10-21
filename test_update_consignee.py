

import json
from my_lib.assertions import Assertion
from my_lib.my_requests import MyRequests
from my_lib.base_case import BaseCase


# python -m pytest -s tests\test_update_consignee.py -k test_correct_delta_f_demo


# Тестирование загрузки справочника "Значения аналитического признака "Заказ""

class TestUpdateConsignee(BaseCase):

# Авторизация и получение необходимых cookie и headers

    def setup(self):
        env = 'http://localhost:83'
        auth_data = {
            "UserName": "Supervisor",
            "UserPassword": "Supervisor"
        }
        self.url = "http://localhost:83/0/rest/SapErpIntegrationService/v1/UpdateConsignee"
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
         "AUFNR":"main test code 1",
         "AUART":"IteAOKind 1",
         "ERNAM":"IteAOAuthor 1",
         "ERDAT":"01.01.01",
         "AENAM":"IteAOLastChangeAuthor 1",
         "AEDAT":"01.01.01",
         "KTEXT":"IteAOShortText 1",
         "BUKRS":"IteBUCode 1",
         "WERKS":"ItePlantCode 1",
         "GSBER":"IteAOBusinessArea 1",
         "KOKRS":"IteAOControllingUnit 1",
         "KOSTV":"IteCSCode 1",
         "STORT":"IteAOLocation 1",
         "SOWRK":"IteAOPlantLocation 1",
         "ASTKZ":"1",
         "PHAS0":"1",
         "PHAS1":"1",
         "PHAS2":"1",
         "PHAS3":"1",
         "CYCLE":"IteRealEntryCSCode 1",
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
                    "BUKRS": "iteCodeBU 1",
                    "KUNNR": "iteCodePartner 1",
                    "KUNNP": "main test code 1",
                    "LAND1": "iteCodeCountry 1",
                    "NAME1": "iteName 1",
                    "NAME2": "iteName 2",
                    "ORT01": "iteCity 1",
                    "PSTLZ": "itePostalCode 1",
                    "STRAS": "iteAddress 1",
                    "STCD1": "iteINN 1",
                    "STCD3": "iteKPP 1",
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
                    "BUKRS": "iteCodeBU 2",
                    "KUNNR": "iteCodePartner 2",
                    "KUNNP": "main test code 2",
                    "LAND1": "iteCodeCountry 2",
                    "NAME1": "iteName 2",
                    "NAME2": "iteName 2",
                    "ORT01": "iteCity 2",
                    "PSTLZ": "itePostalCode 2",
                    "STRAS": "iteAddress 2",
                    "STCD1": "iteINN 2",
                    "STCD3": "iteKPP 2",
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
                    "BUKRS": "iteCodeBU 2",
                    "KUNNR": "iteCodePartner 2",
                    "KUNNP": "main test code 2",
                    "LAND1": "iteCodeCountry 2",
                    "NAME1": "iteName 2",
                    "NAME2": "iteName 2",
                    "ORT01": "iteCity 2",
                    "PSTLZ": "itePostalCode 2",
                    "STRAS": "iteAddress 2",
                    "STCD1": "iteINN 2",
                    "STCD3": "iteKPP 2",
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
                    "BUKRS": "iteCodeBU 3",
                    "KUNNR": "iteCodePartner 3",
                    "KUNNP": "main test code 3",
                    "LAND1": "iteCodeCountry 3",
                    "NAME1": "iteName 3",
                    "NAME2": "iteName 3",
                    "ORT01": "iteCity 3",
                    "PSTLZ": "itePostalCode 3",
                    "STRAS": "iteAddress 3",
                    "STCD1": "iteINN 3",
                    "STCD3": "iteKPP 3",
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
                    "BUKRS": "iteCodeBU 4",
                    "KUNNR": "iteCodePartner 4",
                    "KUNNP": "main test code 4",
                    "LAND1": "iteCodeCountry 4",
                    "NAME1": "iteName 4",
                    "NAME2": "iteName 4",
                    "ORT01": "iteCity 4",
                    "PSTLZ": "itePostalCode 4",
                    "STRAS": "iteAddress 4",
                    "STCD1": "iteINN 4",
                    "STCD3": "iteKPP 4",
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
                    "BUKRS": "iteCodeBU 2",
                    "KUNNR": "iteCodePartner 2",
                    "KUNNP": "main test code 2",
                    "LAND1": "iteCodeCountry 2",
                    "NAME1": "iteName 2",
                    "NAME2": "iteName 2",
                    "ORT01": "iteCity 2",
                    "PSTLZ": "itePostalCode 2",
                    "STRAS": "iteAddress 2",
                    "STCD1": "iteINN 2",
                    "STCD3": "iteKPP 2",
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
                    "KUNNR": "iteCodePartner 5",
                    "KUNNP": "main test code 5",
                    "LAND1": "iteCodeCountry 5",
                    "NAME1": "iteName 5",
                    "NAME2": "iteName 5",
                    "ORT01": "iteCity 5",
                    "PSTLZ": "itePostalCode 5",
                    "STRAS": "iteAddress 5",
                    "STCD1": "iteINN 5",
                    "STCD3": "iteKPP 5",
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

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "KUNNR")

    def test_null_kunnr_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "BUKRS": "iteCodeBU 6",
                    "KUNNR": "",
                    "KUNNP": "main test code 6",
                    "LAND1": "iteCodeCountry 6",
                    "NAME1": "iteName 6",
                    "NAME2": "iteName 6",
                    "ORT01": "iteCity 6",
                    "PSTLZ": "itePostalCode 6",
                    "STRAS": "iteAddress 6",
                    "STCD1": "iteINN 6",
                    "STCD3": "iteKPP 6",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - KUNNR", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "KUNNP")

    def test_null_kunnp_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "BUKRS": "iteCodeBU 7",
                    "KUNNR": "iteCodePartner 7",
                    "KUNNP": "",
                    "LAND1": "iteCodeCountry 7",
                    "NAME1": "iteName 7",
                    "NAME2": "iteName 7",
                    "ORT01": "iteCity 7",
                    "PSTLZ": "itePostalCode 7",
                    "STRAS": "iteAddress 7",
                    "STCD1": "iteINN 7",
                    "STCD3": "iteKPP 7",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - KUNNP", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Загрузка уже существующей записи (изменение записи) в режиме полной выгрузки (delta = "F") корректный запрос

    def test_changing_an_existing_record_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "2",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "BUKRS": "iteCodeBU 1 (new)",
                    "KUNNR": "iteCodePartner 1 (new)",
                    "KUNNP": "main test code 1",
                    "LAND1": "iteCodeCountry 1 (new)",
                    "NAME1": "iteName 1 (new)",
                    "NAME2": "iteName 1 (new)",
                    "ORT01": "iteCity 1 (new)",
                    "PSTLZ": "itePostalCode 1 (new)",
                    "STRAS": "iteAddress 1 (new)",
                    "STCD1": "iteINN 1 (new)",
                    "STCD3": "iteKPP 1 (new)",
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
            "pageCount": "2",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "BUKRS": "iteCodeBU 1 (new)",
                    "KUNNR": "iteCodePartner 1 (new)",
                    "KUNNP": "main test code 1",
                    "LAND1": "iteCodeCountry 1 (new)",
                    "NAME1": "iteName 1 (new)",
                    "NAME2": "iteName 1 (new)",
                    "ORT01": "iteCity 1 (new)",
                    "PSTLZ": "itePostalCode 1 (new)",
                    "STRAS": "iteAddress 1 (new)",
                    "STCD1": "iteINN 1 (new)",
                    "STCD3": "iteKPP 1 (new)",
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
                    "BUKRS": "iteCodeBU 3 (new)",
                    "KUNNR": "iteCodePartner 3 (new)",
                    "KUNNP": "main test code 3",
                    "LAND1": "iteCodeCountry 3 (new)",
                    "NAME1": "iteName 3 (new)",
                    "NAME2": "iteName 3 (new)",
                    "ORT01": "iteCity 3 (new)",
                    "PSTLZ": "itePostalCode 3 (new)",
                    "STRAS": "iteAddress 3 (new)",
                    "STCD1": "iteINN 3 (new)",
                    "STCD3": "iteKPP 3 (new)",
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
                    "BUKRS": "iteCodeBU 3 (new)",
                    "KUNNR": "iteCodePartner 3 (new)",
                    "KUNNP": "main test code 3",
                    "LAND1": "iteCodeCountry 3 (new)",
                    "NAME1": "iteName 3 (new)",
                    "NAME2": "iteName 3 (new)",
                    "ORT01": "iteCity 3 (new)",
                    "PSTLZ": "itePostalCode 3 (new)",
                    "STRAS": "iteAddress 3 (new)",
                    "STCD1": "iteINN 3 (new)",
                    "STCD3": "iteKPP 3 (new)",
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
                    "BUKRS": "iteCodeBU 3 (new)",
                    "KUNNR": "iteCodePartner 3 (new)",
                    "KUNNP": "main test code 3",
                    "LAND1": "iteCodeCountry 3 (new)",
                    "NAME1": "iteName 3 (new)",
                    "NAME2": "iteName 3 (new)",
                    "ORT01": "iteCity 3 (new)",
                    "PSTLZ": "itePostalCode 3 (new)",
                    "STRAS": "iteAddress 3 (new)",
                    "STCD1": "iteINN 3 (new)",
                    "STCD3": "iteKPP 3 (new)",
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
                    "BUKRS": "iteCodeBU 3 (new)",
                    "KUNNR": "iteCodePartner 3 (new)",
                    "KUNNP": "main test code 2",
                    "LAND1": "iteCodeCountry 3 (new)",
                    "NAME1": "iteName 3 (new)",
                    "NAME2": "iteName 3 (new)",
                    "ORT01": "iteCity 3 (new)",
                    "PSTLZ": "itePostalCode 3 (new)",
                    "STRAS": "iteAddress 3 (new)",
                    "STCD1": "iteINN 3 (new)",
                    "STCD3": "iteKPP 3 (new)",
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
                    "BUKRS": "iteCodeBU 3 (new)",
                    "KUNNR": "iteCodePartner 3 (new)",
                    "KUNNP": "main test code 25",
                    "LAND1": "iteCodeCountry 3 (new)",
                    "NAME1": "iteName 3 (new)",
                    "NAME2": "iteName 3 (new)",
                    "ORT01": "iteCity 3 (new)",
                    "PSTLZ": "itePostalCode 3 (new)",
                    "STRAS": "iteAddress 3 (new)",
                    "STCD1": "iteINN 3 (new)",
                    "STCD3": "iteKPP 3 (new)",
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
                    "BUKRS": "iteCodeBU 3 (new)",
                    "KUNNR": "iteCodePartner 3 (new)",
                    "KUNNP": "main test code 3",
                    "LAND1": "iteCodeCountry 3 (new)",
                    "NAME1": "iteName 3 (new)",
                    "NAME2": "iteName 3 (new)",
                    "ORT01": "iteCity 3 (new)",
                    "PSTLZ": "itePostalCode 3 (new)",
                    "STRAS": "iteAddress 3 (new)",
                    "STCD1": "iteINN 3 (new)",
                    "STCD3": "iteKPP 3 (new)",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        assert obj['error'] == "Режим выгрузки справочника не идентифицирован", f"The value of 'MESSAGE' is not correct"



