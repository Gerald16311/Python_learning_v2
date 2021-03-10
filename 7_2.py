# *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не
# программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
import os
with open('config.yaml') as f:
    for line in f:
        if not os.path.exists(os.path.dirname(line.strip())):
            os.makedirs(os.path.dirname(line.strip()))
        with open(f'{os.path.dirname(line.strip())}/{os.path.basename(line.strip())}', 'w') as item:
            pass
