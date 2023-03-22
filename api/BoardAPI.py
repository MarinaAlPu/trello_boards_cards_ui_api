import requests
import allure

# class BoardAPI:
#     def __init__(self, base_url: str, token: str) -> None:
#         self.base_url = base_url
#         self.token = token

#     def get_all_boards_by_org_id(self, org_id: str) -> list:
#         path = "{trello}/organizations/{id}?boards=open&board_fields=id&board_fields=name&fields=boards".format(trello = self.base_url, id = org_id)
#         cookie = {"token": self.token}
#         resp = requests.get(path, cookies = cookie)

#         return resp.json().get("boards")

#     @allure.step("Создать доску {name}")
#     def create_board(self, name: str, default_lists = True) -> dict:
#         body = {
#                 'defaultLists': default_lists,
#                 'name': name,
#                 'token': self.token
#         }
#         path = "{trello}/boards".format(trello = self.base_url)
#         cookie = {"token": self.token}
#         resp = requests.post(path, json = body, cookies = cookie)

#         return resp.json()

#     @allure.step("Удалить доску {id}")    
#     def delete_board_by_id(self, id: str):
#         cookie = {"token": self.token}
#         path = "{trello}/boards/{board_id}".format(trello = self.base_url, board_id = id)
#         resp = requests.delete(path, json = cookie, cookies = cookie)

#         return resp.json()

#     @allure.step("Получить список колонок на доске {id}")
#     def get_lists_by_board_id(self, id: str) -> list:
#         cookie = {"token": self.token}
#         path = "{trello}/boards/{board_id}/lists".format(trello = self.base_url, board_id = id)
#         resp = requests.get(path, json = cookie, cookies = cookie)

#         return resp.json()
    
#     # @allure.step("Получить список карточек в колонке {id}")
#     # def get_cards_by_list_id(self, id: str):
#     #     path = "{trello}/lists/{list_id}/cards".format(trello = self.base_url, list_id = id)
#     #     cookie = {"token": self.token}
#     #     resp = requests.get(path, json = cookie, cookies = cookie)

#     #     return resp.json()  
    
#     # @allure.step("Добавить карточку {name} в колонке {list_id}")
#     # def create_card(self, list_id: str, name: str) -> dict:
#     #     body = {
#     #             'idList': list_id,
#     #             'token': self.token
#     #     }
#     #     path = "{trello}/cards?name={card_name}".format(trello = self.base_url, card_name = name)
#     #     cookie = {"token": self.token}
#     #     resp = requests.post(path, json = body, cookies = cookie)

#     #     return resp.json()

#     # @allure.step("Изменить информацию о карточке {id}")    
#     # def update_card_by_id(self, id: str) -> dict:
#     #     path = "{trello}/cards/{card_id}?name=New name Card 2&desc=We can change card's description!".format(trello = self.base_url, card_id = id)
#     #     cookie = {"token": self.token}
#     #     resp = requests.put(path, json = cookie, cookies = cookie)

#     #     return resp.json()  

#     # @allure.step("Получить информацию о карточке {id}")    
#     # def get_card_info(self, id: str) -> dict:
#     #     path = "{trello}/cards/{card_id}".format(trello = self.base_url, card_id = id)
#     #     cookie = {"token": self.token}
#     #     resp = requests.get(path, json = cookie, cookies = cookie)

#     #     return resp.json()  

#     # @allure.step("Удалить карточку {id}")    
#     # def delete_card_by_id(self, id: str):
#     #     path = "{trello}/cards/{card_id}".format(trello = self.base_url, card_id = id)
#     #     cookie = {"token": self.token}
#     #     resp = requests.delete(path, json = cookie, cookies = cookie)

#     #     return resp.json()  

#     # @allure.step("Переместить карточки из колонки {id} в другую колонку")    
#     # def move_all_cards_to_another_list(self, id: str) -> dict:
#     #     body = {
#     #             'idBoard': '64171ae9aec528643874445f',
#     #             'idList': '64171ae9aec5286438744466',
#     #             'token': '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'
#     #     }
#     #     path = "{trello}/lists/{list_id}/moveAllCards".format(trello = self.base_url, list_id = id)
#     #     cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}
#     #     resp = requests.post(path, json = body, cookies = cookie)

#     #     return resp.json()        
        
#     # @allure.step("Переместить карточку {id} на другой лист")    
#     # def move_one_card_to_another_list(self, id: str) -> dict:
#     #     path = "{trello}/cards/{card_id}?idList=64171ae9aec5286438744467".format(trello = self.base_url, card_id = id)
#     #     cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}
#     #     resp = requests.put(path, json = cookie, cookies = cookie)

#     #     return resp.json()  

#     # @allure.step("Переместить карточку {id} на другой лист")    
#     # def move_one_card(self, id: str) -> dict:
#     #     body = {
#     #             'idList': '64171ae9aec5286438744467',
#     #             'token': self.token
#     #     }        
#     #     path = "{trello}/cards/{card_id}".format(trello = self.base_url, card_id = id)
#     #     cookie = {"token": self.token}
#     #     resp = requests.put(path, json = body, cookies = cookie)

