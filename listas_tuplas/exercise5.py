# def run():
#     num = [0, 1 , 2 , 3, 4, 5, 6,  7, 8, 9, 10]
#     for i in range(1, 11):
#         print(num[-i], end=",")


# if __name__ == "__main__":
#     run()


def run():
    num = [0, 1 , 2 , 3, 4, 5, 6,  7, 8, 9, 10]
    num.reverse()
    for i in num:
        print(i, end=",")


if __name__ == "__main__":
    run()