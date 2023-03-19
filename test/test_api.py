import allure
from api.BoardAPI import BoardAPI
from pages.BoardPage import BoardPage
import pytest

@pytest.mark.skip()
def test_create_board():#api_client: BoardAPI, delete_board: dict, test_data: dict):
    api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")
    # board_list = api.get_all_boards_by_org_id("6410e46e85363751e85ab637")#api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637")

    # org_id = test_data.get("org_id")
    board_list_before = api.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")#api_client.get_all_boards_by_org_id(org_id)
    print("")
    print("")
    print("список досок до добавления (id, name):")
    print(board_list_before)

    print("")
    print("добавляется доска:")
    resp = api.create_board("New new board")#api_client.create_board("New board to be deleted")
    print("id: " + resp.get("id"))
    print("name: " + resp.get("name"))

    # delete_board["board_id"] = resp.get("id")

    board_list_after = api.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")# api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637")
    print("")
    print("список досок после добавления (id, name):")
    print(board_list_after)

    with allure.step("Проверить, что количество досок стало больше на 1"):
        assert len(board_list_after) - len(board_list_before) == 1

@pytest.mark.skip()
def test_delete_board():#api_client: BoardAPI, dummy_board_id: str, test_data: dict):
    # org_id = test_data.get("org_id")
    api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")
    
    board_list_before = api.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")#api_client.get_all_boards_by_org_id(org_id)
    print("")
    print("список досок до удаления (id, name):")
    print(board_list_before)

    api.delete_board_by_id("64171acf63f840bba4f48896")#api_client.delete_board_by_id(dummy_board_id)

    board_list_after = api.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")#api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637")
    print("")
    print("список досок после удаления (id, name):")
    print(board_list_after)

    with allure.step("Проверить, что количество досок стало меньше на 1"):
        assert len(board_list_before) - len(board_list_after) == 1
    
@pytest.mark.skip()
def test_get_boards():#api_client: BoardAPI
    api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")
    board_list = api.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")#api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637")
    print("")
    print("список досок (id, name):")
    print(board_list)

    
# @pytest.mark.skip()
def test_create_card():
    api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

    resp1 = api.get_lists_by_board_id("64171ae9aec528643874445f")
    # print("")
    # print("всего колонок:")
    # print(len(resp))
    # print("")
    # print("список колонок (id, name):")
    # print("первая колонка: " + "id: " + resp[0]["id"] + ", " + "name: " + resp[0]["name"])
    # print("вторая колонка: " + "id: " + resp[1]["id"] + ", " + "name: " + resp[1]["name"])
    # print("третья колонка: " + "id: " + resp[2]["id"] + ", " + "name: " + resp[2]["name"])

    # list_number_1 = resp[0]
    # print("")
    # print("первая колонка:")
    # print(list_number_1)
    # print("")
    # print("id первой колонки: ") # + list_number_1["id"])

    list_id = resp1[0]["id"]
    print("\nid первой колонки:\n" + list_id)
    
    resp2 = api.create_card(list_id, "Card 2")
    print("Добавится карточка:")
    print(resp2)
    print("id новой карточки:")
    card_id = resp2["id"]
    print(card_id)


    # 1. Создать доску
    # 2. Получить id доски
    # 3. Получить id колонок list (список?)
    # 4. Создать карточку по id колонки
    # 5. Удалить карточку
    # 6. Удалить доску




