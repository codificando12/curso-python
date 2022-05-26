def run():
    score = input("write your score from 0.0 to 1.0 to know if you pass it: ")
    try:
        point = float(score)
        if point >= 0.9:
            print("Outstanding")
        elif point >= 0.8:
            print("Remarkable")
        elif point >= 0.7:
            print("Good")
        elif point >= 0.6:
            print("Enought")
        else:
            print("Insufficient")
    except:
        print("Please write a number from 0.0 to 1.0")


if __name__ == "__main__":
    run()





