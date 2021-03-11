# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
# почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в
# данном случае использовать функцию re.compile()?

import re
RE_EMAIL = re.compile(r'^[A-Za-z0-9]{1,10}@[A-Za-z0-9]{2,10}\.[a-z]{2,6}$')


def email_parse(email):
    result = {'username': 'someone', 'domain': 'geekbrains.ru'}
    assert RE_EMAIL.match(email), f"не правильный email"
    email_list = email.split("@")
    result['username'] = email_list[0]
    result['domain'] = email_list[1]
    return result


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
print(email_parse('_someone@geekbr_ains748754.ru4564.com'))
print(email_parse('someone@@geekbrains.ru'))
print(email_parse('someone@geekbrains.ru'))
