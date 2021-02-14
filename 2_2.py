# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и
# кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для
# чисел со знаком?

# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулем!
#
# *(вместо задачи 2) Решить задачу 2 не создавая новый список (как
# говорят, in place). Эта задача намного серьезнее, чем может сначала показаться

text_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
_numbers_list = []

for i in range(0, len(text_list)):
    number = 0
    symbol = text_list[i][0]
    if text_list[i][-1].isdigit():
        number = abs(int(text_list[i]))
        if number > 0:
            _numbers_list.append(text_list.index(text_list[i]))
        if 0 < number < 10:
            text_list[i] = f"0{number}"
        if symbol == "+" or symbol == "-":
            text_list[i] = symbol + text_list[i]
    else:
        text_list[i] = text_list[i] + " "
print(text_list)

list_length = len(text_list) - 1

for i in range(list_length, -1, -1):
    if text_list[i][-1].isdigit():
        text_list.insert(i, '"')
        text_list.insert(i + 2, '" ')

print(text_list)
print("".join(text_list))

# Старый вариант, не правильно собирается строка
# for i in range(0, len(list)):
#     number = 0
#     symbol = list[i][0]
#     try:
#         number = int(list[i])
#     except ValueError:
#         pass
#     if number > 0:
#         _numbers_list.append(list.index(list[i]))
#     if 0 < number < 10:
#         list[i] = f"0{number}"
#     if symbol == "+" or symbol == "-":
#         list[i] = symbol + list[i]
#
# print(list)
# _numbers_list.reverse()
#
# for item in _numbers_list:
#     list.insert(item + 1, '"')
#     list.insert(item, '"')
#
# print(list)
# print(" ".join(list))


