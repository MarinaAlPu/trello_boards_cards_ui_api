import allure
from api.BoardAPI import BoardAPI
# from api.CardAPI import CardAPI

import pytest

# @pytest.mark.skip()
# def test_create_board(api_client: BoardAPI, delete_board: dict, test_data: dict):
#     org_id = test_data.get("org_id")
#     board_list_before = api_client.get_all_boards_by_org_id(org_id)
#     # print("")
#     # print("\nсписок досок до добавления (id, name):")
#     # print(board_list_before)

#     # print("\nдобавляется доска:")
#     resp = api_client.create_board("New board")#api_client.create_board("New board to be deleted")
#     # print("id: " + resp.get("id"))
#     # print("name: " + resp.get("name"))

#     delete_board["board_id"] = resp.get("id") # возвращаем в словарь id созданной доски для удаления в фикстуре

#     board_list_after = api_client.get_all_boards_by_org_id(org_id)
#     # print("\nсписок досок после добавления (id, name):")
#     # print(board_list_after)

#     with allure.step("Проверить, что количество досок стало больше на 1"):
#         assert len(board_list_after) - len(board_list_before) == 1

# @pytest.mark.skip()
# def test_delete_board(api_client: BoardAPI, dummy_board_id: str, test_data: dict):
#     org_id = test_data.get("org_id")
#     board_list_before = api_client.get_all_boards_by_org_id(org_id)
#     # print("\nсписок досок до удаления (id, name):")
#     # print(board_list_before)
#     # print(len(board_list_before))

#     api_client.delete_board_by_id(dummy_board_id)

#     board_list_after = api_client.get_all_boards_by_org_id(org_id)
#     # print("\nсписок досок после удаления (id, name):")
#     # print(board_list_after)
#     # print(len(board_list_after))

#     with allure.step("Проверить, что количество досок стало меньше на 1"):
#         assert len(board_list_before) - len(board_list_after) == 1
    
# @pytest.mark.skip()
# def test_get_boards(api_client: BoardAPI, test_data: dict):
#     org_id = test_data.get("org_id")
#     board_list = api_client.get_all_boards_by_org_id(org_id)
#     # print("\nсписок досок (id, name):")
#     # print(board_list)
#     # print("\nВсего досок" + str(len(board_list)))


# # @pytest.mark.skip()
# def test_create_card(api_card_client: CardAPI, lists_id: dict, delete_card: dict):
#     # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

#     # resp1 = api.get_lists_by_board_id("64171ae9aec528643874445f")
#     # print("\nвсего колонок:")
#     # print(len(resp1))
#     # print("\nсписок колонок (id, name):")
#     # print("первая колонка: " + "id: " + resp1[0]["id"] + ", " + "name: " + resp1[0]["name"])
#     # print("вторая колонка: " + "id: " + resp1[1]["id"] + ", " + "name: " + resp1[1]["name"])
#     # print("третья колонка: " + "id: " + resp1[2]["id"] + ", " + "name: " + resp1[2]["name"])

#     # list_number_1 = resp1[0]
#     # print("\nпервая колонка:")
#     # print(list_number_1)
#     # print("")
#     # print("id первой колонки: " + list_number_1["id"])

#     # list_id = resp1[0]["id"]
#     # print("\nid первой колонки:\n" + list_id)
#     list_id = lists_id.get("first_list_id")
#     print("\nid колонки для получения списка карточек: " + list_id)

#     card_list_before = api_card_client.get_cards_by_list_id(list_id)
#     print("\nКоличество карточек в колонке " + list_id + " до добавления: " + str(len(card_list_before)))
#     # print("id первой карточки: " + resp2[0]["id"] + ", " + "name первой карточки: " + resp2[0]["name"])
#     # print("id второй карточки: " + resp2[1]["id"] + ", " + "name второй карточки: " + resp2[1]["name"])

#     resp3 = api_card_client.create_card(list_id, "New card")
#     print("\nДобавится карточка: " + resp3["id"])
#     print(resp3)
#     card_id = resp3["id"]
#     print("\nid новой карточки: " + card_id)
#     delete_card["card_id"] = resp3.get("id")

#     card_list_after = api_card_client.get_cards_by_list_id(list_id)
#     print("\nКоличество карточек в колонке " + list_id + " после добавления: " + str(len(card_list_after)))
#     print("id первой карточки: " + card_list_after[0]["id"] + ", " + "name первой карточки: " + card_list_after[0]["name"])
#     # print("id второй карточки: " + resp4[1]["id"] + ", " + "name второй карточки: " + resp4[1]["name"])
#     # print("id третьей карточки: " + resp4[2]["id"] + ", " + "name третьей карточки: " + resp4[2]["name"])
#     print("\n список карточек после добавления:")
#     print(card_list_after)
#     assert len(card_list_after) - len(card_list_before) == 1
#     assert card_list_after["name"] == "New card"
#     assert card_list_after["idList"] == list_id

