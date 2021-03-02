# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
#
def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num


n = int(input("Введите до какого числа генерировать нечетные числа - "))

odd_to_n = odd_nums(n)

print(next(odd_to_n))
print(next(odd_to_n))
print(next(odd_to_n))
print(next(odd_to_n))
print(next(odd_to_n))
print(next(odd_to_n))
print(next(odd_to_n))
print(next(odd_to_n))
