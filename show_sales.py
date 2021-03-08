def show_sales(argv):
    program, *args = argv
    start = int(args[0]) if len(args) >= 1 else 0
    stop = int(args[1]) if len(args) == 2 else 0

    with open("bakery.csv", encoding='utf-8') as f:
        for line in enumerate(f):
            if start == 0:
                print(line[1].strip())
            elif start <= line[0] <= stop:
                print(line[1].strip())
            elif start <= line[0] and stop == 0:
                print(line[1].strip())


if __name__ == '__main__':
    import sys

    exit(show_sales(sys.argv))
