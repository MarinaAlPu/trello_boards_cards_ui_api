import allure
from api.BoardAPI import BoardAPI
from api.CardAPI import CardAPI


def test_create_board(api_client: BoardAPI, delete_board: dict, test_data: dict):
    with allure.step("Получить id организации"):
        org_id = test_data.get("org_id")

    board_list_before = api_client.get_all_boards_by_org_id(org_id)

    resp = api_client.create_board("New board to be deleted")

    delete_board["board_id"] = resp.get("id")

    board_list_after = api_client.get_all_boards_by_org_id(org_id)

    with allure.step("Проверить, что количество досок стало больше на 1"):
        assert len(board_list_after) - len(board_list_before) == 1


def test_delete_board(api_client: BoardAPI, dummy_board_id: str, test_data: dict):
    with allure.step("Получить id организации"):
        org_id = test_data.get("org_id")
    
    board_list_before = api_client.get_all_boards_by_org_id(org_id)

    api_client.delete_board_by_id(dummy_board_id)

    board_list_after = api_client.get_all_boards_by_org_id(org_id)

    with allure.step("Проверить, что количество досок стало меньше на 1"):
        assert len(board_list_before) - len(board_list_after) == 1


def test_create_card(api_card_client: CardAPI, lists_on_board: dict):
    cards_on_list_before = api_card_client.get_cards_by_list_id(lists_on_board["list_one_id"])

    created_card = api_card_client.create_card(lists_on_board["list_one_id"], "New card")

    new_card_info = api_card_client.get_card_info(created_card["id"])

    cards_on_list_after = api_card_client.get_cards_by_list_id(lists_on_board["list_one_id"])

    with allure.step("Проверить, что карточка создалась:"):
        with allure.step("количество карточек стало больше на 1"):
            assert len(cards_on_list_after) - len(cards_on_list_before) == 1
        with allure.step("название новой карточки совпадает с заданным названием"):
            assert new_card_info["name"] == "New card"
        with allure.step("карточка находится в той колонке, в которую её добавляли"):
            assert lists_on_board["list_one_id"] == new_card_info["idList"]


def test_update_card(api_card_client: CardAPI, dummy_card_id: str, test_data: dict):
    api_card_client.get_card_info(dummy_card_id)

    api_card_client.update_card(dummy_card_id, test_data.get("card_new_name"), test_data.get("card_new_description"))

    updated_card_info = api_card_client.get_card_info(dummy_card_id)

    with allure.step("Проверить, что данные карточки изменились:"):
        with allure.step("новое название соответствует заданному"):
            assert updated_card_info["name"] == test_data.get("card_new_name")
        with allure.step("новое описание соответствует заданному"):
            assert updated_card_info["desc"] == test_data.get("card_new_description")


def test_move_card(api_card_client: CardAPI, dummy_card_id: str, get_lists_on_board_by_dummy_card_id: dict):
    api_card_client.get_card_info(dummy_card_id)

    future_list_id = get_lists_on_board_by_dummy_card_id['list_two_id']

    api_card_client.move_one_card(dummy_card_id, future_list_id)

    moved_card_info = api_card_client.get_card_info(dummy_card_id)

    with allure.step("Проверить, что карточка переместилась в другую колонку"):
        assert moved_card_info["idList"] == future_list_id


def test_delete_card(api_card_client: CardAPI, dummy_card_id: str, get_lists_on_board_by_dummy_card_id: dict):
    lists_on_board = get_lists_on_board_by_dummy_card_id["list_one_id"]

    cards_before = api_card_client.get_cards_by_list_id(lists_on_board)

    api_card_client.delete_card(dummy_card_id)

    cards_after = api_card_client.get_cards_by_list_id(lists_on_board)

    with allure.step("Проверить, карточек в колонке стало меньше на 1"):
        assert len(cards_before) - len(cards_after) == 1