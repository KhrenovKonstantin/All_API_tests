import json
from my_lib.assertions import Assertion
from my_lib.my_requests import MyRequests
from my_lib.base_case import BaseCase
import allure


# python -m pytest -s test_update_inform_reserv_date.py -k TestUpdateInformReservDate
# py.test --alluredir=allure_result_folder ./test_update_inform_reserv_date.py
# allure serve allure_result_folder

# Актуализация информации о запасах по данным SAP ERP САПФИР

@allure.epic("Актуализация информации о запасах по данным SAP ERP САПФИР ")
class TestUpdateInformReservDate(BaseCase):

    # Авторизация и получение необходимых cookie и headers
    @allure.description('Авторизация и получение необходимых cookie и headers')
    def setup(self):
        env = 'http://localmail.itexpert.ru:5057'
        auth_data = {
            "UserName": "Supervisor",
            "UserPassword": "!Supervisor123Test!"
        }
        self.url = "http://localmail.itexpert.ru:5057/rest/SapErpIntegrationService/v1/UpdateTrafficDocumentsMTP"
        self.jar, self.header = MyRequests.user_auth(self, auth_data, env)

    # 1 положительная обработка + проверка актуальности записи
    @allure.description('1 положительная обработка + проверка актуальности записи')
    def test_first_responce(self):
        json_data = {
            "currentPage": "1",  # //текущая страница
            "pageCount": "1",  # //количество страниц
            "delta": "D",  # // F - режим полной выгрузки справочника, D - дельта (по умолчанию)
            "item": [  # //элементы справочника
                {
                    "row": "1",  # // Номер строки в коллекции
                    "BWART": '101',  # // Вид движения == 101
                    "EBELN_IT": "RM00000174",  # // Номер запроса на перемещение в СУИТА == IteRequestForMoving.IteNumber
                    "EBELP_IT": "1",  # // Позиция запроса на перемещение в СУИТА == IteRequestForMovingAsset.ItePositionNumber
                    #"UMWRK": "1001",  # // Завод-получатель == IteAsset.ItePlantCode
                    #"UMLGO": "82232ad9-81bf-4885-a80d-f0691ed07129",  # // Принимающий склад == IteAsset.IteLogisticStructure
                    # Если поля не заполнены то пишем скрипт
                    # update "IteAsset" set "IteLogisticStructureId" = '82232ad9-81bf-4885-a80d-f0691ed07129' where "Id" = 'bffee4a4-a53c-487d-a74d-dafd37098819';
                    # update "IteAsset" set "ItePlantCode" = '1001' where "Id" = 'bffee4a4-a53c-487d-a74d-dafd37098819';
                    # select * from  "IteAsset" where "Id" = 'bffee4a4-a53c-487d-a74d-dafd37098819'

                    "MBLNR": "0000000",  # // Номер документа  материала == IteRequestForMovingAsset.IteDocSAP
                    # "MJAHR": "int",  # // Год документа материала
                    # "VGART": "string",  # // Вид операции
                    # "BLART": "string",  # // Вид документа
                    "BUDAT": "11.07.2022",  # // Дата проводки в документе (поступления, перемещения, отпуска) == IteRequestForMovingAsset.IteOrderPostingDate
                    "ZEILE": "1",  # // Позиция документа материала == IteRequestForMovingAsset.IteOrderPosSAP
                    #
                    "WERKS": "1001",  # // Завод == IteAsset.ItePlantCode
                    "LGORT": "0008",  # // Склад == IteAsset.IteLogisticStructure
                    # "CHARG": "string",  # // Номер партии
                    # "ZZ_KLASS": "string",  # // Класс оценки
                    # "MATNR": "string",  # // № материала в SAP
                    # "MENGE": "int",  # // Количество материала в БЕИ
                    # "MEINS": "string",  # // Базовая Единица измерения
                    # "ERFMG": "int",  # // Количество в ЕИ ввода/заказа
                    # "ERFME": "string",  # // Единица измерения материала ввода/заказа
                    # "LIFNR": "string",  # // Поставщик
                    # "EBELN": "string",  # // Номер заказа  (на поставку, перемещение)
                    # "BSART": "string",  # // Вид заказа (на поставку, перемещение)
                    # "EBELP": "int",  # // Позиция заказа  (на поставку, перемещение)
                    #
                    # "PS_PSP_PNR": "string",  # // Код СПП-Элемента
                    # "ВИД ОЦЕНКИ": "string",  # // Вид оценки 25.11.2021 И.Дернов - добавлено
                    # "FISTL": "string",  # // ПФМ
                    # "GEBER": "string",  # // Фонд
                    # "FIPOS": "string",  # // Финансовая позиция
                    # "VFDAT": "date",  # // Срок хранения партии
                    # "ANLN1": "string",  # // Номер карточки ОС (при списании на ОС)
                    # "KOSTL": "string",  # // МВЗ (при списании на МВЗ)
                    # "AUFNR": "string",  # // Номер заказа (при списании на заказ)
                    # "SMBLN": "string",  # // Номер сорнируемого документа
                    # "DMBTR": "double",  # // Стоимоcть
                    # "XBLNR_MKPF": "string",  # // Номер документа заголовка
                    # "ARC_DOC_ID": "string",  # // Ссылка на скан в ЭХД
                    # "ACT-ID": "string",  # // Предварительный документ списания
                    # "ACT_POS": "int",  # // Позиция предварительного акта списания
                    "deleted": ""  # // X - удалено, "" - новый или измененный
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        assert obj['message'] is None, f"The value of 'message' is not correct"
        assert obj['error'] is None, obj['error']

    # 2 положительная обработка + проверка актуальности записи
    @allure.description('2 положительная обработка + проверка актуальности записи')
    def test_second_responce(self):
        json_data = {
            "currentPage": "1",  # //текущая страница
            "pageCount": "1",  # //количество страниц
            "delta": "D",  # // F - режим полной выгрузки справочника, D - дельта (по умолчанию)
            "item": [  # //элементы справочника
                {
                    "row": "1",  # // Номер строки в коллекции
                    "BWART": "941",  # // Вид движения (941 или 291 или 261)
                    "ACT-ID": "1111",  # // Предварительный документ списания == iteRequestForCommissioningAsset.itePreWriteoffDocumentNumber
                    "ACT_POS": "1",  # // Позиция предварительного акта списания == IteRequestForCommissioningAsset.itePreWriteoffDocumentPos

    # update "IteRequestForCommissioningAsset" set "ItePreWriteoffDocumentNumber" = '1111' where "Id" = 'dbb5cebc-423e-4bef-8ba5-dbe2c6066c8a';
    # update "IteRequestForCommissioningAsset" set "ItePreWriteoffDocumentPos" = '1' where "Id" = 'dbb5cebc-423e-4bef-8ba5-dbe2c6066c8a';
    # select * from  "IteRequestForCommissioningAsset" where "Id" = 'dbb5cebc-423e-4bef-8ba5-dbe2c6066c8a'

                    "MBLNR": "1321312",  # // Номер документа  материала == iteRequestForCommissioningAsset.iteWriteoffDocumentNumber
                    "MJAHR": "2020",  # // Год документа материала == iteRequestForCommissioningAsset.iteWriteoffDocumentDate


                    # "EBELN_IT ": "string",  # // Номер запроса на перемещение в СУИТА
                    # "EBELP_IT": "int",  # // Позиция запроса на перемещение в СУИТА
                    # "UMWRK": "string",  # // Завод-получатель
                    # "UMLGO": "string",  # // Принимающий склад
                    #
                    #
                    # "VGART": "string",  # // Вид операции
                    # "BLART": "string",  # // Вид документа
                    # "BUDAT": "date",  # // Дата проводки в документе (поступления, перемещения, отпуска)
                    # "ZEILE": "int",  # // Позиция документа материала
                    #
                    # "WERKS": "string",  # // Завод
                    # "LGORT": "string",  # // Склад
                    # "CHARG": "string",  # // Номер партии
                    # "ZZ_KLASS": "string",  # // Класс оценки
                    # "MATNR": "string",  # // № материала в SAP
                    # "MENGE": "int",  # // Количество материала в БЕИ
                    # "MEINS": "string",  # // Базовая Единица измерения
                    # "ERFMG": "int",  # // Количество в ЕИ ввода/заказа
                    # "ERFME": "string",  # // Единица измерения материала ввода/заказа
                    # "LIFNR": "string",  # // Поставщик
                    # "EBELN": "string",  # // Номер заказа  (на поставку, перемещение)
                    # "BSART": "string",  # // Вид заказа (на поставку, перемещение)
                    # "EBELP": "int",  # // Позиция заказа  (на поставку, перемещение)
                    #
                    # "PS_PSP_PNR": "string",  # // Код СПП-Элемента
                    # "ВИД ОЦЕНКИ": "string",  # // Вид оценки 25.11.2021 И.Дернов - добавлено
                    # "FISTL": "string",  # // ПФМ
                    # "GEBER": "string",  # // Фонд
                    # "FIPOS": "string",  # // Финансовая позиция
                    # "VFDAT": "date",  # // Срок хранения партии
                    # "ANLN1": "string",  # // Номер карточки ОС (при списании на ОС)
                    # "KOSTL": "string",  # // МВЗ (при списании на МВЗ)
                    # "AUFNR": "string",  # // Номер заказа (при списании на заказ)
                    # "SMBLN": "string",  # // Номер сорнируемого документа
                    # "DMBTR": "double",  # // Стоимоcть
                    # "XBLNR_MKPF": "string",  # // Номер документа заголовка
                    # "ARC_DOC_ID": "string",  # // Ссылка на скан в ЭХД

                    "deleted": ""  # // X - удалено, "" - новый или измененный
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        assert obj['message'] is None, f"The value of 'message' is not correct"
        assert obj['error'] is None, obj['error']

    # 3 положительная обработка + проверка актуальности записи
    @allure.description('3 положительная обработка + проверка актуальности записи')
    def test_three_responce(self):
        json_data = {
            "currentPage": "1",  # //текущая страница
            "pageCount": "1",  # //количество страниц
            "delta": "D",  # // F - режим полной выгрузки справочника, D - дельта (по умолчанию)
            "item": [  # //элементы справочника
                {
                    "row": "1",  # // Номер строки в коллекции
                    "BWART": "101",  # // Вид движения
                    "EBELN_IT": None,  # // Номер запроса на перемещение в СУИТА (Прием актива)
                    "EBELN": "222333",  # // Номер заказа  (на поставку, перемещение) == IteRequestForSupply.ItePurchaseOrder
                    ## update "IteRequestForSupply" set "ItePurchaseOrder" = '222333' where "Id" = 'cc6d65ca-f522-4f57-8854-2d76042be4a8';
                    ## select * from "IteRequestForSupply" where "Id" = 'cc6d65ca-f522-4f57-8854-2d76042be4a8'
                    "EBELP": "10",  # // Позиция заказа  (на поставку, перемещение) == IteRequestForSupplyAsset.ItePositionNumber

                    "WERKS": "Тестовый завод",  # // Завод
                    "LGORT": "Тестовый склад",  # // Склад
                    "CHARG": "4",  # // Номер партии == IteRequestForSupplyAsset.IteInstance
                    "PS_PSP_PNR": "45645645611",  # // Код СПП-Элемента == IteRequestForSupplyAsset.ItePPStructure

                    ## "UMWRK": "string",  # // Завод-получатель == IteRequestForSupplyAsset.ItePlantCode
                    ## "UMLGO": "string",  # // Принимающий склад == IteRequestForSupplyAsset.IteWHCode
                    #
                    #
                    #
                    ## "ACT-ID": "string",  # // Предварительный документ списания
                    ## "ACT_POS": "int",  # // Позиция предварительного акта списания
                    ## "MBLNR": "string",  # // Номер документа  материала
                    ## "MJAHR": "int",  # // Год документа материала
                    #
                    #
                    #
                    ## "EBELP_IT": "int",  # // Позиция запроса на перемещение в СУИТА
                    #
                    #
                    #
                    ## "VGART": "string",  # // Вид операции
                    ## "BLART": "string",  # // Вид документа
                    # "BUDAT": "date",  # // Дата проводки в документе (поступления, перемещения, отпуска)
                    # "ZEILE": "int",  # // Позиция документа материала
                    #
                    #
                    #
                    # "ZZ_KLASS": "string",  # // Класс оценки
                    # "MATNR": "string",  # // № материала в SAP
                    # "MENGE": "int",  # // Количество материала в БЕИ
                    # "MEINS": "string",  # // Базовая Единица измерения
                    # "ERFMG": "int",  # // Количество в ЕИ ввода/заказа
                    # "ERFME": "string",  # // Единица измерения материала ввода/заказа
                    # "LIFNR": "string",  # // Поставщик
                    #
                    # "BSART": "string",  # // Вид заказа (на поставку, перемещение)
                    #
                    #
                    #
                    # "ВИД ОЦЕНКИ": "string",  # // Вид оценки 25.11.2021 И.Дернов - добавлено
                    # "FISTL": "string",  # // ПФМ
                    # "GEBER": "string",  # // Фонд
                    # "FIPOS": "string",  # // Финансовая позиция
                    # "VFDAT": "date",  # // Срок хранения партии
                    # "ANLN1": "string",  # // Номер карточки ОС (при списании на ОС)
                    # "KOSTL": "string",  # // МВЗ (при списании на МВЗ)
                    # "AUFNR": "string",  # // Номер заказа (при списании на заказ)
                    # "SMBLN": "string",  # // Номер сорнируемого документа
                    # "DMBTR": "double",  # // Стоимоcть
                    # "XBLNR_MKPF": "string",  # // Номер документа заголовка
                    # "ARC_DOC_ID": "string",  # // Ссылка на скан в ЭХД

                    "deleted": ""  # // X - удалено, "" - новый или измененный
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        assert obj['message'] is None, f"The value of 'message' is not correct"
        assert obj['error'] is None, obj['error']

    # Обработка ошибки !(item.BWART == 101 ИЛИ item.BWART == 941 ИЛИ item.BWART == 291 ИЛИ item.BWART == 261)
    @allure.description('Обработка ошибки !(item.BWART == 101 ИЛИ item.BWART == 941 ИЛИ item.BWART == 291 ИЛИ item.BWART == 261)')
    def test_second_break_responce(self):
        json_data = {
            "currentPage": "1",  # //текущая страница
            "pageCount": "1",  # //количество страниц
            "delta": "D",  # // F - режим полной выгрузки справочника, D - дельта (по умолчанию)
            "item": [  # //элементы справочника
                {
                    "row": "1",  # // Номер строки в коллекции
                    "BWART": "222",  # // Вид движения
                    "EBELN_IT": "None",  # // Номер запроса на перемещение в СУИТА (Прием актива)
                    "EBELN": "222333",
                    # // Номер заказа  (на поставку, перемещение) == IteRequestForSupply.ItePurchaseOrder
                    ## update "IteRequestForSupply" set "ItePurchaseOrder" = '222333' where "Id" = 'cc6d65ca-f522-4f57-8854-2d76042be4a8';
                    ## select * from "IteRequestForSupply" where "Id" = 'cc6d65ca-f522-4f57-8854-2d76042be4a8'
                    "EBELP": "10",
                    # // Позиция заказа  (на поставку, перемещение) == IteRequestForSupplyAsset.ItePositionNumber

                    "WERKS": "Тестовый завод",  # // Завод
                    "LGORT": "Тестовый склад",  # // Склад
                    "CHARG": "4",  # // Номер партии == IteRequestForSupplyAsset.IteInstance
                    "PS_PSP_PNR": "456456456",  # // Код СПП-Элемента == IteRequestForSupplyAsset.ItePPStructure

                    ## "UMWRK": "string",  # // Завод-получатель == IteRequestForSupplyAsset.ItePlantCode
                    ## "UMLGO": "string",  # // Принимающий склад == IteRequestForSupplyAsset.IteWHCode
                    #
                    #
                    #
                    ## "ACT-ID": "string",  # // Предварительный документ списания
                    ## "ACT_POS": "int",  # // Позиция предварительного акта списания
                    ## "MBLNR": "string",  # // Номер документа  материала
                    ## "MJAHR": "int",  # // Год документа материала
                    #
                    #
                    #
                    ## "EBELP_IT": "int",  # // Позиция запроса на перемещение в СУИТА
                    #
                    #
                    #
                    ## "VGART": "string",  # // Вид операции
                    ## "BLART": "string",  # // Вид документа
                    # "BUDAT": "date",  # // Дата проводки в документе (поступления, перемещения, отпуска)
                    # "ZEILE": "int",  # // Позиция документа материала
                    #
                    #
                    #
                    # "ZZ_KLASS": "string",  # // Класс оценки
                    # "MATNR": "string",  # // № материала в SAP
                    # "MENGE": "int",  # // Количество материала в БЕИ
                    # "MEINS": "string",  # // Базовая Единица измерения
                    # "ERFMG": "int",  # // Количество в ЕИ ввода/заказа
                    # "ERFME": "string",  # // Единица измерения материала ввода/заказа
                    # "LIFNR": "string",  # // Поставщик
                    #
                    # "BSART": "string",  # // Вид заказа (на поставку, перемещение)
                    #
                    #
                    #
                    # "ВИД ОЦЕНКИ": "string",  # // Вид оценки 25.11.2021 И.Дернов - добавлено
                    # "FISTL": "string",  # // ПФМ
                    # "GEBER": "string",  # // Фонд
                    # "FIPOS": "string",  # // Финансовая позиция
                    # "VFDAT": "date",  # // Срок хранения партии
                    # "ANLN1": "string",  # // Номер карточки ОС (при списании на ОС)
                    # "KOSTL": "string",  # // МВЗ (при списании на МВЗ)
                    # "AUFNR": "string",  # // Номер заказа (при списании на заказ)
                    # "SMBLN": "string",  # // Номер сорнируемого документа
                    # "DMBTR": "double",  # // Стоимоcть
                    # "XBLNR_MKPF": "string",  # // Номер документа заголовка
                    # "ARC_DOC_ID": "string",  # // Ссылка на скан в ЭХД

                    "deleted": ""  # // X - удалено, "" - новый или измененный
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        assert obj['message'] is None, f"The value of 'message' is not correct"
        assert obj['error'] is None, obj['error']

    # Обработка ошибки item.BWART == 101 и item.EBELN_IT != Null, и нет совпадений со сборочным ключом из полей item.EBELN_IT и item.EBELP_IT
    @allure.description('Обработка ошибки item.BWART == 101 и item.EBELN_IT != Null, и нет совпадений со сборочным ключом из полей item.EBELN_IT и item.EBELP_IT')
    def test_three_break_responce(self):
        json_data = {
            "currentPage": "1",  # //текущая страница
            "pageCount": "1",  # //количество страниц
            "delta": "D",  # // F - режим полной выгрузки справочника, D - дельта (по умолчанию)
            "item": [  # //элементы справочника
                {
                    "row": "1",  # // Номер строки в коллекции
                    "BWART": "101",  # // Вид движения
                    "EBELN_IT": "None",  # // Номер запроса на перемещение в СУИТА (Прием актива)
                    "EBELN": "222333",
                    # // Номер заказа  (на поставку, перемещение) == IteRequestForSupply.ItePurchaseOrder
                    ## update "IteRequestForSupply" set "ItePurchaseOrder" = '222333' where "Id" = 'cc6d65ca-f522-4f57-8854-2d76042be4a8';
                    ## select * from "IteRequestForSupply" where "Id" = 'cc6d65ca-f522-4f57-8854-2d76042be4a8'
                    "EBELP": "10",
                    # // Позиция заказа  (на поставку, перемещение) == IteRequestForSupplyAsset.ItePositionNumber

                    "WERKS": "Тестовый завод",  # // Завод
                    "LGORT": "Тестовый склад",  # // Склад
                    "CHARG": "4",  # // Номер партии == IteRequestForSupplyAsset.IteInstance
                    "PS_PSP_PNR": "456456456",  # // Код СПП-Элемента == IteRequestForSupplyAsset.ItePPStructure

                    ## "UMWRK": "string",  # // Завод-получатель == IteRequestForSupplyAsset.ItePlantCode
                    ## "UMLGO": "string",  # // Принимающий склад == IteRequestForSupplyAsset.IteWHCode
                    #
                    #
                    #
                    ## "ACT-ID": "string",  # // Предварительный документ списания
                    ## "ACT_POS": "int",  # // Позиция предварительного акта списания
                    ## "MBLNR": "string",  # // Номер документа  материала
                    ## "MJAHR": "int",  # // Год документа материала
                    #
                    #
                    #
                    ## "EBELP_IT": "int",  # // Позиция запроса на перемещение в СУИТА
                    #
                    #
                    #
                    ## "VGART": "string",  # // Вид операции
                    ## "BLART": "string",  # // Вид документа
                    # "BUDAT": "date",  # // Дата проводки в документе (поступления, перемещения, отпуска)
                    # "ZEILE": "int",  # // Позиция документа материала
                    #
                    #
                    #
                    # "ZZ_KLASS": "string",  # // Класс оценки
                    # "MATNR": "string",  # // № материала в SAP
                    # "MENGE": "int",  # // Количество материала в БЕИ
                    # "MEINS": "string",  # // Базовая Единица измерения
                    # "ERFMG": "int",  # // Количество в ЕИ ввода/заказа
                    # "ERFME": "string",  # // Единица измерения материала ввода/заказа
                    # "LIFNR": "string",  # // Поставщик
                    #
                    # "BSART": "string",  # // Вид заказа (на поставку, перемещение)
                    #
                    #
                    #
                    # "ВИД ОЦЕНКИ": "string",  # // Вид оценки 25.11.2021 И.Дернов - добавлено
                    # "FISTL": "string",  # // ПФМ
                    # "GEBER": "string",  # // Фонд
                    # "FIPOS": "string",  # // Финансовая позиция
                    # "VFDAT": "date",  # // Срок хранения партии
                    # "ANLN1": "string",  # // Номер карточки ОС (при списании на ОС)
                    # "KOSTL": "string",  # // МВЗ (при списании на МВЗ)
                    # "AUFNR": "string",  # // Номер заказа (при списании на заказ)
                    # "SMBLN": "string",  # // Номер сорнируемого документа
                    # "DMBTR": "double",  # // Стоимоcть
                    # "XBLNR_MKPF": "string",  # // Номер документа заголовка
                    # "ARC_DOC_ID": "string",  # // Ссылка на скан в ЭХД

                    "deleted": ""  # // X - удалено, "" - новый или измененный
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        assert obj['message'] is None, f"The value of 'message' is not correct"
        assert obj['error'] is None, obj['error']

    # Обработка ошибки item.BWART == (941 или 291 или 261) и (item.ACT-ID == Null или item.ACT_POS == Null)
    @allure.description('Обработка ошибки item.BWART == (941 или 291 или 261) и (item.ACT-ID == Null или item.ACT_POS == Null)')
    def test_four_responce(self):
        json_data = {
            "currentPage": "1",  # //текущая страница
            "pageCount": "1",  # //количество страниц
            "delta": "D",  # // F - режим полной выгрузки справочника, D - дельта (по умолчанию)
            "item": [  # //элементы справочника
                {
                    "row": "1",  # // Номер строки в коллекции
                    "BWART": "941",  # // Вид движения (941 или 291 или 261)
                    "ACT-ID": None,  # // Предварительный документ списания == iteRequestForCommissioningAsset.itePreWriteoffDocumentNumber
                    "ACT_POS": "1",  # // Позиция предварительного акта списания == IteRequestForCommissioningAsset.itePreWriteoffDocumentPos

    # update "IteRequestForCommissioningAsset" set "ItePreWriteoffDocumentNumber" = '1111' where "Id" = 'dbb5cebc-423e-4bef-8ba5-dbe2c6066c8a';
    # update "IteRequestForCommissioningAsset" set "ItePreWriteoffDocumentPos" = '1' where "Id" = 'dbb5cebc-423e-4bef-8ba5-dbe2c6066c8a';
    # select * from  "IteRequestForCommissioningAsset" where "Id" = 'dbb5cebc-423e-4bef-8ba5-dbe2c6066c8a'

                    "MBLNR": "123123",  # // Номер документа  материала == iteRequestForCommissioningAsset.iteWriteoffDocumentNumber
                    "MJAHR": "2020",  # // Год документа материала == iteRequestForCommissioningAsset.iteWriteoffDocumentDate


                    # "EBELN_IT ": "string",  # // Номер запроса на перемещение в СУИТА
                    # "EBELP_IT": "int",  # // Позиция запроса на перемещение в СУИТА
                    # "UMWRK": "string",  # // Завод-получатель
                    # "UMLGO": "string",  # // Принимающий склад
                    #
                    #
                    # "VGART": "string",  # // Вид операции
                    # "BLART": "string",  # // Вид документа
                    # "BUDAT": "date",  # // Дата проводки в документе (поступления, перемещения, отпуска)
                    # "ZEILE": "int",  # // Позиция документа материала
                    #
                    # "WERKS": "string",  # // Завод
                    # "LGORT": "string",  # // Склад
                    # "CHARG": "string",  # // Номер партии
                    # "ZZ_KLASS": "string",  # // Класс оценки
                    # "MATNR": "string",  # // № материала в SAP
                    # "MENGE": "int",  # // Количество материала в БЕИ
                    # "MEINS": "string",  # // Базовая Единица измерения
                    # "ERFMG": "int",  # // Количество в ЕИ ввода/заказа
                    # "ERFME": "string",  # // Единица измерения материала ввода/заказа
                    # "LIFNR": "string",  # // Поставщик
                    # "EBELN": "string",  # // Номер заказа  (на поставку, перемещение)
                    # "BSART": "string",  # // Вид заказа (на поставку, перемещение)
                    # "EBELP": "int",  # // Позиция заказа  (на поставку, перемещение)
                    #
                    # "PS_PSP_PNR": "string",  # // Код СПП-Элемента
                    # "ВИД ОЦЕНКИ": "string",  # // Вид оценки 25.11.2021 И.Дернов - добавлено
                    # "FISTL": "string",  # // ПФМ
                    # "GEBER": "string",  # // Фонд
                    # "FIPOS": "string",  # // Финансовая позиция
                    # "VFDAT": "date",  # // Срок хранения партии
                    # "ANLN1": "string",  # // Номер карточки ОС (при списании на ОС)
                    # "KOSTL": "string",  # // МВЗ (при списании на МВЗ)
                    # "AUFNR": "string",  # // Номер заказа (при списании на заказ)
                    # "SMBLN": "string",  # // Номер сорнируемого документа
                    # "DMBTR": "double",  # // Стоимоcть
                    # "XBLNR_MKPF": "string",  # // Номер документа заголовка
                    # "ARC_DOC_ID": "string",  # // Ссылка на скан в ЭХД

                    "deleted": ""  # // X - удалено, "" - новый или измененный
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        assert obj['message'] is None, f"The value of 'message' is not correct"
        assert obj['error'] is None, obj['error']

    # Обработка ошибки item.BWART == (941 или 291 или 261) и нет совпадений со сборочным ключом из полей  item.ACT-ID и item.ACT_POS
    @allure.description('Обработка ошибки item.BWART == (941 или 291 или 261) и нет совпадений со сборочным ключом из полей  item.ACT-ID и item.ACT_POS')
    def test_five_responce(self):
        json_data = {
            "currentPage": "1",  # //текущая страница
            "pageCount": "1",  # //количество страниц
            "delta": "D",  # // F - режим полной выгрузки справочника, D - дельта (по умолчанию)
            "item": [  # //элементы справочника
                {
                    "row": "1",  # // Номер строки в коллекции
                    "BWART": "941",  # // Вид движения (941 или 291 или 261)
                    "ACT-ID": "111fgdd",  # // Предварительный документ списания == iteRequestForCommissioningAsset.itePreWriteoffDocumentNumber
                    "ACT_POS": "1",  # // Позиция предварительного акта списания == IteRequestForCommissioningAsset.itePreWriteoffDocumentPos

    # update "IteRequestForCommissioningAsset" set "ItePreWriteoffDocumentNumber" = '1111' where "Id" = 'dbb5cebc-423e-4bef-8ba5-dbe2c6066c8a';
    # update "IteRequestForCommissioningAsset" set "ItePreWriteoffDocumentPos" = '1' where "Id" = 'dbb5cebc-423e-4bef-8ba5-dbe2c6066c8a';
    # select * from  "IteRequestForCommissioningAsset" where "Id" = 'dbb5cebc-423e-4bef-8ba5-dbe2c6066c8a'

                    "MBLNR": "123123",  # // Номер документа  материала == iteRequestForCommissioningAsset.iteWriteoffDocumentNumber
                    "MJAHR": "2020",  # // Год документа материала == iteRequestForCommissioningAsset.iteWriteoffDocumentDate


                    # "EBELN_IT ": "string",  # // Номер запроса на перемещение в СУИТА
                    # "EBELP_IT": "int",  # // Позиция запроса на перемещение в СУИТА
                    # "UMWRK": "string",  # // Завод-получатель
                    # "UMLGO": "string",  # // Принимающий склад
                    #
                    #
                    # "VGART": "string",  # // Вид операции
                    # "BLART": "string",  # // Вид документа
                    # "BUDAT": "date",  # // Дата проводки в документе (поступления, перемещения, отпуска)
                    # "ZEILE": "int",  # // Позиция документа материала
                    #
                    # "WERKS": "string",  # // Завод
                    # "LGORT": "string",  # // Склад
                    # "CHARG": "string",  # // Номер партии
                    # "ZZ_KLASS": "string",  # // Класс оценки
                    # "MATNR": "string",  # // № материала в SAP
                    # "MENGE": "int",  # // Количество материала в БЕИ
                    # "MEINS": "string",  # // Базовая Единица измерения
                    # "ERFMG": "int",  # // Количество в ЕИ ввода/заказа
                    # "ERFME": "string",  # // Единица измерения материала ввода/заказа
                    # "LIFNR": "string",  # // Поставщик
                    # "EBELN": "string",  # // Номер заказа  (на поставку, перемещение)
                    # "BSART": "string",  # // Вид заказа (на поставку, перемещение)
                    # "EBELP": "int",  # // Позиция заказа  (на поставку, перемещение)
                    #
                    # "PS_PSP_PNR": "string",  # // Код СПП-Элемента
                    # "ВИД ОЦЕНКИ": "string",  # // Вид оценки 25.11.2021 И.Дернов - добавлено
                    # "FISTL": "string",  # // ПФМ
                    # "GEBER": "string",  # // Фонд
                    # "FIPOS": "string",  # // Финансовая позиция
                    # "VFDAT": "date",  # // Срок хранения партии
                    # "ANLN1": "string",  # // Номер карточки ОС (при списании на ОС)
                    # "KOSTL": "string",  # // МВЗ (при списании на МВЗ)
                    # "AUFNR": "string",  # // Номер заказа (при списании на заказ)
                    # "SMBLN": "string",  # // Номер сорнируемого документа
                    # "DMBTR": "double",  # // Стоимоcть
                    # "XBLNR_MKPF": "string",  # // Номер документа заголовка
                    # "ARC_DOC_ID": "string",  # // Ссылка на скан в ЭХД

                    "deleted": ""  # // X - удалено, "" - новый или измененный
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        assert obj['message'] is None, f"The value of 'message' is not correct"
        assert obj['error'] is None, obj['error']

    # Обработка ошибки item.BWART == 101 и item.EBELN_IT == Null, и нет совпадений со сборочным ключом из полей item.EBELN и item.EBELP
    @allure.description('Обработка ошибки item.BWART == 101 и item.EBELN_IT == Null, и нет совпадений со сборочным ключом из полей item.EBELN и item.EBELP')
    def test_six_responce(self):
        json_data = {
            "currentPage": "2",  # //текущая страница
            "pageCount": "1",  # //количество страниц
            "delta": "D",  # // F - режим полной выгрузки справочника, D - дельта (по умолчанию)
            "item": [  # //элементы справочника
                {
                    "row": "1",  # // Номер строки в коллекции
                    "BWART": "101",  # // Вид движения
                    "EBELN_IT": None,  # // Номер запроса на перемещение в СУИТА (Прием актива)
                    "EBELN": "222333343",  # // Номер заказа  (на поставку, перемещение) == IteRequestForSupply.ItePurchaseOrder
                    ## update "IteRequestForSupply" set "ItePurchaseOrder" = '222333' where "Id" = 'cc6d65ca-f522-4f57-8854-2d76042be4a8';
                    ## select * from "IteRequestForSupply" where "Id" = 'cc6d65ca-f522-4f57-8854-2d76042be4a8'
                    "EBELP": "10",  # // Позиция заказа  (на поставку, перемещение) == IteRequestForSupplyAsset.ItePositionNumber

                    "WERKS": "Тестовый завод",  # // Завод
                    "LGORT": "Тестовый склад",  # // Склад
                    "CHARG": "4",  # // Номер партии == IteRequestForSupplyAsset.IteInstance
                    "PS_PSP_PNR": "456456456",  # // Код СПП-Элемента == IteRequestForSupplyAsset.ItePPStructure

                    ## "UMWRK": "string",  # // Завод-получатель == IteRequestForSupplyAsset.ItePlantCode
                    ## "UMLGO": "string",  # // Принимающий склад == IteRequestForSupplyAsset.IteWHCode
                    #
                    #
                    #
                    ## "ACT-ID": "string",  # // Предварительный документ списания
                    ## "ACT_POS": "int",  # // Позиция предварительного акта списания
                    ## "MBLNR": "string",  # // Номер документа  материала
                    ## "MJAHR": "int",  # // Год документа материала
                    #
                    #
                    #
                    ## "EBELP_IT": "int",  # // Позиция запроса на перемещение в СУИТА
                    #
                    #
                    #
                    ## "VGART": "string",  # // Вид операции
                    ## "BLART": "string",  # // Вид документа
                    # "BUDAT": "date",  # // Дата проводки в документе (поступления, перемещения, отпуска)
                    # "ZEILE": "int",  # // Позиция документа материала
                    #
                    #
                    #
                    # "ZZ_KLASS": "string",  # // Класс оценки
                    # "MATNR": "string",  # // № материала в SAP
                    # "MENGE": "int",  # // Количество материала в БЕИ
                    # "MEINS": "string",  # // Базовая Единица измерения
                    # "ERFMG": "int",  # // Количество в ЕИ ввода/заказа
                    # "ERFME": "string",  # // Единица измерения материала ввода/заказа
                    # "LIFNR": "string",  # // Поставщик
                    #
                    # "BSART": "string",  # // Вид заказа (на поставку, перемещение)
                    #
                    #
                    #
                    # "ВИД ОЦЕНКИ": "string",  # // Вид оценки 25.11.2021 И.Дернов - добавлено
                    # "FISTL": "string",  # // ПФМ
                    # "GEBER": "string",  # // Фонд
                    # "FIPOS": "string",  # // Финансовая позиция
                    # "VFDAT": "date",  # // Срок хранения партии
                    # "ANLN1": "string",  # // Номер карточки ОС (при списании на ОС)
                    # "KOSTL": "string",  # // МВЗ (при списании на МВЗ)
                    # "AUFNR": "string",  # // Номер заказа (при списании на заказ)
                    # "SMBLN": "string",  # // Номер сорнируемого документа
                    # "DMBTR": "double",  # // Стоимоcть
                    # "XBLNR_MKPF": "string",  # // Номер документа заголовка
                    # "ARC_DOC_ID": "string",  # // Ссылка на скан в ЭХД

                    "deleted": ""  # // X - удалено, "" - новый или измененный
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        assert obj['message'] is None, f"The value of 'message' is not correct"
        assert obj['error'] is None, obj['error']

    # Обработка ошибки item.BWART == Null
    @allure.description('Обработка ошибки item.BWART == Null')
    def test_seven_responce(self):
        json_data = {
            "currentPage": "1",  # //текущая страница
            "pageCount": "1",  # //количество страниц
            "delta": "D",  # // F - режим полной выгрузки справочника, D - дельта (по умолчанию)
            "item": [  # //элементы справочника
                {
                    "row": "1",  # // Номер строки в коллекции
                    "BWART": None,  # // Вид движения == 101
                    "EBELN_IT": "RM00000174",
                    # // Номер запроса на перемещение в СУИТА == IteRequestForMoving.IteNumber
                    "EBELP_IT": "1",
                    # // Позиция запроса на перемещение в СУИТА == IteRequestForMovingAsset.ItePositionNumber
                    # "UMWRK": "1001",  # // Завод-получатель == IteAsset.ItePlantCode
                    # "UMLGO": "82232ad9-81bf-4885-a80d-f0691ed07129",  # // Принимающий склад == IteAsset.IteLogisticStructure
                    # Если поля не заполнены то пишем скрипт
                    # update "IteAsset" set "IteLogisticStructureId" = '82232ad9-81bf-4885-a80d-f0691ed07129' where "Id" = 'bffee4a4-a53c-487d-a74d-dafd37098819';
                    # update "IteAsset" set "ItePlantCode" = '1001' where "Id" = 'bffee4a4-a53c-487d-a74d-dafd37098819';
                    # select * from  "IteAsset" where "Id" = 'bffee4a4-a53c-487d-a74d-dafd37098819'

                    "MBLNR": "0000000",  # // Номер документа  материала == IteRequestForMovingAsset.IteDocSAP
                    # "MJAHR": "int",  # // Год документа материала
                    # "VGART": "string",  # // Вид операции
                    # "BLART": "string",  # // Вид документа
                    "BUDAT": "11.07.2022",
                    # // Дата проводки в документе (поступления, перемещения, отпуска) == IteRequestForMovingAsset.IteOrderPostingDate
                    "ZEILE": "1",  # // Позиция документа материала == IteRequestForMovingAsset.IteOrderPosSAP
                    #
                    "WERKS": "1001",  # // Завод == IteAsset.ItePlantCode
                    "LGORT": "0008",  # // Склад == IteAsset.IteLogisticStructure
                    # "CHARG": "string",  # // Номер партии
                    # "ZZ_KLASS": "string",  # // Класс оценки
                    # "MATNR": "string",  # // № материала в SAP
                    # "MENGE": "int",  # // Количество материала в БЕИ
                    # "MEINS": "string",  # // Базовая Единица измерения
                    # "ERFMG": "int",  # // Количество в ЕИ ввода/заказа
                    # "ERFME": "string",  # // Единица измерения материала ввода/заказа
                    # "LIFNR": "string",  # // Поставщик
                    # "EBELN": "string",  # // Номер заказа  (на поставку, перемещение)
                    # "BSART": "string",  # // Вид заказа (на поставку, перемещение)
                    # "EBELP": "int",  # // Позиция заказа  (на поставку, перемещение)
                    #
                    # "PS_PSP_PNR": "string",  # // Код СПП-Элемента
                    # "ВИД ОЦЕНКИ": "string",  # // Вид оценки 25.11.2021 И.Дернов - добавлено
                    # "FISTL": "string",  # // ПФМ
                    # "GEBER": "string",  # // Фонд
                    # "FIPOS": "string",  # // Финансовая позиция
                    # "VFDAT": "date",  # // Срок хранения партии
                    # "ANLN1": "string",  # // Номер карточки ОС (при списании на ОС)
                    # "KOSTL": "string",  # // МВЗ (при списании на МВЗ)
                    # "AUFNR": "string",  # // Номер заказа (при списании на заказ)
                    # "SMBLN": "string",  # // Номер сорнируемого документа
                    # "DMBTR": "double",  # // Стоимоcть
                    # "XBLNR_MKPF": "string",  # // Номер документа заголовка
                    # "ARC_DOC_ID": "string",  # // Ссылка на скан в ЭХД
                    # "ACT-ID": "string",  # // Предварительный документ списания
                    # "ACT_POS": "int",  # // Позиция предварительного акта списания
                    "deleted": ""  # // X - удалено, "" - новый или измененный
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        assert obj['message'] is None, f"The value of 'message' is not correct"
        assert obj['error'] is None, obj['error']

    # Обработка ошибки currentPage>pageCount
    @allure.description('Обработка ошибки currentPage>pageCount')
    def test_eight_responce(self):
        json_data = {
            "currentPage": "2",  # //текущая страница
            "pageCount": "1",  # //количество страниц
            "delta": "D",  # // F - режим полной выгрузки справочника, D - дельта (по умолчанию)
            "item": [  # //элементы справочника
                {
                    "row": "1",  # // Номер строки в коллекции
                    "BWART": '101',  # // Вид движения == 101
                    "EBELN_IT": "RM00000174",
                    # // Номер запроса на перемещение в СУИТА == IteRequestForMoving.IteNumber
                    "EBELP_IT": "1",
                    # // Позиция запроса на перемещение в СУИТА == IteRequestForMovingAsset.ItePositionNumber
                    # "UMWRK": "1001",  # // Завод-получатель == IteAsset.ItePlantCode
                    # "UMLGO": "82232ad9-81bf-4885-a80d-f0691ed07129",  # // Принимающий склад == IteAsset.IteLogisticStructure
                    # Если поля не заполнены то пишем скрипт
                    # update "IteAsset" set "IteLogisticStructureId" = '82232ad9-81bf-4885-a80d-f0691ed07129' where "Id" = 'bffee4a4-a53c-487d-a74d-dafd37098819';
                    # update "IteAsset" set "ItePlantCode" = '1001' where "Id" = 'bffee4a4-a53c-487d-a74d-dafd37098819';
                    # select * from  "IteAsset" where "Id" = 'bffee4a4-a53c-487d-a74d-dafd37098819'

                    "MBLNR": "0000000",  # // Номер документа  материала == IteRequestForMovingAsset.IteDocSAP
                    # "MJAHR": "int",  # // Год документа материала
                    # "VGART": "string",  # // Вид операции
                    # "BLART": "string",  # // Вид документа
                    "BUDAT": "11.07.2022",
                    # // Дата проводки в документе (поступления, перемещения, отпуска) == IteRequestForMovingAsset.IteOrderPostingDate
                    "ZEILE": "1",  # // Позиция документа материала == IteRequestForMovingAsset.IteOrderPosSAP
                    #
                    "WERKS": "1001",  # // Завод == IteAsset.ItePlantCode
                    "LGORT": "0008",  # // Склад == IteAsset.IteLogisticStructure
                    # "CHARG": "string",  # // Номер партии
                    # "ZZ_KLASS": "string",  # // Класс оценки
                    # "MATNR": "string",  # // № материала в SAP
                    # "MENGE": "int",  # // Количество материала в БЕИ
                    # "MEINS": "string",  # // Базовая Единица измерения
                    # "ERFMG": "int",  # // Количество в ЕИ ввода/заказа
                    # "ERFME": "string",  # // Единица измерения материала ввода/заказа
                    # "LIFNR": "string",  # // Поставщик
                    # "EBELN": "string",  # // Номер заказа  (на поставку, перемещение)
                    # "BSART": "string",  # // Вид заказа (на поставку, перемещение)
                    # "EBELP": "int",  # // Позиция заказа  (на поставку, перемещение)
                    #
                    # "PS_PSP_PNR": "string",  # // Код СПП-Элемента
                    # "ВИД ОЦЕНКИ": "string",  # // Вид оценки 25.11.2021 И.Дернов - добавлено
                    # "FISTL": "string",  # // ПФМ
                    # "GEBER": "string",  # // Фонд
                    # "FIPOS": "string",  # // Финансовая позиция
                    # "VFDAT": "date",  # // Срок хранения партии
                    # "ANLN1": "string",  # // Номер карточки ОС (при списании на ОС)
                    # "KOSTL": "string",  # // МВЗ (при списании на МВЗ)
                    # "AUFNR": "string",  # // Номер заказа (при списании на заказ)
                    # "SMBLN": "string",  # // Номер сорнируемого документа
                    # "DMBTR": "double",  # // Стоимоcть
                    # "XBLNR_MKPF": "string",  # // Номер документа заголовка
                    # "ARC_DOC_ID": "string",  # // Ссылка на скан в ЭХД
                    # "ACT-ID": "string",  # // Предварительный документ списания
                    # "ACT_POS": "int",  # // Позиция предварительного акта списания
                    "deleted": ""  # // X - удалено, "" - новый или измененный
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)

        print(response.text)

        obj = json.loads(response.text)
        assert obj['message'] is None, f"The value of 'message' is not correct"
        assert obj['error'] is None, obj['error']
