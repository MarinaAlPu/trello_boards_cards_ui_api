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
        print("\nid новой доски на выходе из фикстуры dummy_board_id")
        print(resp)
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
def dummy_board(api_client: BoardAPI) -> str:
    # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

    # api = BoardAPI(
    #     ConfigProvider().get("api", "base_url"),
    #     DataProvider().get_token())
    
    with allure.step("Предварительно создать доску"):
        resp = api_client.create_board("Board to be deleted").get("id")
        print("\nid новой доски на выходе из фикстуры dummy_board_id")
        print(resp)
        print("\nсейчас пойдём в фикстуру lists_on_board")
        yield resp

        print("\nвернулись из фикстуры lists_on_board")
    with allure.step("Удалить доску после теста"):
        api_client.delete_board_by_id(resp)    

@pytest.fixture
def lists_on_board(api_client: BoardAPI, dummy_board: str) -> dict:
    # lists = {
    #     'list_one_id': '',
    #     'list_two_id': '',
    #     'list_three_id': ''
    # }
    lists_on_board = api_client.get_lists_by_board_id(dummy_board)
    # print(x)
    # print("\nпервая колонка: id - " + x[0]["id"] + ", " + "name - " + x[0]["name"])
    # print("вторая колонка: id - " + x[1]["id"] + ", " + "name - " + x[1]["name"])
    # print("третья колонка: id - " + x[2]["id"] + ", " + "name - " + x[2]["name"])
    # lists["list_one_id"] = lists_on_board[0]["id"]
    # lists["list_two_id"] = lists_on_board[1]["id"]
    # lists["list_three_id"] = lists_on_board[2]["id"]
    lists = {
        'list_one_id': lists_on_board[0]["id"],
        'list_two_id': lists_on_board[1]["id"],
        'list_three_id': lists_on_board[2]["id"]
    }
    print("\nсейчас пойдём в тест test_create_card")
    yield lists
    print("\nвернулись из теста test_create_card")    

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

    # with allure.step("Предварительно создать карточку"):
    resp = api_card_client.create_card(list_one_id, "Card to be update and deleted").get("id") # !!!!!заменить на значение из словаря!!!!!
    print("\nid новой карточки:")
    print(resp)

    # yield 

    return resp

# получить idBoard по id карточки
@pytest.fixture
def get_lists_on_board_by_dummy_card_id(api_client: BoardAPI, api_card_client: CardAPI, dummy_card_id: str) -> dict:
    board_id_of_card = api_card_client.get_card_info(dummy_card_id)["idBoard"]

    lists_on_board = api_client.get_lists_by_board_id(board_id_of_card)

    first_list_id = lists_on_board[0]["id"]
    second_list_id = lists_on_board[1]["id"]    
    third_list_id = lists_on_board[1]["id"]    

    lists = {
        'list_one_id': lists_on_board[0]["id"],
        'list_two_id': lists_on_board[1]["id"],
        'list_three_id': lists_on_board[2]["id"]
    }
    return lists
