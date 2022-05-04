def is_prime(number):

    for i in range(1, number + 1):
        if i == 1 or i == number:
            return True
        else:
            return False
        
    



def run():
    number = int(input("Write a numbre: "))
    if is_prime(number):
        print("It is a prime number")
    else:
        print("It isn't a prime number.")


if __name__ == "__main__":
    run()