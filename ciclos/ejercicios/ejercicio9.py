def run():
    times = 3
    password = input("Write a password: ")
    ask = input("What is your password? ")
    while password != ask:
        times -= 1
        print("the password is wrong")
        print("you have " + str(times) + " left")
        if times == 0:
            print("Try again in 10 minutes")
            break
        ask = input("Write the password again: ")
        if password == ask:
            print("the password is correct")
        
        


if __name__ == "__main__":
    run()