import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider
from pages.MainPage import MainPage
# from pages.ListPage import ListPage
# from pages.CardPage import CardPage

import time

class BoardPage:

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

    # @allure.step("Прочитать информацию о пользователе")
    # def get_account_info(self) -> list[str]:
    #     container = self.__driver.find_element(By.CSS_SELECTOR, "div[data-testid=account-menu]>div>div:last-child")
    #     fields = container.find_elements(By.CSS_SELECTOR, "div")
    #     name = fields[0].text
    #     email = fields[1].text

    #     return [name, email]
    


    @allure.step("Удалить доску")
    def delete_created_board_ui(self) -> None:
        # нажать кнопку с тремя точками справа
        self.__driver.find_element(By.CSS_SELECTOR, "button[aria-label=Меню]").click()
        time.sleep(7)
        
        # нажать кнопку Ещё
        self.__driver.find_element(By.CSS_SELECTOR, "a.js-open-more").click()
        time.sleep(7)

        # нажать кнопку Закрыть доску 
        self.__driver.find_element(By.CSS_SELECTOR, "a.js-close-board").click()
        time.sleep(7)

        # нажать кнопку Закрыть
        self.__driver.find_element(By.CSS_SELECTOR, "input[value=Закрыть]").click()
        time.sleep(7)

        # нажать кнопку Удалить доску навсегда
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=close-board-delete-board-button]").click()
        time.sleep(7)

        # нажать кнопку Удалить доску навсегда
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=close-board-delete-board-confirm-button]").click()
        time.sleep(7)






    # # ТРИ (четыре?) варианта видимости (уровень конфиденциальности) рабочего пространства 
    # # Workspace Visible (Для рабочего пространства)
    # # Private (Приватная)
    # # Public (Публичная)
    # # 
    # def create_board(self):
    #     # нажать кнопку Создать доску
    #     self.__driver.find_element(By.CSS_SELECTOR, "li[data-testid=create-board-tile]").click()
    #     # в поле Заголовок доски ввести название новой доски
    #     self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid=create-board-title-input]").send_keys("One more board")
    #     # выбрать уровень конфиденциальности доски (три штуки)


    #     # выбрать фон доски из видимых или из трёх точек, фото или цвет
                

    #     # создать или сделать по шаблону
    #     # по шаблону - из популярных или посмотреть шаблоны

    