import requests
import json
from config import password_1
token = password_1
class YaDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        return headers

    def get_my_files_name(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        print(response.status_code)
        return str(response.status_code)

    def create_folder(self, path):
        headers = self.get_headers()
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        res = requests.put(f'{upload_url}?path={path}', headers=headers)
        print(res.status_code)
        return str(res.status_code)



if __name__ == "__main__":
    token = password_1
    ya = YaDisk(token)
    ya.get_my_files_name()
    ya.create_folder(path='New_Folder')
