import requests
import allure

class BoardAPI:
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    def get_all_boards_by_org_id(self, org_id: str) -> list:
        path = "{trello}/organizations/{id}?boards=open&board_fields=id&board_fields=name&fields=boards".format(trello = self.base_url, id = org_id)
        cookie = {"token": self.token}
        resp = requests.get(path, cookies = cookie)

        return resp.json().get("boards")

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
    