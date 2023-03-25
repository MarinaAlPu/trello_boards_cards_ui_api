import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    

    @allure.step("Получить информацию о доске:")
    def get_board_info(self) -> str:
        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))

        with allure.step("получить название доски"):
            return self.__driver.find_element(By.CSS_SELECTOR, "h1").text


    @allure.step("Удалить доску:")
    def delete_board_ui(self) -> None:
        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label=Меню]")))
        # нажать кнопку с тремя точками справа
        with allure.step("нажать кнопку \"Меню\""):
            self.__driver.find_element(By.CSS_SELECTOR, "button[aria-label=Меню]").click()

        with allure.step("нажать кнопку \"Ещё\""):
            self.__driver.find_element(By.CSS_SELECTOR, "a.js-open-more").click()

        with allure.step("нажать кнопку \"Закрыть доску\""):
            self.__driver.find_element(By.CSS_SELECTOR, "a.js-close-board").click()

        with allure.step("нажать кнопку \"Закрыть\""):
            self.__driver.find_element(By.CSS_SELECTOR, "input[value=Закрыть]").click()

        with allure.step("нажать кнопку \"Удалить доску навсегда\""):
            self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=close-board-delete-board-button]").click()

        with allure.step("нажать кнопку \"Удалить\""):
            self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=close-board-delete-board-confirm-button]").click()


    # @allure.step("Создать колонку")
    # def created_list_ui(self) -> None:
    #     # нажать кнопку с тремя точками справа
    #     self.__driver.find_element(By.CSS_SELECTOR, "button[aria-label=Меню]").click()
    #     time.sleep(7)     




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

    

# карточка колонки - их 3 шт. - надо взять первую
# div.js-list-content

    @allure.step("Создать список")   
    def create_list(self):
        # ввести название списка
        self.__driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Ввести заголовок списка"]').click()
        self.__driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Ввести заголовок списка"]').send_keys("Первый список")
        # self.__driver.find_element(By.CSS_SELECTOR, 'input[class="list-name-input"]').send_keys("Первый список")
        # time.sleep(1)

        # нажать кнопку Добавить список
        self.__driver.find_element(By.CSS_SELECTOR, ".js-save-edit").click() #mod-list-add-button
        # time.sleep(1)

        # # нажать кнопку ENTER
        # self.__driver.find_element(By.CSS_SELECTOR, ".js-save-edit").send_keys(Keys.ENTER)
        # time.sleep(5)

    @allure.step("Создать два списка")   
    # def create_board(board_name:str, list_names = [])
    # Реализация:
    # Создать доску с именем board_name
    # В цикле пройтись по списку list_names и вызвать создание колонки с каждым именем.
    # Обратите внимание, что если список пустой, цикл выполнится 0 раз и не будет колонок
    def create_lists(self):
        # список названий списков
        list_names = ["Первый список", "Второй список"]
        length = len(list_names)
        counter = 0
        # ввести название списка
        while counter <= (length - 1):
            self.__driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Ввести заголовок списка"]').click()
            self.__driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Ввести заголовок списка"]').send_keys(list_names[counter])
            # self.__driver.find_element(By.CSS_SELECTOR, 'input[class="list-name-input"]').send_keys("Первый список")
            # time.sleep(1)

            # нажать кнопку Добавить список
            self.__driver.find_element(By.CSS_SELECTOR, ".js-save-edit").click()

            counter = counter + 1
