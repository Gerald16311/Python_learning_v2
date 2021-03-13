# *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
# а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
# {
#     100: (15, ['txt']),
#     1000: (3, ['py', 'txt']),
#     10000: (7, ['html', 'css']),
#     100000: (2, ['png', 'jpg'])
# }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.

import os
import json
folder_path = "some_data"
result = {}
result_list_100 = []
result_list_1000 = []
result_list_10000 = []
result_list_100000 = []

for root, dirs, files in os.walk(folder_path):
    for file in files:
        result_list_100.append(file.split(".")[-1]) if os.path.getsize(f'{folder_path}/{file}') < 100 else ""
        result_list_1000.append(file.split(".")[-1]) if 100 <= os.path.getsize(f'{folder_path}/{file}') < 1000 else ""
        result_list_10000.append(file.split(".")[-1]) if 1000 <= os.path.getsize(f'{folder_path}/{file}') < 10000 else ""
        result_list_100000.append(file.split(".")[-1]) if 10000 <= os.path.getsize(f'{folder_path}/{file}') else ""

result[100] = (str(len(result_list_100)), list(set(result_list_100)))
result[1000] = (str(len(result_list_1000)), list(set(result_list_1000)))
result[10000] = (str(len(result_list_10000)), list(set(result_list_10000)))
result[100000] = (str(len(result_list_100000)), list(set(result_list_100000)))

# print(result)
result_as_str = json.dumps(result)
with open(f'{folder_path}.json', 'w', encoding='utf-8') as f:
   f.write(result_as_str)

