import requests
import xml.etree.ElementTree as ET
from datetime import datetime


def currency_rates(cur):
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    tree = ET.fromstring(r.text)
    date_list = tree.attrib["Date"].split(".")
    date = datetime(year=int(date_list[2]), month=int(date_list[1]), day=int(date_list[0]))
    for i in range(0, len(tree)):
        # print(f"{tree[i][1].text} и {cur.upper()}")
        if tree[i][1].text == cur.upper():
            return f"Дата {date.day}-{date.month}-{date.year} Курс валюты {float(tree[i][4].text.replace(',', '.'))}"


if __name__ == '__main__':
    currency_rates('Иван')
