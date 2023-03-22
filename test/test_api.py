import allure
from api.BoardAPI import BoardAPI
from api.CardAPI import CardAPI

import pytest

# @pytest.mark.skip()
def test_create_board(api_client: BoardAPI, delete_board: dict):#, test_data: dict
    # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")
    # board_list = api.get_all_boards_by_org_id("6410e46e85363751e85ab637")#api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637")

    # org_id = test_data.get("org_id")
    board_list_before = api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")
    print("")
    print("\nсписок досок до добавления (id, name):")
    print(board_list_before)

    print("\nдобавляется доска:")
    resp = api_client.create_board("New board to be deleted")
    print("id: " + resp.get("id"))
    print("name: " + resp.get("name"))

    delete_board["board_id"] = resp.get("id")

    board_list_after = api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")
    print("\nсписок досок после добавления (id, name):")
    print(board_list_after)

    with allure.step("Проверить, что количество досок стало больше на 1"):
        assert len(board_list_after) - len(board_list_before) == 1

# @pytest.mark.skip()
def test_delete_board(api_client: BoardAPI, dummy_board_id: str):#, test_data: dict):
    # org_id = test_data.get("org_id")
    # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")
    
    board_list_before = api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")#api_client.get_all_boards_by_org_id(org_id)
    print("\nсписок досок до удаления (id, name):")
    print(board_list_before)

    x = api_client.delete_board_by_id(dummy_board_id)
    print("\nответ на запрос на удаление доски:")
    print(x)

    board_list_after = api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")#api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637")
    print("\nсписок досок после удаления (id, name):")
    print(board_list_after)

    with allure.step("Проверить, что количество досок стало меньше на 1"):
        assert len(board_list_before) - len(board_list_after) == 1

######################################################################################################

# @pytest.mark.skip()
def test_create_card(api_card_client: CardAPI, lists_on_board: dict):
    # x = api_client.get_lists_by_board_id("641a1de7b512da1e59c58922")
    # print(x)
    # print("\nпервая колонка: id - " + x[0]["id"] + ", " + "name - " + x[0]["name"])
    # print("вторая колонка: id - " + x[1]["id"] + ", " + "name - " + x[1]["name"])
    # print("третья колонка: id - " + x[2]["id"] + ", " + "name - " + x[2]["name"])

    x = lists_on_board
    print(x)
    print("\nпервая колонка: id - " + x["list_one_id"])
    print("вторая колонка: id - " + x["list_two_id"])
    print("третья колонка: id - " + x["list_three_id"])

# получить количество карточек в первой колонке
    print("\nкарточки в первой колонке до добавления карточки:")
    xx = api_card_client.get_cards_by_list_id(x["list_one_id"])
    print(xx)
    print("\nколичество карточек в первой колонке")
    print(len(xx))

    y = api_card_client.create_card(x["list_one_id"], "New card")
    # print(y)
    print("\nновая карточка: id - " + y["id"] + ", " + "name - " + y["name"])

    q = api_card_client.get_card_info(y["id"])
    # print(q)
    print("\nинформация о новой карточке: id - " + q["id"] + ", " + "name - " + q["name"] + ", " + "колонка - " + q["idList"] + ", " + "доска - " + q["idBoard"])
    
    # xx = api_client.get_lists_by_board_id("641a1de7b512da1e59c58922")

    # получить количество карточек в первой колонке
    print("\nкарточки в первой колонке после добавления карточки:")
    xxx = api_card_client.get_cards_by_list_id(x["list_one_id"])
    print(xxx)
    print("\nколичество карточек в первой колонке")
    print(len(xxx))

    assert len(xxx) - len(xx) == 1
    assert q["name"] == "New card"
    assert x["list_one_id"] == q["idList"]

# @pytest.mark.skip()
def test_update_card(api_card_client: CardAPI, dummy_card_id: str):
    # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

    resp1 = api_card_client.get_card_info(dummy_card_id)
    print("\nСтарые данные карточки:")
    print("Старое имя: " + resp1["name"])
    print("Старое описание: " + resp1["desc"])
    # print("Старая колонка: " + resp1["idList"])

    resp2 = api_card_client.update_card(dummy_card_id)
    print("\nБудущие данные карточки:")
    print("Новое имя: " + resp2["name"])
    print("Новое описание: " + resp2["desc"])
    # print("Новая колонка: " + resp2["idList"])

    resp3 = api_card_client.get_card_info(dummy_card_id)
    print("\nНовые данные карточки:")
    print("Новое имя: " + resp3["name"])
    print("Новое описание: " + resp3["desc"])
    # print("Новая колонка: " + resp3["idList"])

    assert resp3["name"] == "Card's new name"
    assert resp3["desc"] == "We can change card's description!"
    # assert resp3["idList"] != resp1["idList"]

# @pytest.mark.skip()
def test_move_card(api_card_client: CardAPI, dummy_card_id: str, get_lists_on_board_by_dummy_card_id: dict):
    # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

    resp1 = api_card_client.get_card_info(dummy_card_id)
    print("\nСтарые данные карточки:")
    print("Старый id: " + resp1["id"])
    print("Старое имя: " + resp1["name"])
    print("Старая колонка: " + resp1["idList"])

    future_list_id = get_lists_on_board_by_dummy_card_id['list_two_id']
    print("")
    print("\nновая колонка карточки: " + future_list_id)

    resp = api_card_client.move_one_card(dummy_card_id, future_list_id)
    1 == 1
    resp2 = api_card_client.get_card_info(dummy_card_id)
    print("\nСтарые данные карточки:")
    print("Новый старый id: " + resp2["id"])
    print("Новое старое имя: " + resp2["name"])
    print("Новая колонка: " + future_list_id)

    assert resp1["id"] == resp2["id"]
    assert resp1["idList"] != resp2["idList"]
    assert resp2["idList"] == future_list_id

# @pytest.mark.skip()
def test_delete_card(api_card_client: CardAPI, dummy_card_id: str, get_lists_on_board_by_dummy_card_id: dict):
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
    
    x = get_lists_on_board_by_dummy_card_id["list_one_id"]


    resp2 = api_card_client.get_cards_by_list_id(x)
    print("\nКоличество карточек в колонке " + x + " до удаления: " + str(len(resp2)))
    print("id первой карточки: " + resp2[0]["id"] + ", " + "name первой карточки: " + resp2[0]["name"])
    # print("id второй карточки: " + resp2[1]["id"] + ", " + "name второй карточки: " + resp2[1]["name"])
    # print("id третьей карточки: " + resp2[2]["id"] + ", " + "name третьей карточки: " + resp2[2]["name"])

    resp3 = api_card_client.delete_card(dummy_card_id)
    # print("\nДобавится карточка: " + resp3["id"])
    print("\nответ на удаление карточки")
    print(resp3)
    # card_id = resp3["id"]
    # print("\nid новой карточки: " + card_id)

    resp4 = api_card_client.get_cards_by_list_id(x)
    print("\nКоличество карточек в колонке " + x + " после удаления: " + str(len(resp4)))
    # print("id первой карточки: " + resp4[0]["id"] + ", " + "name первой карточки: " + resp4[0]["name"])
    # print("id второй карточки: " + resp4[1]["id"] + ", " + "name второй карточки: " + resp4[1]["name"])
    # print("id третьей карточки: " + resp4[2]["id"] + ", " + "name третьей карточки: " + resp4[2]["name"])

    assert len(resp2) - len(resp4) == 1
