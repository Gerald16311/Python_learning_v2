# *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения
# информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>,
# <response_size>), например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
# "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?
import re

RE_REMOTE_ADDR = re.compile(r'^(\d{1,3}\.){3}\d{1,3}|^([\d\w]{0,4}[:]{1}){1,7}[\d\w]{1,4}')
RE_REQUEST_DATATIME = re.compile(r'[0-9]{2}[\/][{1}[A-Za-z]{3}[\/][{1}[0-9]{4}[:][0-9]{2}[:][0-9]{2}[:][0-9]{2}\s[+][0-9]{4}')
RE_REQUEST_TYPE = re.compile(r'["][A-Z]{3}')
RE_REQUESTED_RESOURCE = re.compile(r'[\/][[a-z]{9}[\/][[a-z]{7}[_][0-9]')
RE_RESPONSE_CODE = re.compile(r'[ ][0-9]{3}[ ]')
RE_RESPONSE_SIZE = re.compile(r'[ ][0-9]{1,8}[ ]["]')
with open('nginx_logs.txt', encoding='utf-8') as f:
    for raw in f:
        # Большое решение с использованием списка
        # result = []
        # # Работает на ipV4
        # result_ip = RE_REMOTE_ADDR.search(raw)
        # result.append(result_ip.group(0))
        # # Работает на время
        # result_request_datetime = RE_REQUEST_DATATIME.search(raw)
        # result.append(result_request_datetime.group(0))
        # # Работает на Get
        # result_request_type = RE_REQUEST_TYPE.search(raw)
        # result.append(result_request_type.group(0).replace('"', ''))
        # # Работает на ответ
        # result_requested_resource = RE_REQUESTED_RESOURCE.search(raw)
        # result.append(result_requested_resource.group(0))
        # # Работает на код ответа
        # result_response_code = RE_RESPONSE_CODE.search(raw)
        # result.append(result_response_code.group(0).replace(' ', ''))
        # # Работает на размер
        # result_response_size = RE_RESPONSE_SIZE.search(raw)
        # result.append(result_response_size.group(0).replace('"', '').replace(' ', ''))
        # # parsed_raw = tuple(result)
        # print(parsed_raw)

        parsed_raw = (RE_REMOTE_ADDR.search(raw).group(0), RE_REQUEST_DATATIME.search(raw).group(0),
                      RE_REQUEST_TYPE.search(raw).group(0), RE_REQUESTED_RESOURCE.search(raw).group(0),
                      RE_RESPONSE_CODE.search(raw).group(0).replace(' ', ''),
                      RE_RESPONSE_SIZE.search(raw).group(0).replace('"', '').replace(' ', ''))

        print(parsed_raw)