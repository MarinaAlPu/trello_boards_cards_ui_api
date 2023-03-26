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


    def get_cards_on_list(self):
        cards = self.__driver.find_elements(By.CSS_SELECTOR, ".js-card-details")
        return cards


    @allure.step("Создать карточку")
    def create_card(self, name: str):
        with allure.step("нажать кнопку \"Добавить карточку\""):
            self.__driver.find_element(By.XPATH, '//div[@id="board"]/div[1]/div[last()]//*[text()="Добавить карточку"]').click()

        with allure.step("в поле \"Ввести заголовок для этой карточки\" ввести название карточки"):
            self.__driver.find_element(By.CSS_SELECTOR, "textarea[placeholder=\"Ввести заголовок для этой карточки\"]").send_keys(name)

        with allure.step("нажать кнопку ENTER"):
            self.__driver.find_element(By.CSS_SELECTOR, "textarea[placeholder=\"Ввести заголовок для этой карточки\"]").send_keys(Keys.ENTER)


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

# self.__driver.find_element(By.XPATH, '/div[@id="board"]/div[@class="js-list"]/div[last()]/a/span*[text()="Карточка для перетаскивания"]').click()

        draggable = self.__driver.find_element(By.XPATH, '//span[text()="Карточка для перетаскивания"]')
        # find_serial_number = browser.find_element_by_xpath('.//span[text()=" + ПЕРЕМЕННАЯ + ")]')

        # find_serial_number = browser.find_element_by_xpath(".//*[contains(text(),'sn-" + serialNumber + "')]")

        # find_serial_number = browser.find_element_by_xpath('.//textarea[text()=" + ПЕРЕМЕННАЯ + ")]')
        droppable = self.__driver.find_element(By.XPATH, '//textarea[text()="Второй список"]')
        ActionChains(self.__driver).drag_and_drop(draggable, droppable).perform()    
        
