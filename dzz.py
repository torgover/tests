geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

stats = {'facebook': 55, 'vk': 115,'yandex': 120, 'google': 99, 'email': 42, 'ok': 98}

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}



def max_value():
    value = max(stats.values())
    for k, v in stats.items():
        if v == value:
            return k



def ids_list():
    result = set()
    for k in ids.values():
        result.update(k)
    return list(result)


def geo_log(listvalue, param):
    sortedlist = []
    for val in listvalue:
        if list(val.values())[0][1] == param:
            sortedlist.append(val)
    return sortedlist
            

