import allure
from api.BoardAPI import BoardAPI
# from pages.BoardPage import BoardPage
import pytest

@pytest.mark.skip()
def test_create_board():#api_client: BoardAPI, delete_board: dict, test_data: dict):
    api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")
    # board_list = api.get_all_boards_by_org_id("6410e46e85363751e85ab637")#api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637")

    # org_id = test_data.get("org_id")
    board_list_before = api.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")#api_client.get_all_boards_by_org_id(org_id)
    print("")
    print("\nсписок досок до добавления (id, name):")
    print(board_list_before)

    print("\nдобавляется доска:")
    resp = api.create_board("New new board")#api_client.create_board("New board to be deleted")
    print("id: " + resp.get("id"))
    print("name: " + resp.get("name"))

    # delete_board["board_id"] = resp.get("id")

    board_list_after = api.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")# api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637")
    print("\nсписок досок после добавления (id, name):")
    print(board_list_after)

    with allure.step("Проверить, что количество досок стало больше на 1"):
        assert len(board_list_after) - len(board_list_before) == 1

@pytest.mark.skip()
def test_delete_board():#api_client: BoardAPI, dummy_board_id: str, test_data: dict):
    # org_id = test_data.get("org_id")
    api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")
    
    board_list_before = api.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")#api_client.get_all_boards_by_org_id(org_id)
    print("\nсписок досок до удаления (id, name):")
    print(board_list_before)

    api.delete_board_by_id("64171acf63f840bba4f48896")#api_client.delete_board_by_id(dummy_board_id)

    board_list_after = api.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")#api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637")
    print("\nсписок досок после удаления (id, name):")
    print(board_list_after)

    with allure.step("Проверить, что количество досок стало меньше на 1"):
        assert len(board_list_before) - len(board_list_after) == 1
    
@pytest.mark.skip()
def test_get_boards():#api_client: BoardAPI
    api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")
    board_list = api.get_all_boards_by_org_id("6410e46e85363751e85ab637").get("boards")#api_client.get_all_boards_by_org_id("6410e46e85363751e85ab637")
    print("\nсписок досок (id, name):")
    print(board_list)


@pytest.mark.skip()
def test_create_card():
    api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

    resp1 = api.get_lists_by_board_id("64171ae9aec528643874445f")
    print("\nвсего колонок:")
    print(len(resp1))
    print("\nсписок колонок (id, name):")
    print("первая колонка: " + "id: " + resp1[0]["id"] + ", " + "name: " + resp1[0]["name"])
    print("вторая колонка: " + "id: " + resp1[1]["id"] + ", " + "name: " + resp1[1]["name"])
    print("третья колонка: " + "id: " + resp1[2]["id"] + ", " + "name: " + resp1[2]["name"])

    list_number_1 = resp1[0]
    print("\nпервая колонка:")
    print(list_number_1)
    # print("")
    # print("id первой колонки: " + list_number_1["id"])

    list_id = resp1[0]["id"]
    print("\nid первой колонки:\n" + list_id)
    
    resp2 = api.get_cards_by_list_id("64171ae9aec5286438744466")
    print("\nКоличество карточек в колонке " + list_id + "до добавления: " + str(len(resp2)))
    print("id первой карточки: " + resp2[0]["id"] + ", " + "name первой карточки: " + resp2[0]["name"])
    # print("id второй карточки: " + resp2[1]["id"] + ", " + "name второй карточки: " + resp2[1]["name"])

    resp3 = api.create_card(list_id, "Card 2")
    print("\nДобавится карточка: " + resp3["id"])
    # print(resp3)
    card_id = resp3["id"]
    print("\nid новой карточки: " + card_id)

    resp4 = api.get_cards_by_list_id("64171ae9aec5286438744466")
    print("\nКоличество карточек в колонке " + list_id + "после добавления: " + str(len(resp4)))
    print("id первой карточки: " + resp4[0]["id"] + ", " + "name первой карточки: " + resp4[0]["name"])
    print("id второй карточки: " + resp4[1]["id"] + ", " + "name второй карточки: " + resp4[1]["name"])
    # print("id третьей карточки: " + resp4[2]["id"] + ", " + "name третьей карточки: " + resp4[2]["name"])

    assert len(resp4) - len(resp2) == 1

    # assert resp4["name"] == "Card 3"
    # assert resp4["idList"] == list_id


    # 1. Создать доску
    # 2. Получить id доски
    # 3. Получить id колонок list (список?)
    # 4. Создать карточку по id колонки
    # 5. Удалить карточку
    # 6. Удалить доску


