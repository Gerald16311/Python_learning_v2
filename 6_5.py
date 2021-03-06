# **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя обоих исходных
# файлов и имя выходного файла. Проверить работу скрипта.
import sys


def add_information(argv):
    program, *args = argv
    user_file = args[0]
    hobb_file = args[1]
    result_file = args[2]
    with open(user_file, encoding='utf-8') as users_file:
        with open(hobb_file, encoding='utf-8') as hobby_file:
            for line in users_file:
                if line:
                    hobby = hobby_file.readline()
                    name = line.replace("\n", "")
                    result = f'{name}: {hobby if hobby else None}'
                else:
                    print("1")
                with open(result_file, 'a', encoding='utf-8') as f:
                    f.write(result)


if __name__ == '__main__':
    import sys

    exit(add_information(sys.argv))
