# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
# размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
# {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
#
# #
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
import os

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
