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
import shutil
import os
for dir in os.scandir('my_project'):
    for dir2 in os.scandir(dir):
        print(dir2.name)
        print(dir2.path)
        if dir2.name == 'templates':
            shutil.copytree(dir2.path, 'my_project/templates/')
