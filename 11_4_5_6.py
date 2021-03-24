# 11.4
# Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведённых типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.

# 11.5
# Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

# 11.6
# Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Storage:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        self.state = {}

    def new_item(self, item, count):
        try:
            count = int(count)
            if item.name in self.state:
                self.state[item.name] += count
            else:
                self.state[item.name] = count
        except ValueError:
            print("Введено не корректное количество")

    def item_to_user(self, item, count):
        try:
            count = int(count)
            if item.name not in self.state:
                print(f'На складе нет {item.name} {item.vendor_name}')
            else:
                self.state[item.name] -= count
        except ValueError:
            print("Введено не корректное количество")


class office_equipment:
    def __init__(self, width, length, height, weight):
        self.width = width
        self.length = length
        self.height = height
        self.weight = weight


class printer(office_equipment):
    def __init__(self, name, vendor_name, width, length, height, weight):
        super().__init__(width, length, height, weight)
        self.name = name
        self.vendor_name = vendor_name


class scanner(office_equipment):
    def __init__(self, name, vendor_name, width, length, height, weight):
        super().__init__(width, length, height, weight)
        self.name = name
        self.vendor_name = vendor_name


class copier(office_equipment):
    def __init__(self, name, vendor_name, width, length, height, weight):
        super().__init__(width, length, height, weight)
        self.name = name
        self.vendor_name = vendor_name


storage = Storage(100, 100, 10)

printer_hp = printer("Принтер 1010231", "Hewlett-Packard", 5, 5, 5, 10)
scanner_hp = scanner("Сканер 1239184", "Hewlett-Packard", 5, 5, 5, 10)
copier_Xx = copier("Ксерокс", "Xerox", 5, 5, 5, 10)

storage.new_item(printer_hp, 10)
storage.new_item(scanner_hp, 10)
storage.new_item(copier_Xx, 10)

print(f'на складе сейчас хранится - {storage.state}')

storage.item_to_user(printer_hp, 1)
storage.item_to_user(scanner_hp, 5)
storage.item_to_user(copier_Xx, 10)


print(f'на складе сейчас хранится - {storage.state}')
