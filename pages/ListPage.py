import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains

from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider

import time

class ListPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.data = DataProvider()
        url = ConfigProvider().get("ui", "base_url")
        # self.__url = 

    @allure.step("Создать карточку")
    def create_card(self):
        # нажать кнопку Добавить карточку
        # self.__driver.find_element(By.CSS_SELECTOR, "a[.js-open-card-composer]").click()

        # рабочий, создаёт карточку в первой колонке, а должен во второй, потому что :last-child
        self.__driver.find_element(By.CSS_SELECTOR, 'span.js-add-a-card:last-child').click()


    # @allure.step("Прочитать информацию о пользователе")
    # def get_account_info(self) -> list[str]:
    #     container = self.__driver.find_element(By.CSS_SELECTOR, "div[data-testid=account-menu]>div>div:last-child")
    #     fields = container.find_elements(By.CSS_SELECTOR, "div")
    #     name = fields[0].text
    #     email = fields[1].text
    #     return [name, email]


# div id=board
#   div class=js-list (2 штуки - по числу списков)
#       div -
#       div -
#       div class=card-composer-container
#          a
#             span class=js-add-a-card

        # self.__driver.find_element(By.CSS_SELECTOR, '#board:first-child:last-child/a/span[class=js-add-a-card]').click()

        # self.__driver.find_element(By.XPATH, '//[@id=board]:first-child/following-sibling::*[contains(text(), "Добавить карточку")]').click()
        
        # self.__driver.find_element(By.XPATH, '#board:first-child//span').click()


        # self.__driver.find_elements(By.CSS_SELECTOR, 'span[class="js-add-a-card"]:first-child')
        # self.__driver.find_element(By.CSS_SELECTOR, "input[value=Добавить карточку]").click()
        # self.__driver.find_element(By.CSS_SELECTOR, "input[.js-card-details]").click()
        # time.sleep(5)

        # в поле "Ввести заголовок для этой карточки" ввести название карточки
        # self.__driver.find_element(By.CSS_SELECTOR, ".list-card-details").send_keys("Новая карточка")
        self.__driver.find_element(By.CSS_SELECTOR, "textarea[placeholder=\"Ввести заголовок для этой карточки\"]").send_keys("Карточка для перетаскивания")
        # self.__driver.find_element(By.CSS_SELECTOR, "textarea[.js-card-title]").click()
        # time.sleep(5)

        # # кликнуть в свободное место на поле доски
        # self.__driver.find_element(By.CSS_SELECTOR, "#board").click()
        # time.sleep(5)

        # нажать кнопку ENTER
        self.__driver.find_element(By.CSS_SELECTOR, "textarea[placeholder=\"Ввести заголовок для этой карточки\"]").send_keys(Keys.ENTER)
        # time.sleep(5)


    @allure.step("Перенести карточку в другую колонку")
    def move_card(self):

        # with allure.step("Получить название карточки"):
        #     container = self.__driver.find_element(By.CSS_SELECTOR, "div[data-testid=account-menu]>div>div:last-child")
        #     fields = container.find_elements(By.CSS_SELECTOR, "div")
        #     name = fields[0].text
        #     email = fields[1].text
        #     return [name, email]



    # def test_drag_and_drop_onto_element(driver):
    #     driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')

    #     draggable = driver.find_element(By.ID, "draggable")
    #     droppable = driver.find_element(By.ID, "droppable")
    #     ActionChains(driver)\
    #         .drag_and_drop(draggable, droppable)\
    #         .perform()

    #     assert driver.find_element(By.ID, "drop-status").text == "dropped"
#Карточка для перетаскивания
        draggable = self.__driver.find_element(By.XPATH, '//span[text()="Карточка для перетаскивания"]')
        droppable = self.__driver.find_element(By.XPATH, '//textarea[text()="Второй список"]')
        ActionChains(self.__driver)\
            .drag_and_drop(draggable, droppable)\
            .perform()    
        
