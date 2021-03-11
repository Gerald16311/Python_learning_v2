# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать
# скрипт, который собирает все шаблоны в одну папку templates, например: |--my_project ... |--templates |
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
# которая решена, например, во фреймворке django.

# Решение получилось очень странное, но оно работает
import shutil
import os
for dir_path, dir_names, file_names in os.walk('my_project'):
    _dir_name = dir_names[0] if len(dir_names) > 0 else ""
    if _dir_name == 'templates':
        for directori in os.scandir(os.path.join(dir_path,dir_names[0])):
            shutil.copytree(directori.path, f'my_project/templates/{directori.name}')
