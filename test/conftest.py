import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from api.BoardAPI import BoardAPI
from api.CardAPI import CardAPI
from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider

# @pytest.fixture
# def browser():
#     with allure.step("Открыть и настроить браузер"):
#         timeout = ConfigProvider().get("ui", "timeout")
#         browser_name = ConfigProvider().get("ui", "browser_name")

#         if browser_name == "chrome":
#             browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         else:
#             browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

#         browser.implicitly_wait(timeout)
#         browser.maximize_window()
#         yield browser

#     with allure.step("Закрыть браузер"):
#         browser.quit()

@pytest.fixture
def api_client() -> BoardAPI:
    return BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")
    # return BoardAPI(
    #     ConfigProvider().get("api", "base_url"),
    #     DataProvider().get_token())

@pytest.fixture
def api_client_no_auth() -> BoardAPI:
    return BoardAPI(ConfigProvider().get("api", "base_url"), "")

@pytest.fixture
def dummy_board_id(api_client: BoardAPI) -> str:
    # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

    # api = BoardAPI(
    #     ConfigProvider().get("api", "base_url"),
    #     DataProvider().get_token())
    
    with allure.step("Предварительно создать доску"):
        resp = api_client.create_board("Board to be deleted").get("id")
        return resp

@pytest.fixture
def delete_board(api_client: BoardAPI) -> str:
    dictionary = {"board_id": ""}
    yield dictionary
    # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")
    # api = BoardAPI(
    #     ConfigProvider().get("api", "base_url"),
    #     DataProvider().get_token())
    
    with allure.step("Удалить доску после теста"):
        api_client.delete_board_by_id(dictionary.get("board_id"))

@pytest.fixture
def test_data():
    return DataProvider()

# ####################################################################

@pytest.fixture
def lists_on_board(api_client: BoardAPI, dummy_board_id: str) -> list:
    lists = {
        'list_one_id': '',
        'list_two_id': '',
        'list_three_id': ''
    }
    lists_on_board = api_client.get_lists_by_board_id(dummy_board_id)
    # print(x)
    # print("\nпервая колонка: id - " + x[0]["id"] + ", " + "name - " + x[0]["name"])
    # print("вторая колонка: id - " + x[1]["id"] + ", " + "name - " + x[1]["name"])
    # print("третья колонка: id - " + x[2]["id"] + ", " + "name - " + x[2]["name"])
    lists["list_one_id"] = lists_on_board[0]["id"]
    lists["list_two_id"] = lists_on_board[1]["id"]
    lists["list_three_id"] = lists_on_board[2]["id"]
    return lists

# @pytest.fixture
# def list_one_id(api_client: BoardAPI, lists_on_board: list) -> dict:
#     return lists_on_board[0]["id"]

# @pytest.fixture
# def list_two_id(api_client: BoardAPI, lists_on_board: list) -> dict:
#     return lists_on_board[1]["id"]

# @pytest.fixture
# def list_three_id(api_client: BoardAPI, lists_on_board: list) -> dict:
#     return lists_on_board[2]["id"]





# @pytest.fixture
# def lists_id(api_client: BoardAPI, dummy_board_id: str) -> dict:
#     dictionary = {"first_list_id": "",
#                   "second_list_id": ""
#     }
#     # api =  BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")
#     # return BoardAPI(
#     #     ConfigProvider().get("api", "base_url"),
#     #     DataProvider().get_token())

#     # 1. создать доску, получить id доски
#     # with allure.step("Предварительно создать доску"):
#     #     resp_board_id = api.create_board("Board for card").get("id")
#         # return resp_board_id   
     
#     # 2. получить список колонок на доске
#     resp_lists = api_client.get_lists_by_board_id(dummy_board_id)
#     # list_quantity = len(resp_lists)
#     # # 3. получить список id колонок по индексам
#     # for every_list in resp_lists:
#     #     resp_lists[0]["id"]

