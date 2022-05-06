from ast import Num


def run():
    num = int(input("Write a number: "))
    for i in range(num):
    
        print(str((i + 1) * "*"))
    


if __name__ == "__main__":
    run()