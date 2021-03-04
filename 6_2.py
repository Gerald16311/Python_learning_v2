# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
# задания. Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.

result = []
with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        content = f.readline().split()
        result.append(content[0])

spam_ip = result[0]
spam_ip_count = result.count(spam_ip)
for ip in result:
    if result.count(ip) > spam_ip_count:
        spam_ip_count = result.count(ip)
        spam_ip = ip

print(f"IP адресс спамера {spam_ip}, кодличество запросов {spam_ip_count}")
