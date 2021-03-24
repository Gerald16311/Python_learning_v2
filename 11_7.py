# Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». Реализовать перегрузку
# методов сложения и умножения комплексных чисел. Проверить работу проекта. Для этого создать экземпляры класса (
# комплексные числа), выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного
# результата.
class komplex_number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f"сложение {self.a + other.a} + {self.b + other.b}i"

    def __sub__(self, other):
        return f"вычитание {self.a - other.a} + {self.b - other.b}i"

    def __mul__(self, other):
        return f"умножение {self.a * other.a - self.b * other.b} + {self.b * other.a + self.a * other.b}i"


a = komplex_number(1, 5)
b = komplex_number(1, 5)

print(a + b)
print(a - b)
print(a * b)
