import json
from my_lib.assertions import Assertion
from my_lib.my_requests import MyRequests
from my_lib.base_case import BaseCase
import allure

# python -m pytest -s test_order_purchase_sp_contr.py -k TestOrderPurchaseSpContr
# py.test --alluredir=allure_result_folder ./test_order_purchase_sp_contr.py
# allure serve allure_result_folder

# Тестирование Заказ на поставку (спецификация к контракту) из SAP ERP САПФИР

@allure.epic("Тестирование Заказ на поставку (спецификация к контракту) из SAP ERP САПФИР")
class TestOrderPurchaseSpContr(BaseCase):

    # Авторизация и получение необходимых cookie и headers
    @allure.description('Авторизация и получение необходимых cookie и headers')
    def setup(self):
        env = 'http://localmail.itexpert.ru:5057'
        auth_data = {
            "UserName": "Supervisor",
            "UserPassword": "!Supervisor123Test!"
        }
        self.url = "http://localmail.itexpert.ru:5057/rest/SapErpIntegrationService/v1/UpdatePurchaseOrder"
        self.jar, self.header = MyRequests.user_auth(self, auth_data, env)

    # Заказ на поставку (спецификация к контракту) из SAP ERP САПФИР
    # @allure.description('Заказ на поставку (спецификация к контракту) из SAP ERP САПФИР')
    # def test2(self):
    #     json_data = {
    #         "currentPage": "1",  # //текущая страница
    #         "pageCount": "1",  # //количество страниц
    #         "delta": "F",  # // F - режим полной выгрузки справочника, D - дельта (по умолчанию)
    #         "item": [  # //элементы справочника
    #             {
    #                 "row": "1",  # // Номер строки в коллекции
    #                 "EBELN": "4501219688",  # // Номер заказа на поставку
    #                 "EBELP": "10",  # // Позиция заказа на поставку
    #                 "EBELP_IT": "int",  # // Вид документа
    #                 "BEDAT": "2022-07-04",  # // Дата документа
    #                 "BSART": "ZSZ",  # // Вид документа
    #                 "EKORG": "1000",  # // Закупочная организация
    #                 "EKGRP": "GPZ",  # // Группа закупок
    #                 "FRGGR": "ZZ",  # // Группа деблокирования
    #                 "FRGSX": "ZK",  # // Стратегия деблокирования
    #                 "FRGZU": "1",  # // Статус выдачи
    #                 "BUKRS": "1000",  # // Балансовая единица
    #                 "MATNR": "000000770001087536",  # // № материала в SAP
    #                 "MENGE": "20.0",  # // Количество материала
    #                 "MEINS": "ST",  # // Единица измерения материала в заказе
    #                 "WERKS": "1001",  # / Завод (Принимающий завод)
    #                 "LGORT": "123123",  # // Склад (Принимающий склад)
    #                 "EINDT": "2022-07-04",  # / Дата поставки для позиции
    #                 "PS_PSP_PNR": "00035662",  # // Код СПП-Элемента
    #                 "ZZ_KLASS": "1609",  # // Класс оценки
    #                 "FISTL": "111111",  # // ПФМ
    #                 "GEBER": "222222",  # // Фонд
    #                 "FIPOS": "33",  # // Финансовая позиция
    #                 "LIFNR": "0000098052",  # // Поставщик
    #                 "KONNR": "4600047170",  # // Контракт
    #                 "NAME1": "Тестовая оргнанизация",  # // Данные поставщика - Наименование поставщика
    #                 "STCD1": "0000113636",  # // Данные поставщика - ИНН поставщика
    #                 "STCD2": "00039093",  # // Данные поставщика - ОКПО поставщика
    #                 "STCD3": "000036466",  # // Данные поставщика -КПП поставщика
    #                 "LOEKZ": "1234",  # // Индикатор удаления
    #                 "LMEIN": "ST",  # // Базисная единица измерения материала в заказе
    #                 "UMREZ": "1",  # // Числитель для пересчета ЕИ заказа в базисную ЕИ
    #                 "UMREN": "1",  # // Знаменатель для пересчета ЕИ заказа в базисную ЕИ
    #                 "ZZ_ZEMLI": "0000008602",  # // Грузополучатель
    #                 "ERNAM": "testexample@gmail.com",  # // E-mail пользователя создавшего заказ
    #                 "NETPR": "10000",  # // Цена закупки без НДС
    #
    #                 "deleted": ""  # // X - удалено, "" - новый или измененный
    #             }
    #         ]
    #
    #     }
    #     response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
    #     Assertion.assert_code_status(response, 200)
    #     print(response.text)
    #     obj = json.loads(response.text)
    #     for result in obj['result']:
    #         assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
    #         assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

    # Заказ на поставку (спецификация к контракту) из SAP ERP САПФИР

    # Первая проверка # Система ищет ищет экземпляр позиции запроса на закупку по условию
    #                     # IteRequestForPurchaseAssetComponent.IteOrder== EBELN &&
    #                     # IteRequestForPurchaseAssetComponent.IteOrderPos == EBELP
    @allure.description('Первая проверка # Система ищет ищет экземпляр позиции запроса на закупку по условию '
                        'IteRequestForPurchaseAssetComponent.IteOrder== EBELN && '
                        'IteRequestForPurchaseAssetComponent.IteOrderPos == EBELP')
    def test1_assert(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "EBELN": "444444",  # Поле для поиска
                    "EBELP": "2",  # Поле для поиска
                    "BEDAT": "30.08.2021",
                    # IteRequestForPurchaseAsset(или IteRequestForPurchaseAssetComponent).IteOrderDate= BEDAT
                    "MATNR": "000000000001228424", #НЕ ПОДГРУЗИТСЯ
                    # ТОЛЬКО ДЛЯ IteRequestForPurchaseAsset: IteRequestForPurchaseAsset.IteAssetApproved = элемент справочника iteAssetDirectory по условию (iteAssetDirectory.IteAssetAccountingNumber == MATNR)
                    "MENGE": "12",
                    # IteRequestForPurchaseAsset(или IteRequestForPurchaseAssetComponent).IteQtyApproved = MENGE
                    "EINDT": "30.08.2021",
                    # IteRequestForPurchaseAsset(или IteRequestForPurchaseAssetComponent).IteOrderDeliveryDate = EINDT
                    "LIFNR": "0000040878",
                    # IteRequestForPurchaseAsset(или IteRequestForPurchaseAssetComponent).IteSupplier = элемент справочника Объект Контрагенты по условию Объект Контрагенты.Код == LIFNR
                    "KONNR": "4600045403",
                    # IteRequestForPurchaseAsset(или IteRequestForPurchaseAssetComponent).IteContract = KONNR
                    "ERNAM": "testexample@gmail.com",  # // E - mail пользователя создавшего заказ
                    # IteRequestForPurchaseAsset(или IteRequestForPurchaseAssetComponent).IteOrderAuthorEmail =  ERNAM
                    "NETPR": "111.11",  # // Цена закупки без НДС
                    # IteRequestForPurchaseAsset(или IteRequestForPurchaseAssetComponent).IteContractPrice = NETPR

                    # "BSART": "ZSZ",
                    # "EKORG": "1000",
                    # "EKGRP": "500",
                    # "FRGGR": "ZZ",
                    # "FRGSX": "ZK",
                    # "FRGZU": "X",
                    # "BUKRS": "1000",
                    # "MEINS": "ST",
                    # "WERKS": "1001",
                    # "PS_PSP_PNR": "00034978",
                    # "ZZ_KLASS": "0700",
                    # "NAME1": "Организация1-89055",
                    # "STCD1": "0000111940",
                    # "STCD2": "00038439",
                    # "STCD3": "000035805",
                    # "LMEIN": "ST",
                    # "UMREZ": "1",
                    # "UMREN": "1",
                    # "ZZ_ZEMLI": "0000000836",

                    "deleted": ""  # // X - удалено, "" - новый или измененный
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

    # Вторая проверка  # Система ищет ищет экземпляр позиции запроса на закупку по условию
                       # IteRequestForPurchaseAsset.IteOrder== EBELN && IteRequestForPurchaseAsset.IteOrderPos == EBELP
    @allure.description('Вторая проверка  # Система ищет ищет экземпляр позиции запроса на закупку по условию '
                        'IteRequestForPurchaseAsset.IteOrder== EBELN && IteRequestForPurchaseAsset.IteOrderPos == '
                        'EBELP')
    def test2_assert(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "EBELN": "123123",  # Поле для поиска
                    "EBELP": "1",  # Поле для поиска
                    "BEDAT": "30.08.2021",
                    # IteRequestForPurchaseAsset(или IteRequestForPurchaseAssetComponent).IteOrderDate= BEDAT
                    "MATNR": "1234567890", #Подтянется
                    # ТОЛЬКО ДЛЯ IteRequestForPurchaseAsset: IteRequestForPurchaseAsset.IteAssetApproved = элемент справочника iteAssetDirectory по условию (iteAssetDirectory.IteAssetAccountingNumber == MATNR)
                    "MENGE": "13",
                    # IteRequestForPurchaseAsset(или IteRequestForPurchaseAssetComponent).IteQtyApproved = MENGE
                    "EINDT": "30.08.2021",
                    # IteRequestForPurchaseAsset(или IteRequestForPurchaseAssetComponent).IteOrderDeliveryDate = EINDT
                    "LIFNR": "0000040878",
                    # IteRequestForPurchaseAsset(или IteRequestForPurchaseAssetComponent).IteSupplier = элемент справочника Объект Контрагенты по условию Объект Контрагенты.Код == LIFNR
                    "KONNR": "4600045403",
                    # IteRequestForPurchaseAsset(или IteRequestForPurchaseAssetComponent).IteContract = KONNR
                    "ERNAM": "testexample@gmail.com",  # // E - mail пользователя создавшего заказ
                    # IteRequestForPurchaseAsset(или IteRequestForPurchaseAssetComponent).IteOrderAuthorEmail =  ERNAM
                    "NETPR": "111.11",  # // Цена закупки без НДС
                    # IteRequestForPurchaseAsset(или IteRequestForPurchaseAssetComponent).IteContractPrice = NETPR

                    # "BSART": "ZSZ",
                    # "EKORG": "1000",
                    # "EKGRP": "500",
                    # "FRGGR": "ZZ",
                    # "FRGSX": "ZK",
                    # "FRGZU": "X",
                    # "BUKRS": "1000",
                    # "MEINS": "ST",
                    # "WERKS": "1001",
                    # "PS_PSP_PNR": "00034978",
                    # "ZZ_KLASS": "0700",
                    # "NAME1": "Организация1-89055",
                    # "STCD1": "0000111940",
                    # "STCD2": "00038439",
                    # "STCD3": "000035805",
                    # "LMEIN": "ST",
                    # "UMREZ": "1",
                    # "UMREN": "1",
                    # "ZZ_ZEMLI": "0000000836",

                    "deleted": ""  # // X - удалено, "" - новый или измененный
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