#     #     return resp.json()
















class BoardAPI:
    # base_url = "https://api.trello.com/1" - убрали в конструктор и в тестах добавляем при создании экземпляра класса BoardAPI

    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    def get_all_boards_by_org_id(self, org_id: str) -> dict:#list:
        path = "{trello}/organizations/{id}?boards=open&board_fields=id&board_fields=name&fields=boards".format(trello = self.base_url, id = org_id)
        cookie = {"token": self.token} # длинный токен убрали в конструктор и в тестах добавляем при создании экземпляра класса BoardAPI
        resp = requests.get(path, cookies = cookie)

        return resp.json()#.get("boards")

    @allure.step("Создать доску {name}")
    def create_board(self, name: str, default_lists = True) -> dict:
        body = {
                'defaultLists': default_lists,
                'name': name,
                'token': self.token
        }
        path = "{trello}/boards".format(trello = self.base_url)
        cookie = {"token": self.token}
        resp = requests.post(path, json = body, cookies = cookie)

        return resp.json()

    @allure.step("Удалить доску {id}")    
    def delete_board_by_id(self, id: str):
        cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}#self.token}
        path = "{trello}/boards/{board_id}".format(trello = self.base_url, board_id = id)
        resp = requests.delete(path, json = cookie, cookies = cookie)

        return resp.json()

    @allure.step("Получить список колонок на доске {id}")
    def get_lists_by_board_id(self, id: str) -> list:
        cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}#self.token}
        path = "{trello}/boards/{board_id}/lists".format(trello = self.base_url, board_id = id)
        resp = requests.get(path, json = cookie, cookies = cookie)

        return resp.json()
    
    # @allure.step("Получить список карточек в колонке {id}")
    # def get_cards_by_list_id(self, id: str):
    #     path = "{trello}/lists/{list_id}/cards".format(trello = self.base_url, list_id = id)
    #     cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}
    #     resp = requests.get(path, json = cookie, cookies = cookie)

    #     return resp.json()  
    
    # @allure.step("Добавить карточку в колонке {list_id}: {name}")
    # def create_card(self, list_id: str, name: str) -> dict:#, name: str
    #     body = {
    #             'idList': list_id,
    #             'token': '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'
    #     }
    #     path = "{trello}/cards?name={card_name}".format(trello = self.base_url, card_name = name)
    #     cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}
    #     resp = requests.post(path, json = body, cookies = cookie)

    #     return resp.json()        

    # @allure.step("Изменить информацию о карточке {id}")    
    # def update_card(self, id: str) -> dict:
    #     path = "{trello}/cards/{card_id}?name=Card's new name&desc=We can change card's description!&idList=641a1de8b512da1e59c5892b".format(trello = self.base_url, card_id = id)
    #     cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}
    #     resp = requests.put(path, json = cookie, cookies = cookie)

    #     return resp.json()  

    # @allure.step("Получить информацию о карточке {id}")    
    # def get_card_info(self, id: str) -> dict:
    #     path = "{trello}/cards/{card_id}".format(trello = self.base_url, card_id = id)
    #     cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}
    #     resp = requests.get(path, json = cookie, cookies = cookie)

    #     return resp.json()  

    # @allure.step("Удалить карточку {id}")    
    # def delete_card(self, id: str):
    #     path = "{trello}/cards/{card_id}".format(trello = self.base_url, card_id = id)
    #     cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}
    #     resp = requests.delete(path, json = cookie, cookies = cookie)

    #     return resp.json()  

    # # @allure.step("Переместить карточки из колонки {id} в другую колонку")    
    # # def move_all_cards_to_another_list(self, id: str) -> dict:
    # #     body = {
    # #             'idBoard': '64171ae9aec528643874445f',
    # #             'idList': '64171ae9aec5286438744466',
    # #             'token': '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'
    # #     }
    # #     path = "{trello}/lists/{list_id}/moveAllCards".format(trello = self.base_url, list_id = id)
    # #     cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}
    # #     resp = requests.post(path, json = body, cookies = cookie)

    # #     return resp.json()        
        
    # # @allure.step("Переместить карточку {id} на другой лист")    
    # # def move_one_card_to_another_list(self, id: str) -> dict:
    # #     path = "{trello}/cards/{card_id}?idList=64171ae9aec5286438744467".format(trello = self.base_url, card_id = id)
    # #     cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}
    # #     resp = requests.put(path, json = cookie, cookies = cookie)

    # #     return resp.json()  

    # @allure.step("Переместить карточку {id} на другой лист")    
    # def move_one_card(self, id: str) -> dict:
    #     body = {
    #             'idList': '641a1de8b512da1e59c5892a',
    #             'token': '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'
    #     }        
    #     path = "{trello}/cards/{card_id}".format(trello = self.base_url, card_id = id)
    #     cookie = {"token": '6410e3061677ca07e152a914/ATTSErkH1NWoupUXCMttfF52OxV36yw7Dl1xyoemvFIOi1msR7kG77Ef8tvonVIO4C7T8387F93E'}
    #     resp = requests.put(path, json = body, cookies = cookie)

    #     return resp.json()
    
    