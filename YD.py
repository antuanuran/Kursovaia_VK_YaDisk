import requests
class Load_yadisk:
    def __init__(self, token_YD):
        self.token_YD = token_YD
        self.headers = {
                        'Content-Type': 'application/json',
                        'Authorization': f'{self.token_YD}'
                       }
        self.url_get_file = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        self.url_get_folder = 'https://cloud-api.yandex.net/v1/disk/resources'


    def create_folder(self, name_folder):
        params = {
                    'path': name_folder
                 }
        requests.put(self.url_get_folder, headers=self.headers, params=params)


    def upload_file_post(self, name_disk, link):
       params = {
                    'path': name_disk,
                    'url': link
                }
       requests.post(self.url_get_file, headers=self.headers, params=params)













