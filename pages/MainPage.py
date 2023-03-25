import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider
# from pages.BoardPage import BoardPage
# from pages.ListPage import ListPage
# from pages.CardPage import CardPage

import time

class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.data = DataProvider()
        url = ConfigProvider().get("ui", "base_url")
        # self.__url = 
        

    # @allure.step("Получить текущий URL")
    # def get_current_url(self) -> str:
    #     return self.__driver.current_url


    # @allure.step("Открыть боковое меню \"УЧЁТНАЯ ЗАПИСЬ\"")
    # def open_menu(self):
    #     self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=header-member-menu-button]").click()        


    @allure.step("Посчитать количество досок в Рабочем пространстве Trello до добавления новой доски:")
    def get_boards_before(self) -> list[str]:
        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.board-tile-details-name")))

        with allure.step("посчитать количество досок"):
            fields = self.__driver.find_elements(By.CSS_SELECTOR, "div.board-tile-details-name")
            return len(fields)

    @allure.step("Посчитать количество досок в Рабочем пространстве Trello после добавления новой доски:")
    def get_boards_after(self) -> list[str]:
        with allure.step("нажать кнопку \"Рабочее простанство Trello\" и перейти в Рабочее простанство Trello"):
            self.__driver.find_element(By.XPATH, '//p[text()="Рабочее пространство Trello"]').click()

        with allure.step("посчитать количество досок"):
            fields = self.__driver.find_elements(By.CSS_SELECTOR, "div.board-tile-details-name")
            return len(fields)


    # ТРИ (четыре?) варианта видимости (уровень конфиденциальности) рабочего пространства 
    # Workspace Visible (Для рабочего пространства)
    # Private (Приватная)
    # Public (Публичная)
    
    
    @allure.step("Создать доску:")
    def create_board_ui(self, board_name: str) -> None:
        with allure.step("нажать кнопку \"Создать доску\""):
            self.__driver.find_element(By.CSS_SELECTOR, "li[data-testid=create-board-tile]").click()

        with allure.step("ввести название доски в поле \"Заголовок доски\""):
            self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid=create-board-title-input]").send_keys(board_name) # унести название доски в переменную в test_data

        with allure.step("нажать кнопку \"Создать\""):
            self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=create-board-submit-button]").click()


    @allure.step("Открыть доску")# {name}   
    def open_board(self):#, name: str
        self.__driver.find_element(By.CSS_SELECTOR, 'div[title="New board"]').click()


