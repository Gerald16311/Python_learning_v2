# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
# исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
#
# Примечание: сможете ли вы замаскировать работу декоратора?
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.

def val_checker(lam):
    def wrapper(func):
        def inner(arg):
            if not lam(arg):
                raise ValueError(f'wrong val {arg}')
            return func(arg)
        return inner
    return wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
a = calc_cube(-5)
print(a)