@pytest.mark.skip()
def test_update_card():
    api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

    resp1 = api.get_card_info("64176cfc665c9e95a00c9863")
    print("\nНовые данные карточки:")
    print("Новое имя: " + resp1["name"])
    print("Новое описание: " + resp1["desc"])

    resp2 = api.update_card("64176cfc665c9e95a00c9863")
    print("\nНовые данные карточки:")
    print("Новое имя: " + resp2["name"])
    print("Новое описание: " + resp2["desc"])

    resp3 = api.get_card_info("64176cfc665c9e95a00c9863")
    print("\nНовые данные карточки:")
    print("Новое имя: " + resp3["name"])
    print("Новое описание: " + resp3["desc"])

    assert resp3["name"] == "New name Card 2"
    assert resp3["desc"] == "We can change card's description!"

@pytest.mark.skip()
def test_delete_card():
    api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

    resp1 = api.get_lists_by_board_id("64171ae9aec528643874445f")
    print("\nвсего колонок:")
    print(len(resp1))
    print("\nсписок колонок (id, name):")
    print("первая колонка: " + "id: " + resp1[0]["id"] + ", " + "name: " + resp1[0]["name"])
    print("вторая колонка: " + "id: " + resp1[1]["id"] + ", " + "name: " + resp1[1]["name"])
    print("третья колонка: " + "id: " + resp1[2]["id"] + ", " + "name: " + resp1[2]["name"])

    list_number_1 = resp1[0]
    print("\nпервая колонка:")
    print(list_number_1)
    # print("")
    # print("id первой колонки: " + list_number_1["id"])

    list_id = resp1[0]["id"]
    print("\nid первой колонки:\n" + list_id)
    
    resp2 = api.get_cards_by_list_id("64171ae9aec5286438744467")
    print("\nКоличество карточек в колонке " + list_id + " до удаления: " + str(len(resp2)))
    print("id первой карточки: " + resp2[0]["id"] + ", " + "name первой карточки: " + resp2[0]["name"])
    # print("id второй карточки: " + resp2[1]["id"] + ", " + "name второй карточки: " + resp2[1]["name"])
    # print("id третьей карточки: " + resp2[2]["id"] + ", " + "name третьей карточки: " + resp2[2]["name"])

    resp3 = api.delete_card("64176cfc665c9e95a00c9863")
    # print("\nДобавится карточка: " + resp3["id"])
    print("\nответ на удаление карточки")
    print(resp3)
    # card_id = resp3["id"]
    # print("\nid новой карточки: " + card_id)

    resp4 = api.get_cards_by_list_id("64171ae9aec5286438744467")
    print("\nКоличество карточек в колонке " + list_id + " после удаления: " + str(len(resp4)))
    # print("id первой карточки: " + resp4[0]["id"] + ", " + "name первой карточки: " + resp4[0]["name"])
    # print("id второй карточки: " + resp4[1]["id"] + ", " + "name второй карточки: " + resp4[1]["name"])
    # print("id третьей карточки: " + resp4[2]["id"] + ", " + "name третьей карточки: " + resp4[2]["name"])

    assert len(resp2) - len(resp4) == 1

@pytest.mark.skip()
def test_move_card_to_another_list():
    api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

    resp = api.move_all_cards_to_another_list("64171ae9aec5286438744467")
    print(resp)
    # print("Новые данные карточки:")
    # print("Новая колонка: " + resp["idList"])
    
    # assert resp["idList"] == "64171ae9aec5286438744467"

@pytest.mark.skip()
def test_move_one_card_to_another_list():
    api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

    resp = api.move_one_card_to_another_list("641730941bc1a44cfd938831")
    print("")
    print("\nНовые данные карточки:")
    print("Новая колонка: " + resp["idList"])
    
    assert resp["idList"] == "64171ae9aec5286438744467"

@pytest.mark.skip()
def test_move_card():
    api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

    resp = api.move_one_card("64176cfc665c9e95a00c9863")
    print("")
    print("\nновая колонка карточки: " + resp["idList"])

    assert resp["idList"] == "64171ae9aec5286438744467"

