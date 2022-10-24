import json
from my_lib.assertions import Assertion
from my_lib.my_requests import MyRequests
from my_lib.base_case import BaseCase


# python -m pytest -s tests\test_update_analytics_order.py -k test_correct_delta_f_demo


# Тестирование загрузки справочника "Значения аналитического признака "Заказ""

class TestUpdateAnalyticsOrder(BaseCase):

# Авторизация и получение необходимых cookie и headers

    def setup(self):
        env = 'http://localhost:83'
        auth_data = {
            "UserName": "Supervisor",
            "UserPassword": "Supervisor"
        }
        self.url = "http://localhost:83/0/rest/SapErpIntegrationService/v1/UpdateAnalyticsOrder"
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
                    "AUFNR": "main test code 1",
                    "AUART": "IteAOKind 1",
                    "ERNAM": "IteAOAuthor 1",
                    "ERDAT": "01.01.01",
                    "AENAM": "IteAOLastChangeAuthor 1",
                    "AEDAT": "01.01.01",
                    "KTEXT": "IteAOShortText 1",
                    "BUKRS": "IteBUCode 1",
                    "WERKS": "ItePlantCode 1",
                    "GSBER": "IteAOBusinessArea 1",
                    "KOKRS": "IteAOControllingUnit 1",
                    "KOSTV": "IteCSCode 1",
                    "STORT": "IteAOLocation 1",
                    "SOWRK": "IteAOPlantLocation 1",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 1",
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
                    "AUFNR": "main test code 2",
                    "AUART": "IteAOKind 2",
                    "ERNAM": "IteAOAuthor 2",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 2",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 2",
                    "BUKRS": "IteBUCode 2",
                    "WERKS": "ItePlantCode 2",
                    "GSBER": "IteAOBusinessArea 2",
                    "KOKRS": "IteAOControllingUnit 2",
                    "KOSTV": "IteCSCode 2",
                    "STORT": "IteAOLocation 2",
                    "SOWRK": "IteAOPlantLocation 2",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 2",
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
                    "AUFNR": "main test code 2",
                    "AUART": "IteAOKind 2",
                    "ERNAM": "IteAOAuthor 2",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 2",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 2",
                    "BUKRS": "IteBUCode 2",
                    "WERKS": "ItePlantCode 2",
                    "GSBER": "IteAOBusinessArea 2",
                    "KOKRS": "IteAOControllingUnit 2",
                    "KOSTV": "IteCSCode 2",
                    "STORT": "IteAOLocation 2",
                    "SOWRK": "IteAOPlantLocation 2",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 2",
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
                    "AUFNR": "main test code 3",
                    "AUART": "IteAOKind 3",
                    "ERNAM": "IteAOAuthor 3",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 3",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 3",
                    "BUKRS": "IteBUCode 3",
                    "WERKS": "ItePlantCode 3",
                    "GSBER": "IteAOBusinessArea 3",
                    "KOKRS": "IteAOControllingUnit 3",
                    "KOSTV": "IteCSCode 3",
                    "STORT": "IteAOLocation 3",
                    "SOWRK": "IteAOPlantLocation 3",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 3",
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
                    "AUFNR": "main test code 4",
                    "AUART": "IteAOKind 4",
                    "ERNAM": "IteAOAuthor 4",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 4",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 4",
                    "BUKRS": "IteBUCode 4",
                    "WERKS": "ItePlantCode 4",
                    "GSBER": "IteAOBusinessArea 4",
                    "KOKRS": "IteAOControllingUnit 4",
                    "KOSTV": "IteCSCode 4",
                    "STORT": "IteAOLocation 4",
                    "SOWRK": "IteAOPlantLocation 4",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 4",
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
                    "AUFNR": "main test code 2",
                    "AUART": "IteAOKind 2",
                    "ERNAM": "IteAOAuthor 2",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 2",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 2",
                    "BUKRS": "IteBUCode 2",
                    "WERKS": "ItePlantCode 2",
                    "GSBER": "IteAOBusinessArea 2",
                    "KOKRS": "IteAOControllingUnit 2",
                    "KOSTV": "IteCSCode 2",
                    "STORT": "IteAOLocation 2",
                    "SOWRK": "IteAOPlantLocation 2",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 2",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        assert obj['error'] == "Номер страницы превышает количество страниц", f"The value of 'MESSAGE' is not correct"
        assert obj['status'] == 400, f"The status is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "AUFNR")

    def test_null_aufnr_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "",
                    "AUART": "IteAOKind 5",
                    "ERNAM": "IteAOAuthor 5",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 5",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 5",
                    "BUKRS": "IteBUCode 5",
                    "WERKS": "ItePlantCode 5",
                    "GSBER": "IteAOBusinessArea 5",
                    "KOKRS": "IteAOControllingUnit 5",
                    "KOSTV": "IteCSCode 5",
                    "STORT": "IteAOLocation 5",
                    "SOWRK": "IteAOPlantLocation 5",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 5",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - AUFNR", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "AUART")

    def test_null_auart_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 6",
                    "AUART": "",
                    "ERNAM": "IteAOAuthor 6",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 6",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 6",
                    "BUKRS": "IteBUCode 6",
                    "WERKS": "ItePlantCode 6",
                    "GSBER": "IteAOBusinessArea 6",
                    "KOKRS": "IteAOControllingUnit 6",
                    "KOSTV": "IteCSCode 6",
                    "STORT": "IteAOLocation 6",
                    "SOWRK": "IteAOPlantLocation 6",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 6",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - AUART", f"The value of 'MESSAGE' is not correct"
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
                    "AUFNR": "main test code 12",
                    "AUART": "IteAOKind 12",
                    "ERNAM": "IteAOAuthor 12",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 12",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 12",
                    "BUKRS": "",
                    "WERKS": "ItePlantCode 12",
                    "GSBER": "IteAOBusinessArea 12",
                    "KOKRS": "IteAOControllingUnit 12",
                    "KOSTV": "IteCSCode 12",
                    "STORT": "IteAOLocation 12",
                    "SOWRK": "IteAOPlantLocation 12",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 12",
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
                    "AUFNR": "main test code 2",
                    "AUART": "IteAOKind 2 (new)",
                    "ERNAM": "IteAOAuthor 2 (new)",
                    "ERDAT": "02.02.20",
                    "AENAM": "IteAOLastChangeAuthor 2 (new)",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 2 (new)",
                    "BUKRS": "IteBUCode 2 (new)",
                    "WERKS": "ItePlantCode 2 (new)",
                    "GSBER": "IteAOBusinessArea 2 (new)",
                    "KOKRS": "IteAOControllingUnit 2 (new)",
                    "KOSTV": "IteCSCode 2 (new)",
                    "STORT": "IteAOLocation 2 (new)",
                    "SOWRK": "IteAOPlantLocation 2 (new)",
                    "ASTKZ": "0",
                    "PHAS0": "0",
                    "PHAS1": "0",
                    "PHAS2": "0",
                    "PHAS3": "0",
                    "CYCLE": "IteRealEntryCSCode 2 (new)",
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
                    "AUFNR": "main test code 2",
                    "AUART": "IteAOKind 2 (new)",
                    "ERNAM": "IteAOAuthor 2 (new)",
                    "ERDAT": "02.02.20",
                    "AENAM": "IteAOLastChangeAuthor 2 (new)",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 2 (new)",
                    "BUKRS": "IteBUCode 2 (new)",
                    "WERKS": "ItePlantCode 2 (new)",
                    "GSBER": "IteAOBusinessArea 2 (new)",
                    "KOKRS": "IteAOControllingUnit 2 (new)",
                    "KOSTV": "IteCSCode 2 (new)",
                    "STORT": "IteAOLocation 2 (new)",
                    "SOWRK": "IteAOPlantLocation 2 (new)",
                    "ASTKZ": "0",
                    "PHAS0": "0",
                    "PHAS1": "0",
                    "PHAS2": "0",
                    "PHAS3": "0",
                    "CYCLE": "IteRealEntryCSCode 2 (new)",
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
                    "AUFNR": "main test code 3",
                    "AUART": "IteAOKind 3 (new)",
                    "ERNAM": "IteAOAuthor 3 (new)",
                    "ERDAT": "02.02.20",
                    "AENAM": "IteAOLastChangeAuthor 3 (new)",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "WERKS": "ItePlantCode 3 (new)",
                    "GSBER": "IteAOBusinessArea 3 (new)",
                    "KOKRS": "IteAOControllingUnit 3 (new)",
                    "KOSTV": "IteCSCode 3 (new)",
                    "STORT": "IteAOLocation 3 (new)",
                    "SOWRK": "IteAOPlantLocation 3 (new)",
                    "ASTKZ": "0",
                    "PHAS0": "1",
                    "PHAS1": "0",
                    "PHAS2": "1",
                    "PHAS3": "0",
                    "CYCLE": "IteRealEntryCSCode 3 (new)",
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
                    "AUFNR": "main test code 3",
                    "AUART": "IteAOKind 3 (new)",
                    "ERNAM": "IteAOAuthor 3 (new)",
                    "ERDAT": "02.02.20",
                    "AENAM": "IteAOLastChangeAuthor 3 (new)",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "WERKS": "ItePlantCode 3 (new)",
                    "GSBER": "IteAOBusinessArea 3 (new)",
                    "KOKRS": "IteAOControllingUnit 3 (new)",
                    "KOSTV": "IteCSCode 3 (new)",
                    "STORT": "IteAOLocation 3 (new)",
                    "SOWRK": "IteAOPlantLocation 3 (new)",
                    "ASTKZ": "0",
                    "PHAS0": "1",
                    "PHAS1": "0",
                    "PHAS2": "1",
                    "PHAS3": "0",
                    "CYCLE": "IteRealEntryCSCode 3 (new)",
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
                    "AUFNR": "main test code 3",
                    "AUART": "IteAOKind 3 (new)",
                    "ERNAM": "IteAOAuthor 3 (new)",
                    "ERDAT": "02.02.20",
                    "AENAM": "IteAOLastChangeAuthor 3 (new)",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "WERKS": "ItePlantCode 3 (new)",
                    "GSBER": "IteAOBusinessArea 3 (new)",
                    "KOKRS": "IteAOControllingUnit 3 (new)",
                    "KOSTV": "IteCSCode 3 (new)",
                    "STORT": "IteAOLocation 3 (new)",
                    "SOWRK": "IteAOPlantLocation 3 (new)",
                    "ASTKZ": "0",
                    "PHAS0": "1",
                    "PHAS1": "0",
                    "PHAS2": "1",
                    "PHAS3": "0",
                    "CYCLE": "IteRealEntryCSCode 3 (new)",
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
                    "AUFNR": "main test code 4",
                    "AUART": "IteAOKind 3 (new)",
                    "ERNAM": "IteAOAuthor 3 (new)",
                    "ERDAT": "02.02.20",
                    "AENAM": "IteAOLastChangeAuthor 3 (new)",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "WERKS": "ItePlantCode 3 (new)",
                    "GSBER": "IteAOBusinessArea 3 (new)",
                    "KOKRS": "IteAOControllingUnit 3 (new)",
                    "KOSTV": "IteCSCode 3 (new)",
                    "STORT": "IteAOLocation 3 (new)",
                    "SOWRK": "IteAOPlantLocation 3 (new)",
                    "ASTKZ": "0",
                    "PHAS0": "1",
                    "PHAS1": "0",
                    "PHAS2": "1",
                    "PHAS3": "0",
                    "CYCLE": "IteRealEntryCSCode 3 (new)",
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
                    "AUFNR": "main test code 33",
                    "AUART": "IteAOKind 3 (new)",
                    "ERNAM": "IteAOAuthor 3 (new)",
                    "ERDAT": "02.02.20",
                    "AENAM": "IteAOLastChangeAuthor 3 (new)",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "WERKS": "ItePlantCode 3 (new)",
                    "GSBER": "IteAOBusinessArea 3 (new)",
                    "KOKRS": "IteAOControllingUnit 3 (new)",
                    "KOSTV": "IteCSCode 3 (new)",
                    "STORT": "IteAOLocation 3 (new)",
                    "SOWRK": "IteAOPlantLocation 3 (new)",
                    "ASTKZ": "0",
                    "PHAS0": "1",
                    "PHAS1": "0",
                    "PHAS2": "1",
                    "PHAS3": "0",
                    "CYCLE": "IteRealEntryCSCode 3 (new)",
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
                    "AUFNR": "main test code 3",
                    "AUART": "IteAOKind 3 (new)",
                    "ERNAM": "IteAOAuthor 3 (new)",
                    "ERDAT": "02.02.20",
                    "AENAM": "IteAOLastChangeAuthor 3 (new)",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "WERKS": "ItePlantCode 3 (new)",
                    "GSBER": "IteAOBusinessArea 3 (new)",
                    "KOKRS": "IteAOControllingUnit 3 (new)",
                    "KOSTV": "IteCSCode 3 (new)",
                    "STORT": "IteAOLocation 3 (new)",
                    "SOWRK": "IteAOPlantLocation 3 (new)",
                    "ASTKZ": "0",
                    "PHAS0": "1",
                    "PHAS1": "0",
                    "PHAS2": "1",
                    "PHAS3": "0",
                    "CYCLE": "IteRealEntryCSCode 3 (new)",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        assert obj['error'] == "Режим выгрузки справочника не идентифицирован", f"The value of 'MESSAGE' is not correct"



