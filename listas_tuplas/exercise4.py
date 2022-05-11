from socket import NI_NUMERICSERV


def run():
    nums = []
    for i in range(6):
        nums.append(int(input("Write the past lotery numbers:")))
    nums.sort()
    print("The winner numbers are : " + str(nums))
   
 
if __name__ == "__main__":
    run()