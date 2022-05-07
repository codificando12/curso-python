def run():
    times = 3
    password = input("Write a password: ")
    ask = input("What is your password? ")
    while password == ask:
        print("The password is correct")
        
        if password != ask:
            print("the password is wrong, write another password: ")
        
        


if __name__ == "__main__":
    run()