def run():
    phrase = input("Write a phrase: ")
    letter = input("Choose a letter: ")
    counter = 0
    for i in phrase:
        if i == letter:
            counter += 1
            
    print("The letter '%s' appears %2i times in this phrase: '%s'." % (letter, counter, phrase))
        


if __name__ == "__main__":
    run()


