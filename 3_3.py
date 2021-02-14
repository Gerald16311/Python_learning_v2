# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором
# ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки?
# Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае
users_dict = {}


def thesaurus(name):
    users_dict.update({name[0]: name})
    return users_dict


print(thesaurus("Иван"))
print(thesaurus("Мария"))
print(thesaurus("Петр"))
print(thesaurus("Илья"))
