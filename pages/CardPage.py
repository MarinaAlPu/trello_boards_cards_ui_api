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

    @allure.step("Получить данные карточки:")
    def get_card_info(self):
        # нажать на карточку
        # with allure.step("нажать на карточку"):
            # self.__driver.find_element(By.CSS_SELECTOR, "input[class='js-card-details']").click()
        return self.__driver.find_element(By.CSS_SELECTOR, ".js-card-details").text     


    @allure.step("Изменить данные карточки:")
    def update_card(self):
        # нажать на карточку
        self.__driver.find_element(By.CSS_SELECTOR, ".js-card-details").click()
        time.sleep(1)

        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".window-title")))

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
        with allure.step("нажать кнопку \"Сохранить\""):
            self.__driver.find_element(By.CSS_SELECTOR, 'input[value=Сохранить]:first-child').click()
        time.sleep(3)


    @allure.step("Удалить карточку:")
    def delete_card(self):
        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".js-card-menu")))

        with allure.step("нажать кнопку с иконкой \"карандаш\""):
            self.__driver.find_element(By.CSS_SELECTOR, ".js-card-menu").click()

        with allure.step("нажать кнопку \"Архивировать\""):
            self.__driver.find_element(By.CSS_SELECTOR, ".js-archive").click()


