# *(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05
import requests
import xml.etree.ElementTree as ET
from datetime import datetime


def currency_rates(argv):
    program, *args = argv
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    tree = ET.fromstring(r.text)
    date_list = tree.attrib["Date"].split(".")
    date = datetime(year=int(date_list[2]), month=int(date_list[1]), day=int(date_list[0]))
    for i in range(0, len(tree)):
        if tree[i][1].text == args[0].upper():
            print(f'Курс валюты "{tree[i][3].text}" {round(float(tree[i][4].text.replace(",", ".")), 2)}, Дата {date.day}-{date.month}-{date.year}')


if __name__ == '__main__':
    import sys

    exit(currency_rates(sys.argv))
