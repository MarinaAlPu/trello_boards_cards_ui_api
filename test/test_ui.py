import allure
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
from pages.BoardPage import BoardPage
from pages.ListPage import ListPage
from pages.CardPage import CardPage

import time

import pytest

# @pytest.mark.skip()
# def auth_test(browser, test_data: dict):
#     username = test_data.get("username")
#     email = test_data.get("email")
#     password = test_data.get("password")

#     auth_page = AuthPage(browser)
#     auth_page.go()
#     auth_page.login_as(email, password)

#     main_page = MainPage(browser)
#     main_page.open_menu()
#     info = main_page.get_account_info()

#     current_url = main_page.get_current_url()
#     with allure.step("Проверить, что URL " + current_url + " заканчивается на kahajow976/boards"):
#         assert current_url.endswith("kahajow976/boards")

#     with allure.step("Проверить, что в меню \"УЧЁТНАЯ ЗАПИСЬ\" указаны данные пользователя:"):
#         with allure.step("Имя пользователя должно быть: " + username):
#             assert info[0] == username
#         with allure.step("Электронная почта пользователя должна быть: " + email):
#             assert info[1] == email


@pytest.mark.skip()
def create_board_test(browser, for_create_board, test_data: dict):
    board_name = test_data.get("board_name")

    main_page = MainPage(browser)
    boards_before = main_page.get_boards_before()
    main_page.create_board_ui(board_name)

    board_page = BoardPage(browser)
    info = board_page.get_board_info()
    boards_after = main_page.get_boards_after()

    with allure.step("Проверить, что в \"Рабочем пространстве Trello\" досок стало больше на 1"):
        assert boards_after - boards_before == 1

    with allure.step("Проверить, что название созданной доски: " + board_name):
        assert info == board_name


@pytest.mark.skip()
def delete_board_test(browser, for_delete_board):
    main_page = MainPage(browser)
    boards_before = main_page.get_boards_before()
    main_page.open_board()
    
    board_page = BoardPage(browser)
    board_page.delete_board_ui()

    boards_after = main_page.get_boards_after()

    with allure.step("Проверить, что в \"Рабочем пространстве Trello\" досок стало меньше на 1"):
        assert boards_before - boards_after == 1   
      

@pytest.mark.skip()
def create_card_test(browser, dummy_board_for_ui: str, test_data: dict):
    card_name = test_data.get("card_name")

    list_page = ListPage(browser)
    with allure.step("Посчитать количество карточек в колонке ДО добавления новой карточки"):
        cards_on_list_before = list_page.get_cards_on_list()
    list_page.create_card(card_name)
    with allure.step("Посчитать количество карточек в колонке ПОСЛЕ добавления новой карточки"):
        cards_on_list_after = list_page.get_cards_on_list()

    card_page = CardPage(browser)    
    new_card_name = card_page.get_card_name()

    with allure.step("Проверить, что карточка создалась:"):
        with allure.step("количество карточек стало больше на 1"):
            assert len(cards_on_list_after) - len(cards_on_list_before) == 1
        with allure.step("название новой карточки совпадает с заданным названием"):
            assert new_card_name == card_name   


@pytest.mark.skip()
def delete_card_test(browser, card_to_delete):
    list_page = ListPage(browser)
    with allure.step("Посчитать количество карточек в колонке ДО удаления карточки"):
        cards_on_list_before = list_page.get_cards_on_list()

    card_page = CardPage(browser)
    card_page.delete_card()

    with allure.step("Посчитать количество карточек в колонке ПОСЛЕ удаления карточки"):
        cards_on_list_after = list_page.get_cards_on_list()

    with allure.step("Проверить, что карточка удалилась:"):
        with allure.step("количество карточек в колонке стало меньше на 1"):
            assert len(cards_on_list_before) - len(cards_on_list_after) == 1


@pytest.mark.skip()
def update_card_test(browser, test_data: dict, card_to_delete):
    new_name = test_data.get("new_data")["card_new_name"]
    print("\nновое имя: ")
    print(new_name)
    new_description = test_data.get("new_data")["card_new_description"]
    print("\nновое описание: ")
    print(new_description)
    # username = test_data.get("username")
    # email = test_data.get("email")
    # password = test_data.get("password")

    # auth_page = AuthPage(browser)
    # auth_page.go()
    # auth_page.login_as(email, password)

    # main_page = MainPage(browser)
    # main_page.create_board_ui()
    # time.sleep(5)

    # board_page = BoardPage(browser)
    # board_page.create_list()
    # time.sleep(5)

    # list_page = ListPage(browser)
    # list_page.create_card()
    # time.sleep(5)

    card_page = CardPage(browser)

    card_info_before = card_page.get_card_info_before_update()
    card_name_before = card_info_before.get("name")
    print("\nимя карточки до изменения: ")
    print(card_name_before)
    card_description_before = card_info_before.get("description")
    print("\nописание карточки до изменения: ")
    print(card_description_before)

    card_page.update_card(new_name, new_description)

    card_name_after = card_page.get_card_info_after_update().get("name")
    print("\nимя карточки после изменения: ")
    print(card_name_after)
    card_description_after = card_page.get_card_info_after_update().get("description")
    print("\nописание карточки до изменения: ")
    print(card_description_after)
    time.sleep(5)
    with allure.step("Проверить, что данные карточки изменились:"):
        with allure.step("новое имя карточки: {new_name}"):
            assert card_name_after == new_name
        with allure.step("новое описание карточки: {new_description}"):
            assert card_description_after == new_description   

    time.sleep(5)


@pytest.mark.skip()
def move_card_test(browser, dummy_board_for_moving):
    list_page = ListPage(browser)
    card_page = CardPage(browser)

    list_of_card_before = card_page.get_card_list_before_moving()

    list_page.move_card()

    list_of_card_after = card_page.get_card_list_after_moving()

    with allure.step("Проверить, что название колонки, в которой находится карточка, изменилось"):
        assert list_of_card_after != list_of_card_before
