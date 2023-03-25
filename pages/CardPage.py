import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider

from selenium.webdriver.common.action_chains import ActionChains

import time

class CardPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.data = DataProvider()
        url = ConfigProvider().get("ui", "base_url")
        # self.__url = 

    @allure.step("Изменить данные карточки")
    def update_card(self):
        # нажать на карточку
        # self.__driver.find_element(By.CSS_SELECTOR, "input[class='js-card-details']").click()
        self.__driver.find_element(By.CSS_SELECTOR, ".js-card-details").click()
        time.sleep(1)

        # кликнуть название карточки
        self.__driver.find_element(By.CSS_SELECTOR, ".window-title").click()
        time.sleep(1)

        # ввести новое название карточки
        self.__driver.find_element(By.CSS_SELECTOR, ".is-editing").clear()
        time.sleep(1)

        # ввести новое название карточки
        self.__driver.find_element(By.CSS_SELECTOR, ".is-editing").send_keys("Новое название")
        time.sleep(1)

        # нажать кнопку ENTER
        self.__driver.find_element(By.CSS_SELECTOR, ".is-editing").send_keys(Keys.ENTER)
        time.sleep(3)

        # кликнуть в поле "Добавить более подробное описание…"
        self.__driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Main content area, start typing to enter text."]').click()
        # self.__driver.find_element(By.XPATH, '//*[contains(text(), "Добавить более подробное описание*")]').click()
        # self.__driver.find_element(By.XPATH, '//a[text()="Добавить более подробное описание…"]').click()
        time.sleep(3)

        # в поле "Добавить более подробное описание…" ввести новое описание
        self.__driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Main content area, start typing to enter text."]').send_keys("Новое описание")
        # self.__driver.find_element(By.CSS_SELECTOR, "span[data-testid=placeholder-test-id]").send_keys("Новое описание")
        time.sleep(3)

        # нажать кнопку Сохранить
        self.__driver.find_element(By.CSS_SELECTOR, 'input[value=Сохранить]:first-child').click()
        time.sleep(3)

    @allure.step("Удалить карточку")
    def delete_card(self):
        # # нажать кнопку Добавить карточку
        # # self.__driver.find_element(By.CSS_SELECTOR, "a[.js-open-card-composer]").click()
        # self.__driver.find_element(By.CSS_SELECTOR, 'span.js-add-a-card:last-child').click()
        # time.sleep(5)

        # # в поле "Ввести заголовок для этой карточки" ввести название карточки
        # self.__driver.find_element(By.CSS_SELECTOR, "textarea[placeholder=\"Ввести заголовок для этой карточки\"]").send_keys("Новая карточка")
        # # self.__driver.find_element(By.CSS_SELECTOR, "textarea[.js-card-title]").click()
        # time.sleep(5)

        # # # кликнуть в свободное место на поле доски
        # # self.__driver.find_element(By.CSS_SELECTOR, "#board").click()
        # # # self.__driver.find_element(By.CSS_SELECTOR, 'div[class="board-canvas"]')
        # # time.sleep(5)        

        # открыть меню последней созданной карточки, кликнув икноку с карандашом
        # self.__driver.find_element(By.CSS_SELECTOR, 'span[class="js-card-menu"]:last-child').click()
        self.__driver.find_element(By.CSS_SELECTOR, "span.js-card-menu").click()
        # time.sleep(5)        

        # # в меню карточки кликнуть 
        # self.__driver.find_element(By.CSS_SELECTOR, ".js-card-menu").click()
        # # self.__driver.find_element(By.CSS_SELECTOR, 'div[class="board-canvas"]')
        # time.sleep(5)

        # # открыть последнюю созданную карточку
        # self.__driver.find_element(By.CSS_SELECTOR, "div.js-card-details:last-child").click()
        # # self.__driver.find_element(By.CSS_SELECTOR, 'div[class="board-canvas"]')
        # time.sleep(5)  

        # в меню карточки кликнуть кнопку Архивировать
        self.__driver.find_element(By.CSS_SELECTOR, ".js-archive").click()
        # self.__driver.find_element(By.CSS_SELECTOR, 'div[class="board-canvas"]')
        # time.sleep(5)

