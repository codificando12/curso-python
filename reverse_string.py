def run():
    
    fruit = "banana"
    count = 0
    while count < len(fruit):
        fruitr = fruit[::-1]
        letter = fruitr[count]
        print(letter)
        count = count + 1


if __name__ == "__main__":
    run()