# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
#
#
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
import os

my_project = {
    'name': 'my_project',
    'dir1': ('settings', 'settings_dir1', 'settings_dir2'),
    'dir2': ('mainapp', 'mainapp_dir1', 'mainapp_dir2'),
    'dir3': ('adminapp', 'adminapp_dir1', 'adminapp_dir2'),
    'dir4': ('authapp', 'aauthapp_dir1', 'authapp_dir2'),
}


def new_project(project_name):
    for dir, dir_name in project_name.items():
        if type(dir_name) == str:
            if not os.path.isdir(project_name.get("name")):
                os.mkdir(project_name.get("name"))
            os.chdir(project_name.get("name"))
        else:
            os.makedirs('/'.join(dir_name))


new_project(my_project)
