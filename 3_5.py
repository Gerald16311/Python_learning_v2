# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
# (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         	Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое
# слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное ДЗ.

from random import randrange


def get_jokes(number, no_repeat=False):
    """
    Great joke from 3 list of random strings
    1 - number - count of jokes
    2 -  no repeat names True / false
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if number > 5 and no_repeat:
        print("С текущими списками и при условии не повоторения значений не получится вывести такое количество шуток")
    else:
        while number != 0:
            result = ""
            random_nouns = randrange(len(nouns))
            result += nouns[random_nouns] + " "
            if no_repeat:
                nouns.pop(random_nouns)
            random_adverbs = randrange(len(adverbs))
            result += adverbs[random_adverbs] + " "
            if no_repeat:
                adverbs.pop(random_adverbs)
            random_adjectives = randrange(len(adjectives))
            result += adjectives[random_adjectives] + " "
            if no_repeat:
                adjectives.pop(random_adjectives)
            number -= 1
            print(result)


get_jokes(2)
get_jokes(2, True)

get_jokes(5)
get_jokes(5, True)

get_jokes(6)
get_jokes(6, True)
