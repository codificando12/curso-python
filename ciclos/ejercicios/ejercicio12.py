def run():
    write = input("Write a word: ")
    while write != "Exit":
        print(write)
        write = input("Write another word(if you want to leave, write 'Exit'): ")
        if write == "Exit":
            break
    print("Good Bye")


if __name__ == "__main__":
    run()