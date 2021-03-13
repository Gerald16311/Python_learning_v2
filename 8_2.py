# *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения
# информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>,
# <response_size>), например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
# "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
#
#
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?
import re

RE_remote_addr = re.compile(r'^[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}$')
RE_request_datetime = re.compile(r'^[0-9]{2}[{1}[A-Z]{1}[a-z]{2}[{1}[0-9]{4}[:]{1}[0-9]{2}[:]{1}[0-9]{2}[:]{1}[0-9]{2}\s{1}[+]{1}[0-9]{4}$')
RE_request_type = re.compile(r'^["]{1}[A-Z]{3}$')
RE_requested_resource = re.compile(r'^[{1}[a-z]{9}[{1}[a-z]{7}[_]{1}[0-9]{1}$')
RE_response_code = re.compile(r'^([0-9]{0,3})? ([0-9]{0,3})?$')
RE_response_size = re.compile(r'^([0-9]{0,1})? ([0-9]{0,3})?( )?$')