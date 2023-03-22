import allure
import pytest

from api.BoardAPI import BoardAPI
from api.CardAPI import CardAPI
from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider

@pytest.fixture
def api_client() -> BoardAPI:
    with allure.step("Создать экземпляр класса BoardAPI"):
        return BoardAPI(
            ConfigProvider().get_api_url(),
            DataProvider().get_token())

@pytest.fixture
def api_client_no_auth() -> BoardAPI:
    with allure.step("Создать экземпляр класса BoardAPI без авторизации"):
        return BoardAPI(ConfigProvider().get("api", "base_url"), "")

@pytest.fixture
def dummy_board_id(api_client: BoardAPI) -> str:    
    with allure.step("Предварительно создать доску. Количество колонок по умолчанию - три"):
        resp = api_client.create_board("Board to be deleted").get("id")
        return resp

@pytest.fixture
def delete_board(api_client: BoardAPI) -> str:
    dictionary = {"board_id": ""}
    yield dictionary
    with allure.step("Получить id доски для её удаления"):
        board_id = dictionary.get("board_id")
    with allure.step("Удалить доску после теста"):
        api_client.delete_board_by_id(board_id)

@pytest.fixture
def test_data():
    with allure.step("Получить тестовые данные"):
        return DataProvider()

@pytest.fixture
def dummy_board(api_client: BoardAPI) -> str:
    with allure.step("Предварительно создать доску. Количество колонок по умолчанию - три"):
        resp = api_client.create_board("Board to be deleted").get("id")

        yield resp

    with allure.step("Удалить доску после теста"):
        api_client.delete_board_by_id(resp)    

@pytest.fixture
def lists_on_board(api_client: BoardAPI, dummy_board: str) -> dict:   
    lists_on_board = api_client.get_lists_by_board_id(dummy_board)

    with allure.step("Получить id колонок на доске"):    
        lists = {
            'list_one_id': lists_on_board[0]["id"],
            'list_two_id': lists_on_board[1]["id"],
            'list_three_id': lists_on_board[2]["id"]
        }

    with allure.step("перейти к удалению доски"):    
        yield lists  

@pytest.fixture
def api_card_client() -> CardAPI:
    with allure.step("Создать экземпляр класса CardAPI"):
        return CardAPI(
            ConfigProvider().get("api", "base_url"),
            DataProvider().get_token())

@pytest.fixture
def dummy_card_id(api_card_client: CardAPI, lists_on_board: dict) -> str:
    list_one_id = lists_on_board['list_one_id']

    with allure.step("Предварительно создать карточку"):
        resp = api_card_client.create_card(list_one_id, "Card to be update and deleted").get("id")

        return resp

@pytest.fixture
def get_lists_on_board_by_dummy_card_id(api_client: BoardAPI, api_card_client: CardAPI, dummy_card_id: str) -> dict:
    with allure.step("Получить id доски, на которой расположена карточка"):    
        board_id_of_card = api_card_client.get_card_info(dummy_card_id)["idBoard"]

    with allure.step("Получить список колонок на доске, на которой расположена карточка"):    
        lists_on_board = api_client.get_lists_by_board_id(board_id_of_card)    

    with allure.step("Получить id колонок на доске, на которой расположена карточка"):    
        lists = {
            'list_one_id': lists_on_board[0]["id"],
            'list_two_id': lists_on_board[1]["id"],
            'list_three_id': lists_on_board[2]["id"]
        }
        return lists