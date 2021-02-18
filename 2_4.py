# Создать вручную список, содержащий цены на товары (10–20 товаров), например: [57.8, 46.51, 97, ...]
cost_list = [55.3, 23.4, 22.12, 24.65, 46, 76.8, 358, 569, 87, 54.9, 75, 23.5, 23, 41.9, 85.7, 65.4, 295, 43, 41, 75.6,
             86, 23.45, 7, 4.5, 5.06]
result = ""
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например
# «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7
# копеек или 0 копеек (должно быть 07 коп или 00 коп).
for item in cost_list:
    if isinstance(item, int):
        if item >= 10:
            result = f"{item} руб 00 коп"
        else:
            result = f"{item} руб 00 коп"
        cost_list[cost_list.index(item)] = result
    else:
        ruble = int(item)
        kops = round((item - int(item)) * 100)
        if ruble >= 10:
            result = f"{ruble} руб "
        elif ruble < 10:
            result = f"{ruble} руб "
        if kops >= 10:
            result += f"{kops} коп"
        elif kops < 10:
            result += f"0{kops} коп"
        cost_list[cost_list.index(item)] = result
print(", ".join(cost_list))

# Вывести цены, отсортированные по возрастанию, новый список не создавать ( доказать, что объект списка после сортировки
# остался тот же).
print(cost_list)
print(f"Идентификатор созданного списка {id(cost_list)}")

cost_list.sort(key=lambda item2: int(item2.split(" ")[0]) * 100 + int(item2.split(" ")[2]))
print(cost_list)
print(f"Идентификатор отсортированного списка {id(cost_list)}")

# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
cost_list_to_lower = sorted(cost_list, key=lambda item2: int(item2.split(" ")[0]) * 100 + int(item2.split(" ")[2]),
                            reverse=True)
print(cost_list_to_lower)
print(f"Идентификатор нового списка отсортированного по убыванию {id(cost_list_to_lower)}")

# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print("список 5 самых дорогих товаров")
print(cost_list_to_lower[:5])
