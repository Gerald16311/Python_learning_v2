def edit_sale(argv):
    program, *args = argv
    all_file = []
    item_number = int(args[0])
    new_value = args[1]
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            all_file.append(line.strip())
    if item_number - 1 > len(all_file):
        print("попытка изменения не существующей записи")
    else:
        all_file[item_number-1] = new_value
        with open('bakery.csv', 'w', encoding='utf-8') as f:
            f.write("\n".join(all_file))


if __name__ == '__main__':
    import sys
    exit(edit_sale(sys.argv))