# @pytest.mark.skip()
# def test_delete_card(api_card_client: CardAPI, dummy_card_id: dict):
#     # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

#     # resp1 = api_client.get_lists_by_board_id("64171ae9aec528643874445f")
#     # print("\nвсего колонок:")
#     # print(len(resp1))
#     # print("\nсписок колонок (id, name):")
#     # print("первая колонка: " + "id: " + resp1[0]["id"] + ", " + "name: " + resp1[0]["name"])
#     # print("вторая колонка: " + "id: " + resp1[1]["id"] + ", " + "name: " + resp1[1]["name"])
#     # print("третья колонка: " + "id: " + resp1[2]["id"] + ", " + "name: " + resp1[2]["name"])

#     # list_number_1 = resp1[0]
#     # print("\nпервая колонка:")
#     # print(list_number_1)
#     # print("")
#     # print("id первой колонки: " + list_number_1["id"])

#     # list_id = resp1[0]["id"]
#     # print("\nid первой колонки:\n" + list_id)
#     list_id = dummy_card_id["list_id"]
#     card_list_before = api_card_client.get_cards_by_list_id(list_id) # как сюда принести list_id
#     # print("\nКоличество карточек в колонке " + list_id + " до удаления: " + str(len(resp2)))
#     # print("id первой карточки: " + resp2[0]["id"] + ", " + "name первой карточки: " + resp2[0]["name"])
#     # print("id второй карточки: " + resp2[1]["id"] + ", " + "name второй карточки: " + resp2[1]["name"])
#     # print("id третьей карточки: " + resp2[2]["id"] + ", " + "name третьей карточки: " + resp2[2]["name"])

#     card_id = dummy_card_id["card_id"]
#     api_card_client.delete_card_by_id(card_id)
#     # print("\nДобавится карточка: " + resp3["id"])
#     # print("\nответ на удаление карточки")
#     # print(resp3)
#     # card_id = resp3["id"]
#     # print("\nid новой карточки: " + card_id)

#     card_list_after = api_card_client.get_cards_by_list_id(list_id)
#     # print("\nКоличество карточек в колонке " + list_id + " после удаления: " + str(len(resp4)))
#     # print("id первой карточки: " + resp4[0]["id"] + ", " + "name первой карточки: " + resp4[0]["name"])
#     # print("id второй карточки: " + resp4[1]["id"] + ", " + "name второй карточки: " + resp4[1]["name"])
#     # print("id третьей карточки: " + resp4[2]["id"] + ", " + "name третьей карточки: " + resp4[2]["name"])

#     assert len(card_list_before) - len(card_list_after) == 1

# @pytest.mark.skip()
# def test_update_card(api_card_client: CardAPI, dummy_card_id: dict):
#     # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

#     card_info = api_card_client.get_card_info(dummy_card_id["card_id"])
#     # print("\nСтарые данные карточки:")
#     # print("Старое имя: " + card_info["name"])
#     # print("Старое описание: " + card_info["desc"])
#     # print(card_info["idList"])

#     # print("\nНовые будущие данные карточки:")
#     # print("Новое имя: " + resp1["name"])
#     # print("Новое описание: " + resp1["desc"])

#     resp2 = api_card_client.update_card_by_id(dummy_card_id["card_id"])
#     # print("\nНовые данные карточки:")
#     # print("Новое имя: " + resp2["name"])
#     # print("Новое описание: " + resp2["desc"])

#     new_card_info = api_card_client.get_card_info(dummy_card_id["card_id"])
#     # print("\nНовые данные карточки:")
#     # print("Новое имя: " + new_card_info["name"])
#     # print("Новое описание: " + new_card_info["desc"])

#     assert new_card_info["name"] == "Card's new name"
#     assert new_card_info["desc"] == "We can change card's description!"

# # @pytest.mark.skip()
# # def test_move_card_to_another_list():
# #     api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

# #     resp = api.move_all_cards_to_another_list("64171ae9aec5286438744467")
# #     print(resp)
# #     # print("Новые данные карточки:")
# #     # print("Новая колонка: " + resp["idList"])
    
# #     # assert resp["idList"] == "64171ae9aec5286438744467"

# # @pytest.mark.skip()
# # def test_move_one_card_to_another_list():
# #     api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

