from stringprep import in_table_c3


def run():
    subjets = ["Math", "Grammar", "History", "Spanish", "Chemistry"]
    passed = []
    for subjet in subjets:
        note = float(input("What is your score in " + subjet + "? "))
        if note >= 7:
            passed.append(subjet)
    for subjet in passed:
        subjets.remove(subjet)
    print("You need to repeat " + str(subjets))
     

if __name__ == "__main__":
    run()