# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
# задания. Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.

result = []
with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        content = f.readline().split()
        result.append(content[0])
spam_ip = ""
spam_ip_count = 0
unic_set = set(result)
for ip in unic_set:
    if result.count(ip) > spam_ip_count:
        spam_ip_count = result.count(ip)
        spam_ip = ip

print(f"IP адресс спамера {spam_ip}, количество запросов {spam_ip_count}")


# unic = []
# all = []
# max=0
# with open('nginx_logs.txt', 'r') as f:
#     line = f.readline()
#     while line:
#         ip = line.strip()[0:15]
#         remote_address = ip.replace('-', '').replace(' ', '')
#         if remote_address not in unic:
#             unic.append(remote_address)
#         all.append(remote_address)
#         line = f.readline()
#
# for i in unic:
#     if all.count(i) > max:
#         max = all.count(i)
#         spamip = i
#
# print('IP спамера: ', spamip, "Количество вхождений:", max)