#     # 4. получить id первой колонки по индексу 0
#     print("\nid первой колонки: " + resp_lists[0]["id"])
#     print("\nid второй колонки: " + resp_lists[1]["id"])

#     dictionary["first_list_id"] = resp_lists[0]["id"]
#     dictionary["second_list_id"] = resp_lists[1]["id"]
#     print("\nсловарь на выходе из фикстуры lists_id:")
#     print(dictionary)
#     return dictionary

#     # 5. в первую колонку в тесте добавить карточку




@pytest.fixture
def api_card_client() -> CardAPI:
    return CardAPI("https://api.trello.com/1", '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E')
    # return CardAPI(
    #     ConfigProvider().get("api", "base_url"),
    #     DataProvider().get_token())

@pytest.fixture
def dummy_card_id(api_card_client: CardAPI, lists_on_board: dict) -> str:
    # api = CardAPI(
    #     ConfigProvider().get("api", "base_url"),
    #     DataProvider().get_token())    
    list_one_id = lists_on_board['list_one_id']
    print("\nid первой колонки в фикстуре dummy_card_id: " + list_one_id)


@pytest.fixture
def dummy_card_id_old(api_card_client: CardAPI, lists_id: dict) -> dict:
    # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

    # api = BoardAPI(
    #     ConfigProvider().get("api", "base_url"),
    #     DataProvider().get_token())
    # with allure.step("Предварительно создать доску"):
    #     resp = api.create_board("Board to be deleted").get("id") 

    list_one_id = lists_id.get('first_list_id')

    print("\nid первой колонки для создания карточки в фикстуре dummy_card_id: " + list_one_id)

    dictionary = {
                  "list_id_for_create_card": list_one_id,
                  "card_id": ""
    }
    print("\nпустой словарь в фикстуре dummy_card_id: ")
    print(dictionary)
    # list_id = lists_id.get("first_list_id")
    with allure.step("Предварительно создать карточку"):
# В СЛЕДУЮЩЕЙ СТРОЧКЕ ПРОБЛЕМА!!!!!!!
        resp = api_card_client.create_card(dictionary.get("list_id_for_create_card"), "Card to be update and deleted").get("id") # !!!!!заменить на значение из словаря!!!!!
        
        print("\nid новой карточки: " + str(resp))
        dictionary["card_id"] = resp


    print("\nсловарь в фикстуре dummy_card_id после добавления в него: card_id")
    print(dictionary)
    return dictionary
    # yield 
    # with allure.step("Удалить доску"):



# @pytest.fixture
# def delete_card(api_card_client: CardAPI):# -> dict:
#     dictionary = {"card_id": ""}
#     yield dictionary
#     # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")
#     # api = BoardAPI(
#     #     ConfigProvider().get("api", "base_url"),
#     #     DataProvider().get_token())
    
#     with allure.step("Удалить карточку после теста"):
#         api_card_client.delete_card_by_id(dictionary.get("card_id"))

# # @pytest.fixture
# # def get_list_id() -> str:
# #     api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

# #     # api = BoardAPI(
# #     #     ConfigProvider().get("api", "base_url"),
# #     #     DataProvider().get_token())
    
# #     with allure.step("Предварительно:"):
# #         with allure.step("Создать доску для карточки"):
# #             board_id = api.create_board("Board_for_card").get("id")
# #         with allure.step("Получить список колонок"):
# #             list_of_lists = api.get_lists_by_board_id(board_id)
# #         with allure.step("Получить id первой колонки"):
# #             resp = list_of_lists[0]["id"]
# #             return resp
#     # yield 
#     # with allure.step("Удалить доску"):



# # @pytest.fixture
# # def update_card(api_card_client: CardAPI, dummy_card_id: dict):
# #     # dictionary = {
# #     #               "list_id": list_id,
# #     #               "card_id": card_id
# #     # }    
# #     dummy_card_id
