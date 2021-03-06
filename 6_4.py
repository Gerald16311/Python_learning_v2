# *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется,
# не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). Только теперь не нужно
# создавать словарь с данными. Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt). Хобби
# пишем через двоеточие и пробел после ФИО: Иванов,Иван,Иванович: скалолазание,охота Петров,Петр,Петрович: горные лыжи

with open('users.csv', encoding='utf-8') as users_file:
    with open('hobby.csv', encoding='utf-8') as hobby_file:
        for line in users_file:
            if line:
                hobby = hobby_file.readline()
                name = line.replace("\n", "")
                result = f'{name}: {hobby if hobby else None}'
            else:
                print("1")
            with open('users_hobby.txt', 'a', encoding='utf-8') as f:
                f.write(result)
