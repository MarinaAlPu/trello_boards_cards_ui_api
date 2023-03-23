import allure
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
# from pages.BoardPage import BoardPage
# from pages.CardPage import CardPage
import time

import pytest

@pytest.mark.skip()
def auth_test(browser, test_data: dict):
    username = test_data.get("username")
    email = test_data.get("email")
    password = test_data.get("password")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    current_url = main_page.get_current_url()
    with allure.step("Проверить, что URL " + current_url + " заканчивается на kahajow976/boards"):
        assert current_url.endswith("kahajow976/boards")

    with allure.step("Проверить, что в меню \"УЧЁТНАЯ ЗАПИСЬ\" указаны данные пользователя:"):
        with allure.step("Имя пользователя должно быть: " + username):
            assert info[0] == username
        with allure.step("Электронная почта пользователя должна быть: " + email):
            assert info[1] == email

@pytest.mark.skip()
def create_board_test(browser, test_data: dict):
    username = test_data.get("username")
    email = test_data.get("email")
    password = test_data.get("password")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.create_board_ui()
    time.sleep(13)

@pytest.mark.skip()
def delete_board_test(browser, test_data: dict):
    username = test_data.get("username")
    email = test_data.get("email")
    password = test_data.get("password") 

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.create_board_ui()
    time.sleep(7)

    main_page.delete_board_ui()
    time.sleep(7)    
      
