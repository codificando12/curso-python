def run():
    file = input("Write the file's name: ")
    print(file)
    open_file = open(file)
    for lines in open_file:
        space = lines.rstrip()
        cap = space.upper()
        print(cap)


if __name__ == '__main__':
    run()