# #     resp = api.move_one_card_to_another_list("641730941bc1a44cfd938831")
# #     print("")
# #     print("\nНовые данные карточки:")
# #     print("Новая колонка: " + resp["idList"])
    
# #     assert resp["idList"] == "64171ae9aec5286438744467"

# @pytest.mark.skip()
# def test_move_card(api_card_client: CardAPI, dummy_card_id: dict, lists_id: dict):
#     # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")
#     # list_id = lists_id.get("second_list_id") 

#     x = api_card_client.get_card_info(dummy_card_id["card_id"]).get("idList")
#     print(x)

#     resp = api_card_client.move_one_card(lists_id["second_list_id"])
#     # print("")
#     # print("\nновая колонка карточки: " + resp["idList"])

#     y = api_card_client.get_card_info(dummy_card_id["card_id"]).get("idList")
#     print(y)

#     assert resp["idList"] == lists_id["second_list_id"]
   














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

    api.delete_board_by_id("641a1dab48ffba61722c9b52")#api_client.delete_board_by_id(dummy_board_id)

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






# @pytest.mark.skip()
# def test_create_card_old():
#     api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

#     resp1 = api.get_lists_by_board_id("641a1de7b512da1e59c58922")
#     print("\nвсего колонок:")
#     print(len(resp1))
#     print("\nсписок колонок (id, name):")
#     print("первая колонка: " + "id: " + resp1[0]["id"] + ", " + "name: " + resp1[0]["name"])
#     print("вторая колонка: " + "id: " + resp1[1]["id"] + ", " + "name: " + resp1[1]["name"])
#     print("третья колонка: " + "id: " + resp1[2]["id"] + ", " + "name: " + resp1[2]["name"])

#     list_number_1 = resp1[0]
#     print("\nпервая колонка:")
#     print(list_number_1)
#     # print("")
#     # print("id первой колонки: " + list_number_1["id"])

#     list_id = resp1[0]["id"]
#     print("\nid первой колонки:\n" + list_id)
    
#     resp2 = api.get_cards_by_list_id("641a1de8b512da1e59c58929")
#     print("\nКоличество карточек в колонке " + list_id + "до добавления: " + str(len(resp2)))
#     # print("id первой карточки: " + resp2[0]["id"] + ", " + "name первой карточки: " + resp2[0]["name"])
#     # print("id второй карточки: " + resp2[1]["id"] + ", " + "name второй карточки: " + resp2[1]["name"])

#     resp3 = api.create_card(list_id, "Card 2")
#     print("\nДобавится карточка: " + resp3["id"])
#     # print(resp3)
#     card_id = resp3["id"]
#     print("\nid новой карточки: " + card_id)

#     resp4 = api.get_cards_by_list_id("641a1de8b512da1e59c58929")
#     print("\nКоличество карточек в колонке " + list_id + "после добавления: " + str(len(resp4)))
#     print("id первой карточки: " + resp4[0]["id"] + ", " + "name первой карточки: " + resp4[0]["name"])
#     # print("id второй карточки: " + resp4[1]["id"] + ", " + "name второй карточки: " + resp4[1]["name"])
#     # print("id третьей карточки: " + resp4[2]["id"] + ", " + "name третьей карточки: " + resp4[2]["name"])

#     assert len(resp4) - len(resp2) == 1

#     # assert resp4["name"] == "Card 3"
#     # assert resp4["idList"] == list_id


    # 1. Создать доску
    # 2. Получить id доски
    # 3. Получить id колонок list (список?)
    # 4. Создать карточку по id колонки
    # 5. Удалить карточку
    # 6. Удалить доску


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

# @pytest.mark.skip()
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
# def test_move_card_to_another_list():
#     api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

#     resp = api.move_all_cards_to_another_list("64171ae9aec5286438744467")
#     print(resp)
#     # print("Новые данные карточки:")
#     # print("Новая колонка: " + resp["idList"])
    
#     # assert resp["idList"] == "64171ae9aec5286438744467"

# @pytest.mark.skip()
# def test_move_one_card_to_another_list():
#     api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

#     resp = api.move_one_card_to_another_list("641730941bc1a44cfd938831")
#     print("")
#     print("\nНовые данные карточки:")
#     print("Новая колонка: " + resp["idList"])
    
#     assert resp["idList"] == "64171ae9aec5286438744467"

@pytest.mark.skip()
def test_move_card(api_client: BoardAPI):
    # api = BoardAPI("https://api.trello.com/1", "6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E")

    resp = api_client.move_one_card("641a26192a60d4d132dd1b9a")
    print("")
    print("\nновая колонка карточки: " + resp["idList"])

    assert resp["idList"] == "641a1de8b512da1e59c5892a"

