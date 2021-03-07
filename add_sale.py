def add_sale(argv):
    program, *args = argv
    with open("bakery.csv", 'a', encoding='utf-8') as f:
        f.write(args[0]+"\n")


if __name__ == '__main__':
    import sys

    exit(add_sale(sys.argv))
