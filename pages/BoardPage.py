import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider

class BoardPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.data = DataProvider()
        url = ConfigProvider().get("ui", "base_url")

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
        print("пришли в метод get_board_info")
        with allure.step("получить название доски"):
            return self.__driver.find_element(By.CSS_SELECTOR, "h1").get_property('textContent')


    @allure.step("Удалить доску:")
    def delete_board_ui(self) -> None:
        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label=\"Меню\"]")))
        # нажать кнопку с тремя точками справа
        with allure.step("нажать кнопку \"Меню\""):
            self.__driver.find_element(By.CSS_SELECTOR, "button[aria-label=\"Меню\"]").click()

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


    @allure.step("Создать список {name}:")
    def create_list_ui(self, name: str):
        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="New board"]')))

        with allure.step("открыть доску"):
            self.__driver.find_element(By.CSS_SELECTOR, 'div[title="New board"]').click()

        with allure.step("нажать кнопку \"Добавить список\""):
            self.__driver.find_element(By.CSS_SELECTOR, '.js-open-add-list').click()

        with allure.step("ввести название списка в поле \"Ввести заголовок списка\""):
            self.__driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Ввести заголовок списка"]').send_keys(name)

        with allure.step("нажать кнопку \"Добавить список\""):
            self.__driver.find_element(By.CSS_SELECTOR, ".js-save-edit").click()

        # # нажать кнопку ENTER
        # with allure.step("нажать кнопку ENTER"):        
        #   self.__driver.find_element(By.CSS_SELECTOR, ".js-save-edit").send_keys(Keys.ENTER)


    @allure.step("Создать два списка:")   
    def create_lists_for_moving(self, list_names: list):
        length = len(list_names)
        counter = 0

        with allure.step("открыть доску"):
            self.__driver.find_element(By.CSS_SELECTOR, 'div[title="New board"]').click()

        while counter <= (length - 1):
            with allure.step("нажать кнопку \"Добавить список\""):
                self.__driver.find_element(By.CSS_SELECTOR, '.js-open-add-list').click()

            with allure.step("ввести название списка в поле \"Ввести заголовок списка\""):
                self.__driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Ввести заголовок списка"]').send_keys(list_names[counter])

            with allure.step("нажать кнопку \"Добавить список\""):        
                self.__driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Ввести заголовок списка"]').send_keys(Keys.ENTER)
                self.__driver.find_element(By.CSS_SELECTOR, "#board").click()
                counter = counter + 1
