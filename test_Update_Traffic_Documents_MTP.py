import json
from my_lib.assertions import Assertion
from my_lib.my_requests import MyRequests
from my_lib.base_case import BaseCase


# python -m pytest -s tests\test_Update_Traffic_Documents_MTP.py -k test_correct_delta_f_demo


# Тестирование загрузки справочника "Виды затрат"

class TestUpdateTrafficDocumentsMTP(BaseCase):

# Авторизация и получение необходимых cookie и headers

    def setup(self):
        env = 'http://localhost:83'
        auth_data = {
            "UserName": "Supervisor",
            "UserPassword": "Supervisor"
        }
        self.url = "http://localhost:83/0/rest/SapErpIntegrationService/v1/UpdateTrafficDocumentsMTP"
        self.jar, self.header = MyRequests.user_auth(self, auth_data, env)



# Загрузка запсиси с незаполненным полем "BWART"

    def test_bwart_is_null_delta_f(self):
        test_name = 'Загрузка справочника в режиме полной выгрузки (delta = "F") корректный запрос'
        json_data = {
            "currentPage": 1,
            "pageCount": 1,
            "delta": "D",
            "item": [
                {
                    "row": 1,
                    "EBELN_IT": "null",
                    "EBELP_IT": 0,
                    "MBLNR": "5003138828",
                    "MJAHR": 2021,
                    "VGART": "WE",
                    "BLART": "WE",
                    "BUDAT": "2021-05-16",
                    "ZEILE": 1,
                    "BWART": "",
                    "WERKS": "1001",
                    "LGORT": "3004",
                    "CHARG": "0006678068",
                    "ZZ_KLASS": "0800",
                    "MATNR": "000000770000150513",
                    "MENGE": 100,
                    "MEINS": "KT",
                    "ERFMG": 100,
                    "ERFME": "KT",
                    "LIFNR": "0000022204",
                    "EBELN": "test3",
                    "BSART": "ZSZ",
                    "EBELP": "12345",
                    "UMWRK": "test",
                    "UMLGO": "test",
                    "PS_PSP_PNR": "010099.000.RE-33-0000-02",
                    "FISTL": "100204000",
                    "GEBER": "NOPROJECT",
                    "FIPOS": "2020203",
                    "ANLN1": "test",
                    "KOSTL": "test",
                    "AUFNR": "test",
                    "SMBLN": "test",
                    "DMBTR": 5000000,
                    "XBLNR_MKPF": "0180546478",
                    "ARC_DOC_ID": "test",
                    "ACT-ID": "test",
                    "ACT_POS": 0,
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == 'Не заполнен обязательный атрибут "Вид операции"', f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Загрузка записи с неизвестным атрибутом "Вид операции" BWART != 101 (ИЛИ 941 ИЛИ 291 ИЛИ 261)
    def test_uncorrect_bwart(self):
        test_name = 'Загрузка записи с неизвестным атрибутом "Вид операции" BWART != 101 (ИЛИ 941 ИЛИ 291 ИЛИ 261)'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": 1,
                    "EBELN_IT": "null",
                    "EBELP_IT": 0,
                    "MBLNR": "5003138828",
                    "MJAHR": 2021,
                    "VGART": "WE",
                    "BLART": "WE",
                    "BUDAT": "2021-05-16",
                    "ZEILE": 1,
                    "BWART": 567,
                    "WERKS": "1001",
                    "LGORT": "3004",
                    "CHARG": "0006678068",
                    "ZZ_KLASS": "0800",
                    "MATNR": "000000770000150513",
                    "MENGE": 100,
                    "MEINS": "KT",
                    "ERFMG": 100,
                    "ERFME": "KT",
                    "LIFNR": "0000022204",
                    "EBELN": "test3",
                    "BSART": "ZSZ",
                    "EBELP": "12345",
                    "UMWRK": "test",
                    "UMLGO": "test",
                    "PS_PSP_PNR": "010099.000.RE-33-0000-02",
                    "FISTL": "100204000",
                    "GEBER": "NOPROJECT",
                    "FIPOS": "2020203",
                    "ANLN1": "test",
                    "KOSTL": "test",
                    "AUFNR": "test",
                    "SMBLN": "test",
                    "DMBTR": 5000000,
                    "XBLNR_MKPF": "0180546478",
                    "ARC_DOC_ID": "test",
                    "ACT-ID": "test",
                    "ACT_POS": 0,
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == 'Не известный атрибут "Вид операции"', f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

# Загрузка записи с BWART == 101 и EBELN_IT != Null и нет совпадений со сборочным ключом из полей item.EBELN_IT и item.EBELP_IT

    def test_uncorrect_ebeln_it_and_ebeln_it(self):
        test_name = 'Загрузка записи с BWART == 101 и EBELN_IT != Null и нет совпадений со сборочным ключом из полей item.EBELN_IT и item.EBELP_IT'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": 1,
                    "EBELN_IT": 7555,
                    "EBELP_IT": 56,
                    "MBLNR": "5003138828",
                    "MJAHR": 2021,
                    "VGART": "WE",
                    "BLART": "WE",
                    "BUDAT": "2021-05-16",
                    "ZEILE": 1,
                    "BWART": 101,
                    "WERKS": "1001",
                    "LGORT": "3004",
                    "CHARG": "0006678068",
                    "ZZ_KLASS": "0800",
                    "MATNR": "000000770000150513",
                    "MENGE": 100,
                    "MEINS": "KT",
                    "ERFMG": 100,
                    "ERFME": "KT",
                    "LIFNR": "0000022204",
                    "EBELN": "test3",
                    "BSART": "ZSZ",
                    "EBELP": "12345",
                    "UMWRK": "test",
                    "UMLGO": "test",
                    "PS_PSP_PNR": "010099.000.RE-33-0000-02",
                    "FISTL": "100204000",
                    "GEBER": "NOPROJECT",
                    "FIPOS": "2020203",
                    "ANLN1": "test",
                    "KOSTL": "test",
                    "AUFNR": "test",
                    "SMBLN": "test",
                    "DMBTR": 5000000,
                    "XBLNR_MKPF": "0180546478",
                    "ARC_DOC_ID": "test",
                    "ACT-ID": "test",
                    "ACT_POS": 0,
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "В системе нет позиции ИТ-актива в запросе на перемещение с заданным ключом", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

# Не заполнен идентификатор для определения ИТ-актива в запросе на ввод в эксплуатацию (BWART == 941 и ACT_POS == Null)
    def test_bwart_is_941_act_id_is_null(self):
        test_name = 'Не заполнен идентификатор для определения ИТ-актива в запросе на ввод в эксплуатацию (BWART == 941 и ACT_POS == Null)'
        json_data = {
            "currentPage": "1",
            "pageCount": "3",
            "delta": "D",
            "item": [
                {
                    "row": 1,
                    "EBELN_IT": 7555,
                    "EBELP_IT": 56,
                    "MBLNR": "5003138828",
                    "MJAHR": 2021,
                    "VGART": "WE",
                    "BLART": "WE",
                    "BUDAT": "2021-05-16",
                    "ZEILE": 1,
                    "BWART": 941,
                    "WERKS": "1001",
                    "LGORT": "3004",
                    "CHARG": "0006678068",
                    "ZZ_KLASS": "0800",
                    "MATNR": "000000770000150513",
                    "MENGE": 100,
                    "MEINS": "KT",
                    "ERFMG": 100,
                    "ERFME": "KT",
                    "LIFNR": "0000022204",
                    "EBELN": "test3",
                    "BSART": "ZSZ",
                    "EBELP": "12345",
                    "UMWRK": "test",
                    "UMLGO": "test",
                    "PS_PSP_PNR": "010099.000.RE-33-0000-02",
                    "FISTL": "100204000",
                    "GEBER": "NOPROJECT",
                    "FIPOS": "2020203",
                    "ANLN1": "test",
                    "KOSTL": "test",
                    "AUFNR": "test",
                    "SMBLN": "test",
                    "DMBTR": 5000000,
                    "XBLNR_MKPF": "0180546478",
                    "ARC_DOC_ID": "test",
                    "ACT-ID": "test",
                    "ACT_POS": "",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == 'Не заполнен идентификатор для определения ИТ-актива в запросе на ввод в эксплуатацию для подтверждения операции "Ввод в эксплуатацию"', f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

# Не заполнен идентификатор для определения ИТ-актива в запросе на ввод в эксплуатацию (BWART == 291 и ACT_POS == Null)
    def test_bwart_is_291_act_pos_is_null(self):
        test_name = 'Не заполнен идентификатор для определения ИТ-актива в запросе на ввод в эксплуатацию (BWART == 291 и ACT_POS == Null)'
        json_data = {
            "currentPage": "1",
            "pageCount": "3",
            "delta": "D",
            "item": [
                {
                    "row": 1,
                    "EBELN_IT": 7555,
                    "EBELP_IT": 56,
                    "MBLNR": "5003138828",
                    "MJAHR": 2021,
                    "VGART": "WE",
                    "BLART": "WE",
                    "BUDAT": "2021-05-16",
                    "ZEILE": 1,
                    "BWART": 291,
                    "WERKS": "1001",
                    "LGORT": "3004",
                    "CHARG": "0006678068",
                    "ZZ_KLASS": "0800",
                    "MATNR": "000000770000150513",
                    "MENGE": 100,
                    "MEINS": "KT",
                    "ERFMG": 100,
                    "ERFME": "KT",
                    "LIFNR": "0000022204",
                    "EBELN": "test3",
                    "BSART": "ZSZ",
                    "EBELP": "12345",
                    "UMWRK": "test",
                    "UMLGO": "test",
                    "PS_PSP_PNR": "010099.000.RE-33-0000-02",
                    "FISTL": "100204000",
                    "GEBER": "NOPROJECT",
                    "FIPOS": "2020203",
                    "ANLN1": "test",
                    "KOSTL": "test",
                    "AUFNR": "test",
                    "SMBLN": "test",
                    "DMBTR": 5000000,
                    "XBLNR_MKPF": "0180546478",
                    "ARC_DOC_ID": "test",
                    "ACT-ID": "test",
                    "ACT_POS": "",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == 'Не заполнен идентификатор для определения ИТ-актива в запросе на ввод в эксплуатацию для подтверждения операции "Ввод в эксплуатацию"', f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Не заполнен идентификатор для определения ИТ-актива в запросе на ввод в эксплуатацию (BWART == 261 и ACT_POS == Null)
    def test_bwart_is_261_act_pos_is_null(self):
        test_name = 'Не заполнен идентификатор для определения ИТ-актива в запросе на ввод в эксплуатацию (BWART ==  261 и ACT_POS == Null)'
        json_data = {
            "currentPage": "1",
            "pageCount": "3",
            "delta": "D",
            "item": [
                {
                    "row": 1,
                    "EBELN_IT": 7555,
                    "EBELP_IT": 56,
                    "MBLNR": "5003138828",
                    "MJAHR": 2021,
                    "VGART": "WE",
                    "BLART": "WE",
                    "BUDAT": "2021-05-16",
                    "ZEILE": 1,
                    "BWART": 261,
                    "WERKS": "1001",
                    "LGORT": "3004",
                    "CHARG": "0006678068",
                    "ZZ_KLASS": "0800",
                    "MATNR": "000000770000150513",
                    "MENGE": 100,
                    "MEINS": "KT",
                    "ERFMG": 100,
                    "ERFME": "KT",
                    "LIFNR": "0000022204",
                    "EBELN": "test3",
                    "BSART": "ZSZ",
                    "EBELP": "12345",
                    "UMWRK": "test",
                    "UMLGO": "test",
                    "PS_PSP_PNR": "010099.000.RE-33-0000-02",
                    "FISTL": "100204000",
                    "GEBER": "NOPROJECT",
                    "FIPOS": "2020203",
                    "ANLN1": "test",
                    "KOSTL": "test",
                    "AUFNR": "test",
                    "SMBLN": "test",
                    "DMBTR": 5000000,
                    "XBLNR_MKPF": "0180546478",
                    "ARC_DOC_ID": "test",
                    "ACT-ID": "test",
                    "ACT_POS": "",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == 'Не заполнен идентификатор для определения ИТ-актива в запросе на ввод в эксплуатацию для подтверждения операции "Ввод в эксплуатацию"', f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

    def test_bwart_is_941_act_id_is_null(self):
        test_name = 'Не заполнен идентификатор для определения ИТ-актива в запросе на ввод в эксплуатацию (BWART == 941 и ACT-ID == Null)'
        json_data = {
            "currentPage": "1",
            "pageCount": "3",
            "delta": "D",
            "item": [
                {
                    "row": 1,
                    "EBELN_IT": 7555,
                    "EBELP_IT": 56,
                    "MBLNR": "5003138828",
                    "MJAHR": 2021,
                    "VGART": "WE",
                    "BLART": "WE",
                    "BUDAT": "2021-05-16",
                    "ZEILE": 1,
                    "BWART": 941,
                    "WERKS": "1001",
                    "LGORT": "3004",
                    "CHARG": "0006678068",
                    "ZZ_KLASS": "0800",
                    "MATNR": "000000770000150513",
                    "MENGE": 100,
                    "MEINS": "KT",
                    "ERFMG": 100,
                    "ERFME": "KT",
                    "LIFNR": "0000022204",
                    "EBELN": "test3",
                    "BSART": "ZSZ",
                    "EBELP": "12345",
                    "UMWRK": "test",
                    "UMLGO": "test",
                    "PS_PSP_PNR": "010099.000.RE-33-0000-02",
                    "FISTL": "100204000",
                    "GEBER": "NOPROJECT",
                    "FIPOS": "2020203",
                    "ANLN1": "test",
                    "KOSTL": "test",
                    "AUFNR": "test",
                    "SMBLN": "test",
                    "DMBTR": 5000000,
                    "XBLNR_MKPF": "0180546478",
                    "ARC_DOC_ID": "test",
                    "ACT-ID": "",
                    "ACT_POS": 0,
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == 'Не заполнен идентификатор для определения ИТ-актива в запросе на ввод в эксплуатацию для подтверждения операции "Ввод в эксплуатацию"', f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


    def test_bwart_is_291_act_id_is_null(self):
        test_name = 'Не заполнен идентификатор для определения ИТ-актива в запросе на ввод в эксплуатацию (BWART == 291 и ACT-ID == Null)'
        json_data = {
            "currentPage": "1",
            "pageCount": "3",
            "delta": "D",
            "item": [
                {
                    "row": 1,
                    "EBELN_IT": 7555,
                    "EBELP_IT": 56,
                    "MBLNR": "5003138828",
                    "MJAHR": 2021,
                    "VGART": "WE",
                    "BLART": "WE",
                    "BUDAT": "2021-05-16",
                    "ZEILE": 1,
                    "BWART": 291,
                    "WERKS": "1001",
                    "LGORT": "3004",
                    "CHARG": "0006678068",
                    "ZZ_KLASS": "0800",
                    "MATNR": "000000770000150513",
                    "MENGE": 100,
                    "MEINS": "KT",
                    "ERFMG": 100,
                    "ERFME": "KT",
                    "LIFNR": "0000022204",
                    "EBELN": "test3",
                    "BSART": "ZSZ",
                    "EBELP": "12345",
                    "UMWRK": "test",
                    "UMLGO": "test",
                    "PS_PSP_PNR": "010099.000.RE-33-0000-02",
                    "FISTL": "100204000",
                    "GEBER": "NOPROJECT",
                    "FIPOS": "2020203",
                    "ANLN1": "test",
                    "KOSTL": "test",
                    "AUFNR": "test",
                    "SMBLN": "test",
                    "DMBTR": 5000000,
                    "XBLNR_MKPF": "0180546478",
                    "ARC_DOC_ID": "test",
                    "ACT-ID": "",
                    "ACT_POS": 0,
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == 'Не заполнен идентификатор для определения ИТ-актива в запросе на ввод в эксплуатацию для подтверждения операции "Ввод в эксплуатацию"', f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

    def test_bwart_is_261_act_id_is_null(self):
        test_name = 'Не заполнен идентификатор для определения ИТ-актива в запросе на ввод в эксплуатацию (BWART ==  261 и ACT-ID == Null)'
        json_data = {
            "currentPage": "1",
            "pageCount": "3",
            "delta": "D",
            "item": [
                {
                    "row": 1,
                    "EBELN_IT": 7555,
                    "EBELP_IT": 56,
                    "MBLNR": "5003138828",
                    "MJAHR": 2021,
                    "VGART": "WE",
                    "BLART": "WE",
                    "BUDAT": "2021-05-16",
                    "ZEILE": 1,
                    "BWART": 261,
                    "WERKS": "1001",
                    "LGORT": "3004",
                    "CHARG": "0006678068",
                    "ZZ_KLASS": "0800",
                    "MATNR": "000000770000150513",
                    "MENGE": 100,
                    "MEINS": "KT",
                    "ERFMG": 100,
                    "ERFME": "KT",
                    "LIFNR": "0000022204",
                    "EBELN": "test3",
                    "BSART": "ZSZ",
                    "EBELP": "12345",
                    "UMWRK": "test",
                    "UMLGO": "test",
                    "PS_PSP_PNR": "010099.000.RE-33-0000-02",
                    "FISTL": "100204000",
                    "GEBER": "NOPROJECT",
                    "FIPOS": "2020203",
                    "ANLN1": "test",
                    "KOSTL": "test",
                    "AUFNR": "test",
                    "SMBLN": "test",
                    "DMBTR": 5000000,
                    "XBLNR_MKPF": "0180546478",
                    "ARC_DOC_ID": "test",
                    "ACT-ID": "",
                    "ACT_POS": 0,
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == 'Не заполнен идентификатор для определения ИТ-актива в запросе на ввод в эксплуатацию для подтверждения операции "Ввод в эксплуатацию"', f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

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

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "KOKRS")

    def test_null_kokrs_value_delta_f(self):
        test_name = 'Проверка возможности создания записи без обязательных полей режим "F" (пустой "KOKRS")'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "",
                    "BUKRS": "IteBUCode 5",
                    "SAKNR": "IteCTNumAccount 5",
                    "KSTAR": "main test code 5",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 5",
                    "SPRAS": "IteCTLanguageCode 5",
                    "KTOPL": "IteCTChartOfAccounts 5",
                    "KTEXT": "IteCTCommonName 5",
                    "LTEXT": "IteCTDescription 5",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - KOKRS", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "BUKRS")

    def test_null_bukrs_value_delta_f(self):
        test_name = 'Проверка возможности создания записи без обязательных полей режим "F" (пустой "BUKRS")'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 6",
                    "BUKRS": "",
                    "SAKNR": "IteCTNumAccount 6",
                    "KSTAR": "main test code 6",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 6",
                    "SPRAS": "IteCTLanguageCode 6",
                    "KTOPL": "IteCTChartOfAccounts 6",
                    "KTEXT": "IteCTCommonName 6",
                    "LTEXT": "IteCTDescription 6",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - BUKRS", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "SAKNR")

    def test_null_saknr_value_delta_f(self):
        test_name = 'Проверка возможности создания записи без обязательных полей режим "F" (пустой "SAKNR")'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 7",
                    "BUKRS": "IteBUCode 7",
                    "SAKNR": "",
                    "KSTAR": "main test code 7",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 7",
                    "SPRAS": "IteCTLanguageCode 7",
                    "KTOPL": "IteCTChartOfAccounts 7",
                    "KTEXT": "IteCTCommonName 7",
                    "LTEXT": "IteCTDescription 7",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - SAKNR", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


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


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "DATBI")

    def test_null_datbi_value_delta_f(self):
        test_name = 'Проверка возможности создания записи без обязательных полей режим "F" (пустой "DATBI")'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 9",
                    "BUKRS": "IteBUCode 9",
                    "SAKNR": "IteCTNumAccount 9",
                    "KSTAR": "main test code 9",
                    "DATBI": "",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 9",
                    "SPRAS": "IteCTLanguageCode 9",
                    "KTOPL": "IteCTChartOfAccounts 9",
                    "KTEXT": "IteCTCommonName 9",
                    "LTEXT": "IteCTDescription 9",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - DATBI", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "DATAB")

    def test_null_datab_value_delta_f(self):
        test_name = 'Проверка возможности создания записи без обязательных полей режим "F" (пустой "DATAB")'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 10",
                    "BUKRS": "IteBUCode 10",
                    "SAKNR": "IteCTNumAccount 10",
                    "KSTAR": "main test code 10",
                    "DATBI": "01.01.20",
                    "DATAB": "",
                    "KATYP": "IteCTCostElementType 10",
                    "SPRAS": "IteCTLanguageCode 10",
                    "KTOPL": "IteCTChartOfAccounts 10",
                    "KTEXT": "IteCTCommonName 10",
                    "LTEXT": "IteCTDescription 10",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - DATAB", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "KATYP")

    def test_null_katyp_value_delta_f(self):
        test_name = 'Проверка возможности создания записи без обязательных полей режим "F" (пустой "KATYP")'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 11",
                    "BUKRS": "IteBUCode 11",
                    "SAKNR": "IteCTNumAccount 11",
                    "KSTAR": "main test code 11",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "",
                    "SPRAS": "IteCTLanguageCode 11",
                    "KTOPL": "IteCTChartOfAccounts 11",
                    "KTEXT": "IteCTCommonName 11",
                    "LTEXT": "IteCTDescription 11",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - KATYP", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "SPRAS")

    def test_null_spras_value_delta_f(self):
        test_name = 'Проверка возможности создания записи без обязательных полей режим "F" (пустой "SPRAS")'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 12",
                    "BUKRS": "IteBUCode 12",
                    "SAKNR": "IteCTNumAccount 12",
                    "KSTAR": "main test code 12",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 12",
                    "SPRAS": "",
                    "KTOPL": "IteCTChartOfAccounts 12",
                    "KTEXT": "IteCTCommonName 12",
                    "LTEXT": "IteCTDescription 12",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - SPRAS", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "KTOPL")

    def test_null_ktopl_value_delta_f(self):
        test_name = 'Проверка возможности создания записи без обязательных полей режим "F" (пустой "KTOPL")'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 13",
                    "BUKRS": "IteBUCode 13",
                    "SAKNR": "IteCTNumAccount 13",
                    "KSTAR": "main test code 13",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 13",
                    "SPRAS": "IteCTLanguageCode 13",
                    "KTOPL": "",
                    "KTEXT": "IteCTCommonName 13",
                    "LTEXT": "IteCTDescription 13",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - KTOPL", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "KTEXT")

    def test_null_ktext_value_delta_f(self):
        test_name = 'Проверка возможности создания записи без обязательных полей режим "F" (пустой "KTEXT")'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 14",
                    "BUKRS": "IteBUCode 14",
                    "SAKNR": "IteCTNumAccount 14",
                    "KSTAR": "main test code 14",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 14",
                    "SPRAS": "IteCTLanguageCode 14",
                    "KTOPL": "IteCTChartOfAccounts 14",
                    "KTEXT": "",
                    "LTEXT": "IteCTDescription 14",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - KTEXT", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "LTEXT")

    def test_null_ltext_value_delta_f(self):
        test_name = 'Проверка возможности создания записи без обязательных полей режим "F" (пустой "LTEXT")'
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "KOKRS": "IteCTControllingUnit 15",
                    "BUKRS": "IteBUCode 15",
                    "SAKNR": "IteCTNumAccount 15",
                    "KSTAR": "main test code 15",
                    "DATBI": "01.01.20",
                    "DATAB": "31.12.21",
                    "KATYP": "IteCTCostElementType 15",
                    "SPRAS": "IteCTLanguageCode 15",
                    "KTOPL": "IteCTChartOfAccounts 15",
                    "KTEXT": "IteCTCommonName 15",
                    "LTEXT": "",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar, test_name=test_name)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - LTEXT", f"The value of 'MESSAGE' is not correct"
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



