# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (USD, EUR, ...) и возвращающую курс
# этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере,
# посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу? Функция
# должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
# величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от
# того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
import requests
import xml.etree.ElementTree as ET


def currency_rates(cur):
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    tree = ET.fromstring(r.text)
    for i in range(0, len(tree)):
        # print(f"{tree[i][1].text} и {cur.upper()}")
        if tree[i][1].text == cur.upper():
            return float(tree[i][4].text.replace(",", "."))


print(currency_rates('USD'))
print(currency_rates('Eur'))
print(currency_rates('BACKS'))
