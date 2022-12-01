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


if __name__ == '__main__':
    name_disk = '_Folder_disk/123.jpg'
    name_file = '123.jpg'
    link_file = 'https://sun9-16.userapi.com/impf/MNQvl7_QKzdZDrcLfrTbG7cdyz8jiVXw6Bf7cA/RSD0QGW2b_A.jpg?size=919x1080&quality=96&sign=090c7e0ee2aaa2c080c958dce621fe3d&c_uniq_tag=zc82O6dxznZBmJOReeY2x4X048GIEJ7M_ycQWdFOrCU&type=album'
    name_folder = '_Folder_disk'
    token = 'y0_AgAAAAAK6z8BAADLWwAAAADTjFk3EH-r368MQZa3Fykb1Dkgkk4YvhI'

    # list_1 = [{'32.jpg': 'file_name', 'z': 'max size', '3.jpg': 'file_name', 'w': 'max size', '3_[2021-03-02_18:07:48].jpg': 'file_name', 'x': 'max size'}]
    #
    # list_2 = [{'2018-02-04_12:01:35': ['32.jpg', 'z',  'https://sun9-16.userapi.com/impf/MNQvl7_QKzdZDrcLfrTbG7cdyz8jiVXw6Bf7cA/RSD0QGW2b_A.jpg?size=919x1080&quality=96&sign=090c7e0ee2aaa2c080c958dce621fe3d&c_uniq_tag=zc82O6dxznZBmJOReeY2x4X048GIEJ7M_ycQWdFOrCU&type=album'],
    #            '2020-03-11_11:18:52': ['3.jpg', 'w',   'https://sun9-39.userapi.com/impg/c858528/v858528142/11c2d2/9UT49kS8K7E.jpg?size=2388x2160&quality=96&sign=40d39d8e80ab9c09f63eac8b86dd088a&c_uniq_tag=oYZilw8v3riaHkRIdALhFtP0cZLmguuyUO8gCdqNxEM&type=album'],
    #            '2021-03-02_18:07:48': ['3_[2021-03-02_18:07:48].jpg', 'x', 'https://sun9-52.userapi.com/impg/p7avRL55PQJ46d2rPe7oUZjZh-YoRX_-Zl-_Sg/L90FAys2UVo.jpg?size=500x500&quality=96&sign=ab510c2ad8131c896ecfe89c54dba1d9&c_uniq_tag=wAU9pR2GHEzflwYpDeXwaBD_mcO7W8EqXo_8SXjEWBU&type=album']
    #            }]



    load_1 = Load_yadisk(token)
    load_1.create_folder(name_folder)
    load_1.upload_file_post(name_disk, link_file)

