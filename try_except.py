def run():
    hour = input("How many hours did you work last week?: ")
    wages = input("How much is your salary per hour? ")
    try:
        hours = float(hour)
        wage = float(wages)
        if hours > 40:
            extra = hours - 40
            extra_wage = (extra * wage) * 1.5
            print("Working hours " + str(hours) + "\n" + 
              "Extra hours: " + str(extra) + "\n" +
              "Normal salary: " + str(wage * 40) + "\n" +
              "Extra salary: " + str(extra_wage) + "\n" +
              "Total for this week: " + str((wage * 40) + extra_wage))       
        else:
           print("Working hours " + str(hours) + "\n" + 
              "Extra hours: 0" + "\n" +
              "Normal salary: " + str(wage * hours) + "\n" +
              "Extra salary: 0" + "\n" +
              "Total for this week: " + str(wage * hours))
    except:
        print("Error, please write a number in hours and salary")
      

if __name__ == "__main__":
    run()