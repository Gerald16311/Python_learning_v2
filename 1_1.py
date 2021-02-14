# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности

# duration в секундах:
# до минуты: <s> сек;
# * до часа: <m> мин <s> сек;
# * до суток: <h> час <m> мин <s> сек;
# * *до месяца, до года, больше года: по аналогии.

duration = int(input("Введите промежуток времени в секундах: "))
result = ""
while duration != 0:
    if duration > 3153600:
        result += str(duration // 31536000) + " лет "
        duration -= (duration // 31536000) * 31536000
    elif duration > 2678400:
        result += str(duration // 2678400) + " месяцев "
        duration -= (duration // 2678400) * 2678400
    elif duration > 86400:
        result += str(duration // 86400) + " дней "
        duration -= (duration // 86400) * 86400
    elif duration > 3600:
        result += str(duration // 3600) + " часов "
        duration -= (duration // 3600) * 3600
    elif duration > 60:
        result += str(duration // 60) + " минут "
        duration -= (duration // 60) * 60
    elif duration > 0:
        result += str(duration) + " секунд "
        duration -= duration
print(result)
