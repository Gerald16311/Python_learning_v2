# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для
# перевода: какой тип данных выбрать, в теле функции или снаружи.

# создал словарь как глобальную переменную, для возмождности его использования в других функциях
dict = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять",
}


def num_translate(number_name):
    """Rename english number to russ"""
    if number_name in dict:
        return dict[number_name]
    else:
        return None


print(num_translate("eight"))
print(num_translate("one"))
print(num_translate("123"))
