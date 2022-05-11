def run():
    subjets = ["Math", "Grammar", "History", "Spanish", "Chemistry"]
    notes = []
    for subjet in subjets:
        note = input("What is your score in " + subjet + ":")
        notes.append(note)
    for i in range(len(subjets)):               
        print("Your score in " + subjets[i] + " is: " + notes[i])


if __name__ == "__main__":
    run()