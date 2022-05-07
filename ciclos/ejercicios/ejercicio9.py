def run():
    times = 3
    password = input("Write a password: ")
    ask = input("What is your password? ")
    while password != ask:
        print("the password is wrong")
        break
    print(input("please write it again: "))

    if password == ask:
        print("the password is correct")
        
        


if __name__ == "__main__":
    run()