def run():
    num = int(input("write a positive pair number: "))
    for i in range(1, num + 1, 2):
        print(i, end=", ")


if __name__ == "__main__":
    run()