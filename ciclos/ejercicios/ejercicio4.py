def run():
    num = int(input("write a number: "))
    for i in range(num, - 1, -1):
        print(i, end=", ")


if __name__ == "__main__":
    run()