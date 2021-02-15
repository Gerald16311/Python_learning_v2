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


def thesaurus_adv(name1, name2, name3, name4, name5):
    names_list = [name1.split(" "), name2.split(" "), name3.split(" "), name4.split(" "), name5.split(" ")]
    print(names_list)

    for name in names_list:
        if name[1][0] in users_dict:
            pass
        else:
            users_dict[name[1][0]] = {}

    for name in names_list:
        if name[0][0] in users_dict[name[1][0]]:
            users_dict[name[1][0]][name[0][0]].append(" ".join(name))
        else:
            users_dict[name[1][0]].update({name[0][0]: [(" ".join(name))]})
    return users_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))