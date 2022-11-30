import VK
from pprint import pprint


token = 'vk1.a.vVYM0eedmRCZz-ZroKIyH_Ay7rMu0lJLEJcyao_bOyvfwHyEiwi3eQIJKtZTwpNsG8tbnFbCAOCW6BKQTJN0Jl37W1PsZOiZppQfr7YQhpfKm91L3LKZ-aM4nZX8xkcgwK5Ep6Z8qSZlT4hm17OZGsFGT_QljaO-zLY5C1HvLE_9ZS0r_DXMIN2mkwSfD0MNCoSmlTRWXa6jqW1ucasgZA'
screen_n = 'antuanuran'

id_1 = VK.Vk_id(token)
id_1.name_result(screen_n)

a = id_1.date_like_name_all(screen_n)
pprint(a)