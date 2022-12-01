import VK
import YD


if __name__ == '__main__':
    token_VK = 'vk1.a.vVYM0eedmRCZz-ZroKIyH_Ay7rMu0lJLEJcyao_bOyvfwHyEiwi3eQIJKtZTwpNsG8tbnFbCAOCW6BKQTJN0Jl37W1PsZOiZppQfr7YQhpfKm91L3LKZ-aM4nZX8xkcgwK5Ep6Z8qSZlT4hm17OZGsFGT_QljaO-zLY5C1HvLE_9ZS0r_DXMIN2mkwSfD0MNCoSmlTRWXa6jqW1ucasgZA'
    screen_VK = 'antuanuran'

    token_YaDisk = 'y0_AgAAAAAK6z8BAADLWwAAAADTjFk3EH-r368MQZa3Fykb1Dkgkk4YvhI'
    name_folder_YaDisk = '_Folder_disk'

    vk_instance = VK.Vk_id(token_VK)
    dict_VK_result = vk_instance.name_result(screen_VK)

    yadisk_instance = YD.Load_yadisk(token_YaDisk)
    yadisk_instance.create_folder(name_folder_YaDisk)


    for i in dict_VK_result:
        name = f'{name_folder_YaDisk}/{dict_VK_result[i][0]}'
        url = dict_VK_result[i][2]
        yadisk_instance.upload_file_post(name, url)
        print(name)
        print('загружен...\n')

    yadisk_instance.upload_file_info(f'{name_folder_YaDisk}/files_info.txt', 'files_info.txt')




