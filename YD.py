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
        params =      {
                        'path': name_folder
                      }
        response = requests.put(self.url_get_folder, headers=self.headers, params=params).json()


    def get_link_file(self, name_disk):
        params =      {
                        'path': name_disk,
                        'overwrite': 'true'
                      }
        response = requests.get(self.url_get_file, headers=self.headers, params=params).json()
        return response['href']


    def upload_file_put(self, name_disk, link):
        href = self.get_link_file(name_disk)
        requests.put(href, link)



if __name__ == '__main__':
    name_disk = '_Folder_disk/123.jpg'
    name_file = '123.jpg'
    link_file = 'https://sun9-16.userapi.com/impf/MNQvl7_QKzdZDrcLfrTbG7cdyz8jiVXw6Bf7cA/RSD0QGW2b_A.jpg?size=919x1080&quality=96&sign=090c7e0ee2aaa2c080c958dce621fe3d&c_uniq_tag=zc82O6dxznZBmJOReeY2x4X048GIEJ7M_ycQWdFOrCU&type=album'
    name_folder = '_Folder_disk'
    token = 'y0_AgAAAAAK6z8BAADLWwAAAADTjFk3EH-r368MQZa3Fykb1Dkgkk4YvhI'

    load_1 = Load_yadisk(token)
    load_1.create_folder(name_folder)
    load_1.upload_file_put(name_disk, link_file)

