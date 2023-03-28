import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        # self.data = DataProvider()
        # url = ConfigProvider().get("ui", "base_url")

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


    # @allure.step("Посчитать количество досок в Рабочем пространстве Trello ДО добавления новой доски:")
    def get_boards_before_add_board(self) -> list[str]:
        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.board-tile-details-name")))

        with allure.step("посчитать количество досок"):
            fields = self.__driver.find_elements(By.CSS_SELECTOR, "div.board-tile-details-name")
            print("\n досок ДО добавления:" + str(len(fields)))
            return len(fields)

    # @allure.step("Посчитать количество досок в Рабочем пространстве Trello ПОСЛЕ добавления новой доски:")
    def get_boards_after_add_board(self) -> list[str]:
        with allure.step("нажать кнопку \"Рабочее простанство Trello\" и перейти в Рабочее простанство Trello"):
            self.__driver.find_element(By.XPATH, '//p[text()="Рабочее пространство Trello"]').click()

        # with allure.step("подождать загрузки всех необходимых элементов"):
        #     WebDriverWait(self.__driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div[title="New board"]')))

        print("\n пришли считать доски ПОСЛЕ добавления")
        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.board-tile-details-name")))

        with allure.step("посчитать количество досок"):
            fields = self.__driver.find_elements(By.CSS_SELECTOR, "div.board-tile-details-name")
            print("\n досок ПОСЛЕ добавления:" + str(len(fields)))
            return len(fields)
        

    # @allure.step("Посчитать количество досок в Рабочем пространстве Trello ДО добавления новой доски:")
    def get_boards_before_delete(self) -> list[str]:
        with allure.step("подождать загрузки всех необходимых элементов"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="New board"]')))

        with allure.step("посчитать количество досок"):
            fields = self.__driver.find_elements(By.CSS_SELECTOR, "div.board-tile-details-name")
            print("\n досок ДО удаления:" + str(len(fields)))
            return len(fields)

    # @allure.step("Посчитать количество досок в Рабочем пространстве Trello ПОСЛЕ добавления новой доски:")
    def get_boards_after_delete(self) -> list[str]:
        # with allure.step("нажать кнопку \"Рабочее простанство Trello\" и перейти в Рабочее простанство Trello"):
        #     self.__driver.find_element(By.XPATH, '//p[text()="Рабочее пространство Trello"]').click()

        # with allure.step("подождать загрузки всех необходимых элементов"):
        #     WebDriverWait(self.__driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div[title="New board"]')))

        print("\n пришли считать доски ПОСЛЕ удаления")
        # with allure.step("подождать загрузки всех необходимых элементов"):
        #     WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.board-tile-details-name")))

        with allure.step("посчитать количество досок"):
            fields = self.__driver.find_elements(By.CSS_SELECTOR, "div.board-tile-details-name")
            print("\n досок ПОСЛЕ удаления:" + str(len(fields)))
            return len(fields)


    @allure.step("Создать доску {board_name}:")
    def create_board_ui(self, board_name: str) -> None:
        with allure.step("нажать кнопку \"Создать доску\""):
            self.__driver.find_element(By.CSS_SELECTOR, "li[data-testid=create-board-tile]").click()

        with allure.step("ввести название доски в поле \"Заголовок доски\""):
            self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid=create-board-title-input]").send_keys(board_name)

        with allure.step("подождать, когда кнопка \"Создать\" станет кликабельной"):
            WebDriverWait(self.__driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="create-board-submit-button"]')))

        with allure.step("нажать кнопку \"Создать\""):
            self.__driver.find_element(By.CSS_SELECTOR, 'button[data-testid="create-board-submit-button"]').click()


    @allure.step("Открыть доску")# {name} # переменную в селектор???????????
    def open_board(self):#, name: str
        self.__driver.find_element(By.CSS_SELECTOR, 'div[title="New board"]').click()
