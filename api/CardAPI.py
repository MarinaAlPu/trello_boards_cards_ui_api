import requests
import allure

class CardAPI:
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    @allure.step("Получить список карточек в колонке {id}")
    def get_cards_by_list_id(self, id: str):
        path = "{trello}/lists/{list_id}/cards".format(trello = self.base_url, list_id = id)
        cookie = {"token": self.token}
        resp = requests.get(path, json = cookie, cookies = cookie)

        return resp.json()  
    
    @allure.step("Добавить карточку {name} в колонке {list_id}")
    def create_card(self, list_id: str, name: str) -> dict:
        body = {
                'idList': list_id,
                'token': self.token
        }
        path = "{trello}/cards?name={card_name}".format(trello = self.base_url, card_name = name)
        cookie = {"token": self.token}
        resp = requests.post(path, json = body, cookies = cookie)

        return resp.json()        

    @allure.step("Изменить информацию о карточке {id}")    
    def update_card(self, id: str) -> dict:
        path = "{trello}/cards/{card_id}?name=Card's new name&desc=We can change card's description!".format(trello = self.base_url, card_id = id)
        cookie = {"token": self.token}
        resp = requests.put(path, json = cookie, cookies = cookie)

        return resp.json()
    
    @allure.step("Получить информацию о карточке {id}")    
    def get_card_info(self, id: str) -> dict:
        path = "{trello}/cards/{card_id}".format(trello = self.base_url, card_id = id)
        cookie = {"token": self.token}
        resp = requests.get(path, json = cookie, cookies = cookie)

        return resp.json()  

    @allure.step("Переместить карточку {card_id} в другую колонку")    
    def move_one_card(self, card_id: str, list_id: str) -> dict:
        body = {
                'idList': list_id,
                'token': self.token
        }        
        path = "{trello}/cards/{card_id}".format(trello = self.base_url, card_id = card_id)
        cookie = {"token": self.token}
        resp = requests.put(path, json = body, cookies = cookie)

        return resp.json()
    
    @allure.step("Удалить карточку {id}")    
    def delete_card(self, id: str):
        path = "{trello}/cards/{card_id}".format(trello = self.base_url, card_id = id)
        cookie = {"token": self.token}
        resp = requests.delete(path, json = cookie, cookies = cookie)

        return resp.json()    
