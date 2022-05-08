def run():
    phrase = str(input("Write a phrase: "))
    for i in range(len(phrase)-1, -1, -1):
        print(phrase[i])
    


if __name__ == "__main__":
    run()