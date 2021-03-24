# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый — с декоратором @classmethod. Он должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class data:
    def __init__(self, date):
        date = date.split("-")
        self.day = date[0]
        self.month = date[1]
        self.year = date[2]

    @classmethod
    def to_int(cls, date):
        date = date.split("-")
        cls.date = int(date[0])
        cls.month = int(date[1])
        cls.year = int(date[2])

    @staticmethod
    def validate(date):
        date = date.split("-")
        if 1 <= int(date[0]) <= 31 and 1 <= int(date[1]) <= 12 and 0 < int(date[2]):
            print("Введены КОРРЕКТНЫЕ данные")
        else:
            print("Введены не корректные данные")


a = data("12-12-12")
a.to_int("12-12-12")
print(a.month, a.year, a.date)
a.validate("15-15-15")