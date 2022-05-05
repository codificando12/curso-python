def run():
    invest = int(input("How much do you want to invest: "))
    interest = int(input("What interest rate per year would you like to receive?: "))
    years = int(input("How many years would you like to invest?: "))
    for i in range(years):
        invest *= 1 + interest / 100
        print("After " + str(i + 1) + " years: " + str(round(invest, 2)))


if __name__ == "__main__":
    run()