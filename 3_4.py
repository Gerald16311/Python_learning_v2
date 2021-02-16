# *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
# и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме
# предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?
users_dict = {}


def thesaurus_adv(*names_list):
    print(names_list)
    for name in names_list:
        name_spl = name.split(" ")
        if name_spl[1][0] in users_dict:
            pass
        else:
            users_dict[name_spl[1][0]] = {}
        if name_spl[0][0] in users_dict[name_spl[1][0]]:
            users_dict[name_spl[1][0]][name_spl[0][0]].append(name)
        else:
            users_dict[name_spl[1][0]].update({name_spl[0][0]: [name]})
    return users_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))