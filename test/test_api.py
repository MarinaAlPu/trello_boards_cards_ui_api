import allure
from api.BoardAPI import BoardAPI
from api.CardAPI import CardAPI

import pytest

@pytest.mark.skip()
def test_create_board(api_client: BoardAPI):#, delete_board: dict, test_data: dict):
    # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")
    # board_list = api.get_all_boards_by_org_id("6410e46e85363751e85ab637")#api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637")

    # org_id = test_data.get("org_id")
    board_list_before = api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")#api_client.get_all_boards_by_org_id(org_id)
    print("")
    print("\nсписок досок до добавления (id, name):")
    print(board_list_before)

    print("\nдобавляется доска:")
    resp = api_client.create_board("New new board")#api_client.create_board("New board to be deleted")
    print("id: " + resp.get("id"))
    print("name: " + resp.get("name"))

    # delete_board["board_id"] = resp.get("id")

    board_list_after = api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")# api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637")
    print("\nсписок досок после добавления (id, name):")
    print(board_list_after)

    with allure.step("Проверить, что количество досок стало больше на 1"):
        assert len(board_list_after) - len(board_list_before) == 1

@pytest.mark.skip()
def test_delete_board(api_client: BoardAPI):#, dummy_board_id: str, test_data: dict):
    # org_id = test_data.get("org_id")
    # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")
    
    board_list_before = api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")#api_client.get_all_boards_by_org_id(org_id)
    print("\nсписок досок до удаления (id, name):")
    print(board_list_before)

    api_client.delete_board_by_id("641a1dab48ffba61722c9b52")#api_client.delete_board_by_id(dummy_board_id)

    board_list_after = api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")#api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637")
    print("\nсписок досок после удаления (id, name):")
    print(board_list_after)

    with allure.step("Проверить, что количество досок стало меньше на 1"):
        assert len(board_list_before) - len(board_list_after) == 1

######################################################################################################

@pytest.mark.skip()
def test_create_card(api_client: BoardAPI):
    x = api_client.get_lists_by_board_id("641a1de7b512da1e59c58922")
    # print(x)
    print("\nпервая колонка: id - " + x[0]["id"] + ", " + "name - " + x[0]["name"])
    print("вторая колонка: id - " + x[1]["id"] + ", " + "name - " + x[1]["name"])
    print("третья колонка: id - " + x[2]["id"] + ", " + "name - " + x[2]["name"])

    y = api_client.create_card(x[0]["id"], "New card")
    # print(y)
    print("\nновая карточка: id - " + y["id"] + ", " + "name - " + y["name"])

    q = api_client.get_card_info(y["id"])
    # print(q)
    print("\nинформация о новой карточке: id - " + q["id"] + ", " + "name - " + q["name"] + ", " + "колонка - " + q["idList"] + ", " + "доска - " + q["idBoard"])
    
    xx = api_client.get_lists_by_board_id("641a1de7b512da1e59c58922")

    assert len(xx) - len(x) == 1
    assert q["name"] == "New card"
    assert x[0]["id"] == q["idList"]

@pytest.mark.skip()
def test_update_card(api_client: BoardAPI):
    # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

    resp1 = api_client.get_card_info("641a26192a60d4d132dd1b9a")
    print("\nСтарые данные карточки:")
    print("Старое имя: " + resp1["name"])
    print("Старое описание: " + resp1["desc"])
    print("Старая колонка: " + resp1["idList"])

    resp2 = api_client.update_card("641a26192a60d4d132dd1b9a")
    print("\nБудущие данные карточки:")
    print("Новое имя: " + resp2["name"])
    print("Новое описание: " + resp2["desc"])
    print("Новая колонка: " + resp2["idList"])

    resp3 = api_client.get_card_info("641a26192a60d4d132dd1b9a")
    print("\nНовые данные карточки:")
    print("Новое имя: " + resp3["name"])
    print("Новое описание: " + resp3["desc"])
    print("Новая колонка: " + resp3["idList"])

    assert resp3["name"] == "Card's new name"
    assert resp3["desc"] == "We can change card's description!"
    assert resp3["idList"] == "641a1de8b512da1e59c5892b"

@pytest.mark.skip()
def test_move_card(api_client: BoardAPI):
    # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

    resp = api_client.move_one_card("641a26192a60d4d132dd1b9a")
    print("")
    print("\nновая колонка карточки: " + resp["idList"])

    assert resp["idList"] == "641a1de8b512da1e59c5892a"

@pytest.mark.skip()
def test_delete_card(api_client: BoardAPI):
    # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

    # resp1 = api_client.get_lists_by_board_id("641a1de7b512da1e59c58922")
    # print("\nвсего колонок:")
    # print(len(resp1))
    # print("\nсписок колонок (id, name):")
    # print("первая колонка: " + "id: " + resp1[0]["id"] + ", " + "name: " + resp1[0]["name"])
    # print("вторая колонка: " + "id: " + resp1[1]["id"] + ", " + "name: " + resp1[1]["name"])
    # print("третья колонка: " + "id: " + resp1[2]["id"] + ", " + "name: " + resp1[2]["name"])

    # list_number_1 = resp1[0]
    # print("\nпервая колонка:")
    # print(list_number_1)
    # # print("")
    # # print("id первой колонки: " + list_number_1["id"])

    # list_id = resp1[1]["id"]
    # print("\nid первой колонки:\n" + list_id)
    
    resp2 = api_client.get_cards_by_list_id("641a1de8b512da1e59c5892a")
    print("\nКоличество карточек в колонке " + "641a1de8b512da1e59c5892a" + " до удаления: " + str(len(resp2)))
    print("id первой карточки: " + resp2[0]["id"] + ", " + "name первой карточки: " + resp2[0]["name"])
    # print("id второй карточки: " + resp2[1]["id"] + ", " + "name второй карточки: " + resp2[1]["name"])
    # print("id третьей карточки: " + resp2[2]["id"] + ", " + "name третьей карточки: " + resp2[2]["name"])

    resp3 = api_client.delete_card("641a26192a60d4d132dd1b9a")
    # print("\nДобавится карточка: " + resp3["id"])
    print("\nответ на удаление карточки")
    print(resp3)
    # card_id = resp3["id"]
    # print("\nid новой карточки: " + card_id)

    resp4 = api_client.get_cards_by_list_id("641a1de8b512da1e59c5892a")
    print("\nКоличество карточек в колонке " + "641a1de8b512da1e59c5892a" + " после удаления: " + str(len(resp4)))
    # print("id первой карточки: " + resp4[0]["id"] + ", " + "name первой карточки: " + resp4[0]["name"])
    # print("id второй карточки: " + resp4[1]["id"] + ", " + "name второй карточки: " + resp4[1]["name"])
    # print("id третьей карточки: " + resp4[2]["id"] + ", " + "name третьей карточки: " + resp4[2]["name"])

    assert len(resp2) - len(resp4) == 1

# @pytest.mark.skip()
def test_for_test(api_client: BoardAPI, lists_on_board):
    # x = api_client.lists_on_board
    print("\nКолонки на доске:")
    print(lists_on_board)
    print("\nКолонки на доске поштучно:")
    print(lists_on_board['list_one_id'])
    print(lists_on_board['list_two_id'])
    print(lists_on_board['list_three_id'])

# @pytest.mark.skip()
def test_create_card(api_card_client: CardAPI, dummy_card_id: str):
    print("\nid первой колонки для создания карточки в тесте: " + str(dummy_card_id))
