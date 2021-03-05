# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби. Известно,
# что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями —
# запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения —
# данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби,
# меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ. Фрагмент файла с данными о
# пользователях (users.csv): Иванов,Иван,Иванович Петров,Петр,Петрович
#
# Фрагмент файла с данными о хобби  (hobby.csv):
# скалолазание,охота
# горные лыжи
#
result = {}

with open('users.csv', encoding='utf-8') as users_file:
    with open('hobby.csv', encoding='utf-8') as hobby_file:
        names_line = users_file.readline()
        hobby_line = hobby_file.readline()
        while names_line:
            if not names_line:
                print("1")
                break
            else:
                names_line = users_file.readline()
                user_name = names_line.replace("\n", "")

        while hobby_line:
            if not hobby_line:
                user_hobby = "None"
                hobby_line = hobby_file.readline()
            else:
                hobby_line = hobby_file.readline()
                user_hobby = hobby_line.replace("\n", "")

        result[user_name] = user_hobby

print(result)
