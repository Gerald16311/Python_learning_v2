# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
# задания. Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.

# result = []
#
# with open('nginx_logs.txt', encoding='utf-8') as f:
#     line = f.readline()
#     while line:
#         content = line.split(" ")
#         result.append(content[0])
#         line = f.readline()
#
# spam_ip = ""
# spam_ip_count = 0
# unic_set = set(result)
# for ip in unic_set:
#     if result.count(ip) > spam_ip_count:
#         spam_ip_count = result.count(ip)
#         spam_ip = ip
#
# print(f"IP адресс спамера {spam_ip}, количество запросов {spam_ip_count}")

# result = []
#
# with open('nginx_logs.txt', encoding='utf-8') as f:
#     for line in f:
#         content = line.split()
#         result.append(content[0])
#
# spam_ip = ""
# spam_ip_count = 0
# unic_set = set(result)
# for ip in unic_set:
#     if result.count(ip) > spam_ip_count:
#         spam_ip_count_for = result.count(ip)
#         spam_ip_for = ip
#
# print(f"IP адресс спамера {spam_ip}, количество запросов {spam_ip_count}")

result = {}

with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        content = line.split()
        if content[0] in result:
            result[content[0]] += 1
        else:
            result[content[0]] = 1

max_ip_count = max(result, key=result.get)

print(f"IP адресс спамера {max_ip_count}, количество запросов {result[max_ip_count]}")
