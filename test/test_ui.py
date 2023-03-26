import allure
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
from pages.BoardPage import BoardPage
from pages.ListPage import ListPage
from pages.CardPage import CardPage

from pages.ApiPage import ApiForUI

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
def create_board_test(browser, auth_for_create_board, test_data: dict):
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
def delete_board_test(browser, auth_for_delete_board):#, test_data: dict
    # board_name = test_data.get("board_name")
    main_page = MainPage(browser)
    boards_before = main_page.get_boards_before()
    main_page.open_board()
    
    board_page = BoardPage(browser)
    board_page.delete_board_ui()

    boards_after = main_page.get_boards_after()

    with allure.step("Проверить, что в \"Рабочем пространстве Trello\" досок стало меньше на 1"):
        assert boards_before - boards_after == 1   
      

# @pytest.mark.skip()
def create_card_test(browser, dummy_board_for_ui: str, test_data: dict):
    card_name = test_data.get("card_name")

    list_page = ListPage(browser)
    with allure.step("Посчитать количество карточек в колонке ДО добавления новой карточки"):
        cards_on_list_before = list_page.get_cards_on_list()
    list_page.create_card(card_name)
    with allure.step("Посчитать количество карточек в колонке ПОСЛЕ добавления новой карточки"):
        cards_on_list_after = list_page.get_cards_on_list()

    card_page = CardPage(browser)    
    new_card_name = card_page.get_card_info()

    with allure.step("Проверить, что карточка создалась:"):
        with allure.step("количество карточек стало больше на 1"):
            assert len(cards_on_list_after) - len(cards_on_list_before) == 1
        with allure.step("название новой карточки совпадает с заданным названием"):
            assert new_card_name == card_name   


@pytest.mark.skip()
def delete_card_test(browser, test_data: dict):
    username = test_data.get("username")
    email = test_data.get("email")
    password = test_data.get("password") 

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.create_board_ui()
    time.sleep(5)

    board_page = BoardPage(browser)
    board_page.create_list()
    time.sleep(5)   

    list_page = ListPage(browser)
    list_page.create_card()
    time.sleep(5) 

    card_page = CardPage(browser)
    card_page.delete_card()
    time.sleep(5) 

@pytest.mark.skip()
def update_card_test(browser, test_data: dict):
    username = test_data.get("username")
    email = test_data.get("email")
    password = test_data.get("password") 

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.create_board_ui()
    time.sleep(5)

    board_page = BoardPage(browser)
    board_page.create_list()
    time.sleep(5)

    list_page = ListPage(browser)
    list_page.create_card()
    time.sleep(5)

    card_page = CardPage(browser)
    card_page.update_card()
    time.sleep(5)

@pytest.mark.skip()
def move_card_test(browser, test_data: dict):
    username = test_data.get("username")
    email = test_data.get("email")
    password = test_data.get("password") 

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.create_board_ui()
    time.sleep(5)

    board_page = BoardPage(browser)
    board_page.create_lists_for_moving()
    time.sleep(5)

    list_page = ListPage(browser)
    list_page.create_card()
    time.sleep(5)

    list_page = ListPage(browser)
    list_page.move_card()
    time.sleep(5)

