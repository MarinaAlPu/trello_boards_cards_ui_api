import requests
import allure

class CardAPI:
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    @allure.step("Получить список карточек в колонке {id}")
    def get_cards_by_list_id(self, id: str):
        path = "{trello}/lists/{list_id}/cards".format(trello = self.base_url, list_id = id)
        cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}
        resp = requests.get(path, json = cookie, cookies = cookie)

        return resp.json()  
    
    @allure.step("Добавить карточку в колонке {list_id}: {name}")
    def create_card(self, list_id: str, name: str) -> dict:#, name: str
        body = {
                'idList': list_id,
                'token': '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'
        }
        path = "{trello}/cards?name={card_name}".format(trello = self.base_url, card_name = name)
        cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}
        resp = requests.post(path, json = body, cookies = cookie)

        return resp.json()        

    @allure.step("Изменить информацию о карточке {id}")    
    def update_card(self, id: str) -> dict:
        path = "{trello}/cards/{card_id}?name=Card's new name&desc=We can change card's description!".format(trello = self.base_url, card_id = id)
        cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}
        resp = requests.put(path, json = cookie, cookies = cookie)

        return resp.json()
    
    @allure.step("Получить информацию о карточке {id}")    
    def get_card_info(self, id: str) -> dict:
        path = "{trello}/cards/{card_id}".format(trello = self.base_url, card_id = id)
        cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}
        resp = requests.get(path, json = cookie, cookies = cookie)

        return resp.json()  

    @allure.step("Переместить карточку {card_id} на другой лист")    
    def move_one_card(self, card_id: str, list_id: str) -> dict:
        body = {
                'idList': list_id,
                'token': '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'
        }        
        path = "{trello}/cards/{card_id}".format(trello = self.base_url, card_id = card_id)
        cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}
        resp = requests.put(path, json = body, cookies = cookie)

        return resp.json()
    
    @allure.step("Удалить карточку {id}")    
    def delete_card(self, id: str):
        path = "{trello}/cards/{card_id}".format(trello = self.base_url, card_id = id)
        cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}
        resp = requests.delete(path, json = cookie, cookies = cookie)

        return resp.json()    
