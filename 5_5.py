# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список
# с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
#
#
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

# unique_items = set()
# tmp = set()
# for item in src:
#     if item not in tmp:
#         unique_items.add(item)
#     else:
#         unique_items.discard(item)
#     tmp.add(item)
#
# unique_items_ord = [item for item in src if item in unique_items]
#
# print(f"Вывод уникальных элементов {unique_items}")
# print(f"Вывод с сохраненной очередностью {unique_items_ord}")

result = [num for num in src if src.count(num) == 1]
print(f"Вывод уникальных элементов {result}")
