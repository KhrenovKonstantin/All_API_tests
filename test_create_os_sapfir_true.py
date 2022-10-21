import json
from my_lib.assertions import Assertion
from my_lib.my_requests import MyRequests
from my_lib.base_case import BaseCase
import allure

# Название: Создать ОС в САПФИР
# Место положение: раздел Ввод ИТ-активов в эксплуатации
# Тест кейс: https://jira.itexpert.ru/secure/Tests.jspa#/testCase/IT4ITMVP-T2108
# Описание: https://cf.itexpert.ru/pages/viewpage.action?pageId=155490682
# Описание раздела: https://cf.itexpert.ru/pages/viewpage.action?pageId=155486811

# python -m pytest -s test_create_os_sapfir_false.py -k TestCreateCommis_Assembling_False
# python -m pytest -s tests\test_create_os_sapfir_false.py -k TestCreateCommis_Assembling_False.py.test
# python -m pytest --alluredir=allure_result_folder tests/test_create_commissioning_true.py
# allure serve allure_result_folder


@allure.epic("Создать ОС в САПФИР")
class TestCreateCommis_Assembling_True(BaseCase):

    # Запрос в состоянии Выполняется и IteAccountingSystem == САП.
    # И у каждой позиции из объекта Актив в запросе на ввод в эксплуатацию(ОС)(IteRequestForCommissioningAsset) заполнены поля:
    # iteRequestForCommissioningAsset.iteAsset.ItePlantCode, == Завод
    # iteRequestForCommissioningAsset.iteAsset.IteLogisticStructure, == Склад
    # iteRequestForCommissioningAsset.iteAsset.IteConsignmentCode, == Партия
    # iteRequestForCommissioningAsset.iteAsset.ItePPStructure == СПП-элемент
    # Авторизация и получение необходимых cookie и headers
    # Запрос создает запись в справочнике 'Категории ЕСМ'
    @allure.description("Авторизация и получение необходимых cookie и headers"
                        "Создать ОС в САПФИР'")
    def setup(self):
        env = 'http://localmail.itexpert.ru:5057'
        auth_data = {
            "UserName": "d.vavrinyuk",
            "UserPassword": "123"
        }
        self.url = "http://192.168.0.73:44400/test/createOS"
        self.jar, self.header = MyRequests.user_auth(self, auth_data, env)
    # по условию iteRequestForCommissioningAsset.iteSendToAccountingSytem == FALSE
    # галочка Передано в БУ не активана

    # Необходим монтаж iteNeedForAssembling = True

    # iteRequestForCommissioningAsset
    # Поиск значений в справочнике осуществляется по Поле Код "Code"
    # Если значение найдено - обновляем атрибуты, если не найдено - создаем новую запись в справочнике "Категории ЕСМ"
    # Если "Deletion_mark": "True" то запись с соответсвующем Код КСУ НСИ буде удалена
        # 3 Отправка сообщения для ввода в эксплуатацию ОС
        @allure.description("Отправка сообщения для ввода в эксплуатацию ОС")
        def test_request_3(self):

            self.url = "http://192.168.0.73:44400/test/createOS"

            json_data = {
                "currentPage": "1",  # текущая страница
                "pageCount": "1",  # количество страниц
                "delta": "F",  # F - режим полной выгрузки справочника, D - дельта(по умолчанию),
                "item": [
                    {
                        "BUKRS": "1000",        # iteRequestForCommissioning.IteOwningОrganization.IteBUCode
                        "ANLKL": "10400000",    # iiteRequestForCommissioningAsset.iteAsset.IteAssetDirectory.iteAssetClass
                        "POSNR": "11000.I16GSP0119",  # iiteRequestForCommissioning.ItePPStructure.IteItemCode
                        "TXT50": "Ноутбук Dell PER440/409316Z",# Наименование справочник-ИТА iiteRequestForCommissioningAsset.iteAsset.IteAssetDirectory.IteAssetWorkingName
                        "TXA50": "",            # iiteRequestForCommissioningAsset.iteAsset.IteAssetDirectory.IteAssetWorkingName
                        "SERNR": "123Test",     # Серийный номер актива #iiteRequestForCommissioningAsset.iteAsset.IteSerialNumber
                        "INVNR": "",
                        "XNEU_AM": "",
                        "MEINS": "шт",          # единицы измерения в справочнике-ИТА iiteRequestForCommissioningAsset.iteAsset.IteAssetDirectory.IteBaseUnit,
                        "MENGE": "1.0",         # i1,
                        "GLO_RUS_OKOF16": "test123",# Код ОКФ спрвочник-ИТА iiteRequestForCommissioningAsset.iteAsset.IteAssetDirectory.iteOKOFCode
                        "NDJAR": "2029254348",  # iiteRequestForCommissioningAsset.IteAsset.IteUsefulLife
                        "ZZPROPTYPE": "1",      # i1,
                        "AKTIV": "",            # iiteRequestForCommissioning.iteCommissioningDate,
                        "ZZTOU": "Код ТОУ",     # Код ТОУ в справчонике ИТА iiteRequestForCommissioningAsset.iteAsset.IteAssetDirectory.iteTOUCode
                        "GLO_RUS_DEPGR": "Группа амортизации", # iiteRequestForCommissioningAsset.iteAsset.IteAssetDirectory.iteAmortizationGroup
                        "KOSTL": "2029254348",  # iiteRequestForCommissioning.IteCostCenter.IteCSCode,
                        "PERNR": "285052",      # iiteRequestForCommissioningAsset.iteAsset.IteResponsible.IteConditionalNumber.ItePersonnelNumber
                                                # (где IteConditionalNumber.IteBUCode == значение для поля "BUKRS")
                        "STORT": "KTEXT",
                        "KTEXT": "",
                        "ZZMATNR": "",
                        "INBDA": "",
                        "ZZVVOD_DOK_NAME": "",
                        "ZZVVOD_DOK_DATE": "",
                        "ZZVVOD_DOK_NUM": "",
                        "LIEFE": "",
                        "ORD43": "test",        # iteRequestForCommissioningAsset.iteAcquisitionKind.Code,
                        "ZZDOG_NUM": "",
                        "NAME_TEXT": "test_spec",# (контакт текущей учетной записи, кто инициировал отправку сообщения в САПФИР)
                        "SMTP_ADDR": "5050@stepanov.work"# (контакт текущей учетной записи, кто инициировал отправку сообщения в САПФИР)
                    }
                ]
            }

            print(f"\n Отправка сообщения для ввода в эксплуатацию ОС")
            # проверка всех полей на заполнение
            json_data_list = json_data["item"]
            json_data_dict = json_data_list[0]
            # print(json_data_dict)
            # for key, value in json_data_dict.items():
            #     if value == "":
            #         print(key)

            assert json_data_dict["NAME_TEXT"] != "", "Параметр Code не может быть пустым."
            assert json_data_dict["SMTP_ADDR"] != "", "Параметр Name не может быть пустым."

            response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
            Assertion.assert_code_status(response, 200)

            print(response.text)

            obj = json.loads(response.text)
            assert obj["message"] == 'OK', f"The value of 'MESSAGE' is not correct"
            assert obj["isSuccessful"] == True, f"The value of 'success' is not correct"
            for str in obj["result"]:
                for key, value in str.items():
                    if key == "TYPE":
                        assert value == "S", f"Запрос не корректен"

