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


    @allure.step("Получить данные карточки ДО изменения информации:")
    def get_card_info_before_update(self):
        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "New card")]')))
        time.sleep(3)
        with allure.step("извлечь название карточки"):
            card_name = self.__driver.find_element(By.XPATH, '//span[contains(text(), "New card")]').text
        time.sleep(3)
        with allure.step("открыть карточку, нажав на неё"):
            self.__driver.find_element(By.CSS_SELECTOR, ".js-card-name").click()
        time.sleep(3)
        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.js-desc')))

        with allure.step("извлечь описание карточки"):
            card_description = self.__driver.find_element(By.CSS_SELECTOR, '.js-desc').text

        data_before = {"name": card_name,
                       "description": card_description}

        return data_before

    
    @allure.step("Получить данные карточки ПОСЛЕ изменения информации:")
    def get_card_info_after_update(self):
        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "Card\'s new name")]')))
        time.sleep(3)
        with allure.step("извлечь название карточки"):
            card_name = self.__driver.find_element(By.XPATH, '//span[contains(text(), "Card\'s new name")]').text
        time.sleep(3)
        with allure.step("открыть карточку, нажав на неё"):
            self.__driver.find_element(By.CSS_SELECTOR, ".js-card-details").click()
        time.sleep(3)
        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.js-desc')))

        with allure.step("извлечь описание карточки"):
            card_description = self.__driver.find_element(By.CSS_SELECTOR, '.js-desc').text

        data_after = {"name": card_name,
                       "description": card_description}

        return data_after

########################################################################################################################################
#     @allure.step("Получить данные карточки ПОСЛЕ изменения информации:")
#     def get_card_info_test_update(self):
#         # нажать на карточку
#         with allure.step("нажать на карточку"):
#             # self.__driver.find_element(By.CSS_SELECTOR, "input[class='js-card-details']").click()
#         # return self.__driver.find_element(By.CSS_SELECTOR, ".js-card-details").text     
#             self.__driver.find_element(By.CSS_SELECTOR, ".js-card-details").click()   
#         time.sleep(3)
#         # with allure.step("подождать загрузки всех необходимых элементов"):
#         #     WebDriverWait(self.__driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#js-dialog-title")))

#         with allure.step("получить название карточки"):
#             # card_name = self.__driver.find_element(By.CSS_SELECTOR, "#js-dialog-title").text
#             card_name = self.__driver.find_element(By.CSS_SELECTOR, "div>h2").text
#             print("сейчас напечатаю имя карточки:")
#             print(card_name)
#         time.sleep(3)
#         with allure.step("получить описание карточки"):
#             # card_description = self.__driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Main content area, start typing to enter text."]').text
#             card_description = self.__driver.find_element(By.CSS_SELECTOR, 'span[data-testid="placeholder-test-id"]').text
#             print("а сейчас напечатаю описание карточки:")
#             print(card_description)
#         time.sleep(3)

# # Добавляйте форматирование, пока пишете, используя символы разметки. Например, * для списков, # для заголовков и --- для горизонтальной разделительной линии.
        
#         data = {
#             "name": card_name,
#             "description": card_description
#         }
#         print(data)
#         return data
#########################################################################################################################


    @allure.step("Изменить данные карточки:")
    def update_card(self):#, name: str, description: str): # не фурычит
        name = "Card's new name"
        description = "We can change card's description!" 

        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".js-card-name")))
        
        with allure.step("открыть карточку нажатием на неё"):
            self.__driver.find_element(By.CSS_SELECTOR, ".js-card-name").click()
            time.sleep(3)

        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.js-card-detail-title-input")))

        with allure.step("кликнуть название карточки"):
            self.__driver.find_element(By.CSS_SELECTOR, "textarea.js-card-detail-title-input").click()
            time.sleep(3)

        with allure.step("удалить старое название карточки"):
            self.__driver.find_element(By.CSS_SELECTOR, ".is-editing").clear()
            time.sleep(3)

        with allure.step("ввести новое название карточки"):
            self.__driver.find_element(By.CSS_SELECTOR, ".is-editing").send_keys(name)
            time.sleep(3)
            self.__driver.find_element(By.CSS_SELECTOR, ".is-editing").send_keys(Keys.ENTER)
            time.sleep(3)

        with allure.step("кликнуть в поле \"Описание\""):
            self.__driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Main content area, start typing to enter text."]').click()
            time.sleep(3)

        with allure.step("ввести новое описание в поле \"Описание\""):
            self.__driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Main content area, start typing to enter text."]').send_keys(description)
            time.sleep(3)

        with allure.step("нажать кнопку \"Сохранить\""):
            self.__driver.find_element(By.CSS_SELECTOR, 'input[value=Сохранить]:first-child').click()
        time.sleep(3)

        with allure.step("закрыть карточку нажатием на \"крестик\" в правом верхнем углу"):
            self.__driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Закрыть диалоговое окно"]').click()
        time.sleep(3)


    @allure.step("Получить список, в котором находится открытая карточка:")
    def get_list_of_card(self):
        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.list-card-title")))
        
        with allure.step("нажать на карточку"):
            self.__driver.find_element(By.CSS_SELECTOR, "span.list-card-title").click()
        time.sleep(1)

        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".js-open-move-from-header")))

        with allure.step("получить название списка, в котором находится карточка"):
            list_name = self.__driver.find_element(By.CSS_SELECTOR, ".js-open-move-from-header").text
            return list_name


    @allure.step("Удалить карточку:")
    def delete_card(self):
        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".js-card-menu")))

        with allure.step("нажать кнопку с иконкой \"карандаш\""):
            self.__driver.find_element(By.CSS_SELECTOR, ".js-card-menu").click()

        with allure.step("нажать кнопку \"Архивировать\""):
            self.__driver.find_element(By.CSS_SELECTOR, ".js-archive").click()
