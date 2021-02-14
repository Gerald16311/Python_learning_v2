# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы - результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

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


def num_translate_adv(number_name):
    """Rename english number to russ"""
    number_name_lower = number_name.lower()
    if number_name_lower in dict and number_name[0].isupper():
        return dict[number_name_lower].capitalize()
    elif number_name_lower in dict:
        return dict[number_name]
    else:
        return None


print(num_translate_adv("eight"))
print(num_translate_adv("one"))
print(num_translate_adv("123"))

print(num_translate_adv("Eight"))
print(num_translate_adv("One"))
