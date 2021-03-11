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

result = {}
for root, dirs, files in os.walk('some_data'):
    for file in files:
        file_size = os.path.getsize(f'some_data/{file}')
        if file_size < 100:
            if 100 in result:
                result[100] += 1
            else:
                result.setdefault(100, 1)
        elif 100 <= file_size < 1000:
            if 1000 in result:
                result[1000] += 1
            else:
                result.setdefault(1000, 1)
        elif 1000 <= file_size < 10000:
            if 10000 in result:
                result[10000] += 1
            else:
                result.setdefault(10000, 1)
        elif 10000 <= file_size < 100000:
            if 100000 in result:
                result[100000] += 1
            else:
                result.setdefault(100000, 1)

print(result)

