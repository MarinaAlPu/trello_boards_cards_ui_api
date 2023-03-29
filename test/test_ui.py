import allure
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
from pages.BoardPage import BoardPage
from pages.ListPage import ListPage
from pages.CardPage import CardPage

from configuration.ConfigProvider import ConfigProvider
from user_data.UserProvider import UserProvider


@allure.epic("Автоматизация тестов для проверки работы с досками и карточками в сервисе Trello")
@allure.suite("UI-тесты")
class TrelloTestUI:
    @allure.story("Доски")
    @allure.title("Создание доски")
    @allure.description("Проверка создания новой доски по id организации")
    # @allure.feature("GET")
    @allure.severity("critical")
    @allure.id("UI-1")    
    # @pytest.mark.skip()
    # def auth_test(self, browser):#, test_data: dict
    #     username = UserProvider().get("user", "username")
    #     email = UserProvider().get("user", "email")
    #     password = UserProvider().get("user", "password")

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


    def create_board_test(self, browser, for_create_board, test_data: dict):
        board_name = test_data.get("board_name")

        main_page = MainPage(browser)

        with allure.step("Посчитать количество досок ДО создания новой доски:"):
            boards_before = main_page.get_boards_before_add_board()

        main_page.create_board_ui(board_name)

        board_page = BoardPage(browser)
        info = board_page.get_board_info()

        with allure.step("Посчитать количество досок ПОСЛЕ создания новой доски:"):
            boards_after = main_page.get_boards_after_add_board()

        with allure.step("Проверить, что досок стало больше на 1"):
            assert boards_after - boards_before == 1

        with allure.step("Проверить, что название созданной доски: " + board_name):
            assert info == board_name


    def delete_board_test(self, browser, for_delete_board):
        main_page = MainPage(browser)
        
        with allure.step("Посчитать количество досок ДО удаления доски:"):
            boards_before = main_page.get_boards_before_delete()

        main_page.open_board()
        
        board_page = BoardPage(browser)
        board_page.delete_board_ui()

        with allure.step("Посчитать количество досок ПОСЛЕ удаления доски:"):
            boards_after = main_page.get_boards_after_delete()

        with allure.step("Проверить, что досок стало меньше на 1"):
            assert boards_before - boards_after == 1   
        

    def create_card_test(self, browser, dummy_board_for_ui: str, test_data: dict):
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


    def delete_card_test(self, browser, card_to_delete):
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


    def update_card_test(self, browser, test_data: dict, card_to_delete):
        new_name = test_data.get("new_data")["card_new_name"]
        new_description = test_data.get("new_data")["card_new_description"]

        card_page = CardPage(browser)
        card_page.update_card(new_name, new_description)

        card_name_after = card_page.get_card_info_after_update().get("name")
        card_description_after = card_page.get_card_info_after_update().get("description")
        with allure.step("Проверить, что данные карточки изменились:"):
            with allure.step("новое имя карточки: {new_name}"):
                assert card_name_after == new_name
            with allure.step("новое описание карточки: {new_description}"):
                assert card_description_after == new_description   


    def move_card_test(self, browser, dummy_board_for_moving):
        list_page = ListPage(browser)
        card_page = CardPage(browser)

        list_of_card_before = card_page.get_card_list_before_moving()

        list_page.move_card()

        list_of_card_after = card_page.get_card_list_after_moving()

        with allure.step("Проверить, что название колонки, в которой находится карточка, изменилось"):
            assert list_of_card_after != list_of_card_before
