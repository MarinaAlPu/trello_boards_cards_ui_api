import requests
import allure

class ApiForUI:
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    @allure.step("Получить id всех досок организации {org_id}")
    def get_all_boards_by_org_id(self, org_id: str) -> list:
        path = "{trello}/organizations/{id}?boards=open&board_fields=id&board_fields=name&fields=boards".format(trello = self.base_url, id = org_id)
        cookie = {"token": self.token}
        resp = requests.get(path, cookies = cookie)

        return resp.json().get("boards")


    @allure.step("Создать доску {name} без колонок")
    def create_board(self, name: str, default_lists = False) -> dict:
        body = {
                'defaultLists': default_lists,
                'name': name,
                'token': self.token
        }
        path = "{trello}/boards".format(trello = self.base_url)
        cookie = {"token": self.token}
        resp = requests.post(path, json = body, cookies = cookie)

        return resp.json()


    @allure.step("Удалить доску с id {id}")    
    def delete_board_by_id(self, id: str) -> dict:
        cookie = {"token": self.token}
        path = "{trello}/boards/{board_id}".format(trello = self.base_url, board_id = id)
        resp = requests.delete(path, json = cookie, cookies = cookie)

        return resp.json()


    @allure.step("Получить список колонок на доске {id}")
    def get_lists_by_board_id(self, id: str) -> list:
        cookie = {"token": self.token}
        path = "{trello}/boards/{board_id}/lists".format(trello = self.base_url, board_id = id)
        resp = requests.get(path, json = cookie, cookies = cookie)

        return resp.json()
    

# class CardAPI:
    # def __init__(self, base_url: str, token: str) -> None:
    #     self.base_url = base_url
    #     self.token = token

    # @allure.step("Получить список карточек в колонке {id}")
    # def get_cards_by_list_id(self, id: str):
    #     path = "{trello}/lists/{list_id}/cards".format(trello = self.base_url, list_id = id)
    #     cookie = {"token": self.token}
    #     resp = requests.get(path, json = cookie, cookies = cookie)

    #     return resp.json()  
    
    # @allure.step("Добавить карточку {name} в колонке {list_id}")
    # def create_card(self, list_id: str, name: str) -> dict:
    #     body = {
    #             'idList': list_id,
    #             'token': self.token
    #     }
    #     path = "{trello}/cards?name={card_name}".format(trello = self.base_url, card_name = name)
    #     cookie = {"token": self.token}
    #     resp = requests.post(path, json = body, cookies = cookie)

    #     return resp.json()        

    # @allure.step("Изменить информацию о карточке {id}")    
    # def update_card(self, id: str, card_name: str, card_desc: str) -> dict:
    #     path = "{trello}/cards/{card_id}?name={card_new_name}&desc={card_new_description}"\
    #             .format(trello = self.base_url, card_id = id, card_new_name = card_name, card_new_description = card_desc)
    #     cookie = {"token": self.token}
    #     resp = requests.put(path, json = cookie, cookies = cookie)

    #     return resp.json()
    
    # @allure.step("Получить информацию о карточке {id}")    
    # def get_card_info(self, id: str) -> dict:
    #     path = "{trello}/cards/{card_id}".format(trello = self.base_url, card_id = id)
    #     cookie = {"token": self.token}
    #     resp = requests.get(path, json = cookie, cookies = cookie)

    #     return resp.json()  

    # @allure.step("Переместить карточку {card_id} в другую колонку")    
    # def move_one_card(self, card_id: str, list_id: str) -> dict:
    #     body = {
    #             'idList': list_id,
    #             'token': self.token
    #     }        
    #     path = "{trello}/cards/{card_id}".format(trello = self.base_url, card_id = card_id)
    #     cookie = {"token": self.token}
    #     resp = requests.put(path, json = body, cookies = cookie)

    #     return resp.json()
    
    # @allure.step("Удалить карточку {id}")    
    # def delete_card(self, id: str):
    #     path = "{trello}/cards/{card_id}".format(trello = self.base_url, card_id = id)
    #     cookie = {"token": self.token}
    #     resp = requests.delete(path, json = cookie, cookies = cookie)

    #     return resp.json()