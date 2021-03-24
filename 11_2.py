# Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверить его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.
class MyError(Exception):
    def __init__(self, text):
        self.text = text


a = input("Введите числитель = ")
b = input("Введите знаменатель = ")

try:
    a = int(a)
    b = int(b)
    if b == 0 and a != 0:
        raise MyError("Вы ввели 0 в качестве знаменателя")
except ValueError:
    print("Ошибка в веденных данных")
else:
    if a == 0 and b == 0:
        print(f"Результат деления {a} на {b} = 0")
    else:
        print(f"Результат вычислений {a / b}")
