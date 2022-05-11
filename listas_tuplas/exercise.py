def run():
    subjets = ["Math", "Grammar", "History", "Spanish", "Chemistry"]
    for subjet in subjets:
        notes = input("What is your score in " + subjet + ":")
    print("Your score in " + subjet + " is: " + notes)


if __name__ == "__main__":
    run()