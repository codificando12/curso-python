def run():
    vowells = ["a", "e", "i", "o", "u"]
    phrase = input("Write a phrase: ")
    for vowell in vowells:
        times = 0
        for letter in phrase:
           if letter == vowell:
               times += 1
        print("the vowell " + vowell + " appears " + str(times) + " times")
     
        


if __name__ == "__main__":
    run()