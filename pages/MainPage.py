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
        

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.step("Открыть боковое меню \"УЧЁТНАЯ ЗАПИСЬ\"")
    def open_menu(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=header-member-menu-button]").click()        

    @allure.step("Прочитать информацию о пользователе")
    def get_account_info(self) -> list[str]:
        container = self.__driver.find_element(By.CSS_SELECTOR, "div[data-testid=account-menu]>div>div:last-child")
        fields = container.find_elements(By.CSS_SELECTOR, "div")
        name = fields[0].text
        email = fields[1].text

        return [name, email]
    
    # ТРИ (четыре?) варианта видимости (уровень конфиденциальности) рабочего пространства 
    # Workspace Visible (Для рабочего пространства)
    # Private (Приватная)
    # Public (Публичная)
    
    @allure.step("Создать доску")
    def create_new_board_ui(self) -> None:
        # нажать кнопку Создать доску
        self.__driver.find_element(By.CSS_SELECTOR, "li[data-testid=create-board-tile]").click()
        # в поле Заголовок доски ввести название новой доски
        self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid=create-board-title-input]").send_keys("One more board") # унести название доски в переменную в test_data

        # WebDriverWait(self.__driver, 13).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".nch-select")))

        # нажать кнопку выбора уровня конфиденциальности доски
        # visible = 
#        self.__driver.find_element(By.CSS_SELECTOR, '.nch-select').click()#'form')#'//label[text()="Видимость"]>div').click()#"#iframe-io-host").click()    ##//*[text()=”Кнопка Войти”]
        # fields = visible.find_elements(By.CSS_SELECTOR, "div")
        # conf = fields[1]
        # conf.click()

        # выбрать уровень конфиденциальности доски (три штуки)

#        x = self.__driver.find_elements(By.CSS_SELECTOR, '.css-1og2rpm')#'form')#'//label[text()="Видимость"]>div').click()#"#iframe-io-host").click()    ##//*[text()=”Кнопка Войти”]
#        y = x[0]
#        print(y.text)

        # выбрать фон доски из видимых или из трёх точек, фото или цвет
                

        # создать или сделать по шаблону
        # по шаблону - из популярных или посмотреть шаблоны

        # нажать кнопку Создать
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=create-board-submit-button]").click()

        # нажать на доску на главной странице
        # self.__driver.find_element(By.XPATH, '//*[text()="One more board"]').click()


        # удалить доску
        # self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=create-board-submit-button]").click()



