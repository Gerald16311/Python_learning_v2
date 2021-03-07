def show_sales(argv):
    program, *args = argv
    count = 0
    start, stop = 0, 0

    if len(args) == 2:
        start = int(args[0])
        stop = int(args[1])
    elif len(args) == 1:
        start = int(args[0])

    print(start)
    print(stop)

    with open("bakery.csv", encoding='utf-8') as f:
        for line in f:
            count += 1
            if not args:
                print(line.replace("\n", ""))
            elif start <= count <= stop:
                print(line.replace("\n", ""))
            elif start <= count and len(args) == 1:
                print(line.replace("\n", ""))


if __name__ == '__main__':
    import sys

    exit(show_sales(sys.argv))
