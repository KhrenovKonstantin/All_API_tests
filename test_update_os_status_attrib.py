import json
from my_lib.assertions import Assertion
from my_lib.my_requests import MyRequests
from my_lib.base_case import BaseCase
import allure

# python -m pytest -s test_update_os_status_attrib.py -k Test_update_osk
# py.test --alluredir=allure_result_folder ./test_update_os_status_attrib.py
# allure serve allure_result_folder

@allure.epic("Актуализация атрибутов и статусов ОС ")
class Test_update_osk(BaseCase):

    # Авторизация и получение необходимых cookie и headers
    @allure.description('Авторизация и получение необходимых cookie и headers')
    def setup(self):
        env = 'http://localmail.itexpert.ru:5058'
        auth_data = {
            "UserName": "Supervisor",
            "UserPassword": "!Supervisor123Test!"
        }
        self.url = "http://localmail.itexpert.ru:5058/rest/SapErpIntegrationService/v1/UpdateOSDirectory"
        self.jar, self.header = MyRequests.user_auth(self, auth_data, env)

    @allure.description('Актуализация атрибутов и статусов ОС')
    def test_first_responce(self):
        json_data = {
            "currentPage": 1,
            "pageCount": 1,
            "delta": "F",
            "item": [
                {
                    "ANLN1": "240000240179",
                    "TXT50": "Аппарат телефонный Cisco/CP-7945G=13",
                    "INVNR": "12121313",
                    "AKTIV": "29.03.2016",
                    "KOSTL": "1006103050",
                    "WERKS": "1002",
                    "STORT": "43",
                    "ANSW_END": "20000.00",
                    "RBW_END": "10000",
                    "MENGE": "2",
                    "POSNR": "1100648.80016-YO04-00013",
                    "GLO_RUS_OKOF16": "330.28.12",
                    "GLO_RUS_DEPGRN": "03",
                    "NDJAR": "003",
                    "DEAKT": "13.02.2023",
                    "KTEXT3": "г.Санкт-Петербург ул.Почтамтская 3-5",
                    "ZZCNDPERNR": "00028076",
                    "CNDPERNR_NAME": "Дернов ИН123",
                    "OS_STATUS": "Активен",
                    "AWKEY": "09072021/2",
                    "GJAHR": "2021",
                    "ACT-ID": "pre09072021/2",
                    "SERNR": "666",
                    "row": 1,
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] != "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", result['MESSAGE']
            print(result['MESSAGE'])
        #assert obj['MESSAGE'] != None, f"The value of 'message' is not correct"
        #assert obj['error'] is None, obj['error']

    @allure.description('Актуализация атрибутов и статусов ОС (Не заполнен обязательный атрибут "Инвентарный номер")')
    def test_second_responce(self):
        json_data = {
            "currentPage": 1,
            "pageCount": 1,
            "delta": "F",
            "item": [
                {
                    "ANLN1": "240000240179",
                    "TXT50": "Аппарат телефонный Cisco/CP-7945G=13",
                    "INVNR": None,
                    "AKTIV": "29.03.2016",
                    "KOSTL": "1006103050",
                    "WERKS": "1002",
                    "STORT": "43",
                    "ANSW_END": "20000.00",
                    "RBW_END": "10000",
                    "MENGE": "2",
                    "POSNR": "1100648.80016-YO04-00013",
                    "GLO_RUS_OKOF16": "330.28.12",
                    "GLO_RUS_DEPGRN": "03",
                    "NDJAR": "003",
                    "DEAKT": "13.02.2023",
                    "KTEXT3": "г.Санкт-Петербург ул.Почтамтская 3-5",
                    "ZZCNDPERNR": "00028076",
                    "CNDPERNR_NAME": "Дернов ИН123",
                    "OS_STATUS": "Активен",
                    "AWKEY": "09072021/2",
                    "GJAHR": "2021",
                    "ACT-ID": "pre09072021/2",
                    "SERNR": "123йцу123йу1",
                    "row": 1,
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] != "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", result['MESSAGE']
            print(result['MESSAGE'])
        #assert obj['MESSAGE'] != None, f"The value of 'message' is not correct"
        #assert obj['error'] is None, obj['error']


    @allure.description('Актуализация атрибутов и статусов ОС (Инвентарный номер не найден в КСУИТ)')
    def test_three_responce(self):
        json_data = {
            "currentPage": 1,
            "pageCount": 1,
            "delta": "F",
            "item": [
                {
                    "ANLN1": "240000240179",
                    "TXT50": "Аппарат телефонный Cisco/CP-7945G=13",
                    "INVNR": "",
                    "AKTIV": "29.03.2016",
                    "KOSTL": "1006103050",
                    "WERKS": "1002",
                    "STORT": "43",
                    "ANSW_END": "20000.00",
                    "RBW_END": "10000",
                    "MENGE": "2",
                    "POSNR": "1100648.80016-YO04-00013",
                    "GLO_RUS_OKOF16": "330.28.12",
                    "GLO_RUS_DEPGRN": "03",
                    "NDJAR": "003",
                    "DEAKT": "13.02.2023",
                    "KTEXT3": "г.Санкт-Петербург ул.Почтамтская 3-5",
                    "ZZCNDPERNR": "00028076",
                    "CNDPERNR_NAME": "Дернов ИН123",
                    "OS_STATUS": "Активен",
                    "AWKEY": "09072021/2",
                    "GJAHR": "2021",
                    "ACT-ID": "pre09072021/2",
                    "SERNR": "123йцу123йу1",
                    "row": 1,
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] != "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", result['MESSAGE']
        #assert obj['MESSAGE'] != None, f"The value of 'message' is not correct"
        #assert obj['error'] is None, obj['error']


    @allure.description('Актуализация атрибутов и статусов ОС (МВЗ не найдено в КСУИТ)')
    def test_foo_responce(self):
        json_data = {
            "currentPage": 1,
            "pageCount": 1,
            "delta": "F",
            "item": [
                {
                    "ANLN1": "240000240179",
                    "TXT50": "Аппарат телефонный Cisco/CP-7945G=13",
                    "INVNR": "12121313",
                    "AKTIV": "29.03.2016",
                    "KOSTL": "1006103088",
                    "WERKS": "1002",
                    "STORT": "43",
                    "ANSW_END": "20000.00",
                    "RBW_END": "10000",
                    "MENGE": "2",
                    "POSNR": "1100648.80016-YO04-00013",
                    "GLO_RUS_OKOF16": "330.28.12",
                    "GLO_RUS_DEPGRN": "03",
                    "NDJAR": "003",
                    "DEAKT": "13.02.2023",
                    "KTEXT3": "г.Санкт-Петербург ул.Почтамтская 3-5",
                    "ZZCNDPERNR": "00028076",
                    "CNDPERNR_NAME": "Дернов ИН123",
                    "OS_STATUS": "Активен",
                    "AWKEY": "09072021/2",
                    "GJAHR": "2021",
                    "ACT-ID": "pre09072021/2",
                    "SERNR": "123йцу123йу1",
                    "row": 1,
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] != "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", result['MESSAGE']
        #assert obj['MESSAGE'] != None, f"The value of 'message' is not correct"
        #assert obj['error'] is None, obj['error']


    @allure.description('Актуализация атрибутов и статусов ОС (СПП-элемент не найден в КСУИТ)')
    def test_five_responce(self):
        json_data = {
            "currentPage": 1,
            "pageCount": 1,
            "delta": "F",
            "item": [
                {
                    "ANLN1": "240000240179",
                    "TXT50": "Аппарат телефонный Cisco/CP-7945G=13",
                    "INVNR": "12121313",
                    "AKTIV": "29.03.2016",
                    "KOSTL": "1006103050",
                    "WERKS": "1002",
                    "STORT": "43",
                    "ANSW_END": "20000.00",
                    "RBW_END": "10000",
                    "MENGE": "2",
                    "POSNR": "1100648.80016-YO04-00011",
                    "GLO_RUS_OKOF16": "330.28.12",
                    "GLO_RUS_DEPGRN": "03",
                    "NDJAR": "003",
                    "DEAKT": "13.02.2023",
                    "KTEXT3": "г.Санкт-Петербург ул.Почтамтская 3-5",
                    "ZZCNDPERNR": "00028076",
                    "CNDPERNR_NAME": "Дернов ИН123",
                    "OS_STATUS": "Активен",
                    "AWKEY": "09072021/2",
                    "GJAHR": "2021",
                    "ACT-ID": "pre09072021/2",
                    "SERNR": "123йцу123йу1",
                    "row": 1,
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] != "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", result['MESSAGE']
        #assert obj['MESSAGE'] != None, f"The value of 'message' is not correct"
        #assert obj['error'] is None, obj['error']


    @allure.description('Актуализация атрибутов и статусов ОС (не найден в КСУИТ)')
    def test_six_responce(self):
        json_data = {
            "currentPage": 1,
            "pageCount": 1,
            "delta": "F",
            "item": [
                {
                    "ANLN1": "240000240179",
                    "TXT50": "Аппарат телефонный Cisco/CP-7945G=13",
                    "INVNR": "12121313",
                    "AKTIV": "29.03.2016",
                    "KOSTL": "1006103050",
                    "WERKS": "1002",
                    "STORT": "43",
                    "ANSW_END": "20000.00",
                    "RBW_END": "10000",
                    "MENGE": "2",
                    "POSNR": "1100648.80016-YO04-00013",
                    "GLO_RUS_OKOF16": "330.28.12",
                    "GLO_RUS_DEPGRN": "03",
                    "NDJAR": "003",
                    "DEAKT": "13.02.2023",
                    "KTEXT3": "г.Санкт-Петербург ул.Почтамтская 3-5",
                    "ZZCNDPERNR": "00028076",
                    "CNDPERNR_NAME": "Дернов ИН123",
                    "OS_STATUS": "Активе",
                    "AWKEY": "09072021/2",
                    "GJAHR": "2021",
                    "ACT-ID": "pre09072021/2",
                    "SERNR": "123йцу123йу1",
                    "row": 1,
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] != "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", result['MESSAGE']
        #assert obj['MESSAGE'] != None, f"The value of 'message' is not correct"
        #assert obj['error'] is None, obj['error']


    @allure.description('Актуализация атрибутов и статусов ОС (Номер страницы превышает количество страниц)')
    def test_seven_responce(self):
        json_data = {
            "currentPage": 2,
            "pageCount": 1,
            "delta": "F",
            "item": [
                {
                    "ANLN1": "240000240179",
                    "TXT50": "Аппарат телефонный Cisco/CP-7945G=13",
                    "INVNR": "12121313",
                    "AKTIV": "29.03.2016",
                    "KOSTL": "1006103050",
                    "WERKS": "1002",
                    "STORT": "43",
                    "ANSW_END": "20000.00",
                    "RBW_END": "10000",
                    "MENGE": "2",
                    "POSNR": "1100648.80016-YO04-00013",
                    "GLO_RUS_OKOF16": "330.28.12",
                    "GLO_RUS_DEPGRN": "03",
                    "NDJAR": "003",
                    "DEAKT": "13.02.2023",
                    "KTEXT3": "г.Санкт-Петербург ул.Почтамтская 3-5",
                    "ZZCNDPERNR": "00028076",
                    "CNDPERNR_NAME": "Дернов ИН123",
                    "OS_STATUS": "Активен",
                    "AWKEY": "09072021/2",
                    "GJAHR": "2021",
                    "ACT-ID": "pre09072021/2",
                    "SERNR": "123йцу123йу1",
                    "row": 1,
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        assert obj['status'] == "200", obj['error']
        #assert obj['MESSAGE'] != None, f"The value of 'message' is not correct"
        #assert obj['error'] is None, obj['error']

    @allure.description('Актуализация атрибутов и статусов ОС, item.OS_STATUS == Перемещен и item.DEAKT не пусто')
    def test_eith_responce(self):
        json_data = {
            "currentPage": 1,
            "pageCount": 1,
            "delta": "F",
            "item": [
                {
                    "ANLN1": "240000240179",
                    "TXT50": "Аппарат телефонный Cisco/CP-7945G=13",
                    "INVNR": "12121313",
                    "AKTIV": "29.03.2016",
                    "KOSTL": "1006103050",
                    "WERKS": "1002",
                    "STORT": "43",
                    "ANSW_END": "20000.00",
                    "RBW_END": "10000",
                    "MENGE": "2",
                    "POSNR": "1100648.80016-YO04-00013",
                    "GLO_RUS_OKOF16": "330.28.12",
                    "GLO_RUS_DEPGRN": "03",
                    "NDJAR": "003",
                    "DEAKT": "13.02.2023",
                    "KTEXT3": "г.Санкт-Петербург ул.Почтамтская 3-5",
                    "ZZCNDPERNR": "00028076",
                    "CNDPERNR_NAME": "Дернов ИН123",
                    "OS_STATUS": "Перемещен",
                    "AWKEY": "09072021/2",
                    "GJAHR": "2021",
                    "ACT-ID": "pre09072021/2",
                    "SERNR": "666",
                    "row": 1,
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] != "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", result['MESSAGE']
            print(result['MESSAGE'])