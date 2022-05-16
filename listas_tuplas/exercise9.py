def run():
    price = [50, 75, 46, 22, 80, 65, 8]
    min = max = price[0]
    for p in price:
        if p < min:
            min = p
        elif p > max:
            max = p
    print("The chepeast prices is " + str(min))
    print("The more expensive prices is " + str(max))
    


if __name__ == "__main__":
    run()