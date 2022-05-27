# def run():
#     hours = float(input("How many hours did you work last week?: "))
#     wage = float(input("How much is your salary per hour? "))
#     if hours > 40:
#         extra = hours - 40
#         extra_wage = (extra * wage) * 1.5
#         print("Working hours " + str(hours) + "\n" + 
#               "Extra hours: " + str(extra) + "\n" +
#               "Normal salary: " + str(wage * 40) + "\n" +
#               "Extra salary: " + str(extra_wage) + "\n" +
#               "Total for this week: " + str((wage * 40) + extra_wage))       
#     else:
#            print("Working hours " + str(hours) + "\n" + 
#               "Extra hours: 0" + "\n" +
#               "Normal salary: " + str(wage * hours) + "\n" +
#               "Extra salary: 0" + "\n" +
#               "Total for this week: " + str(wage * hours))  

# if __name__ == "__main__":
#     run()
 
 
    
def run():
    hours = float(input("How many hours did you work last week?: "))
    wage = float(input("How much is your salary per hour? "))
    
    def e_extra(hour, wage):
        if hour > 40:
            extra = hour - 40
            extra_wage = (extra * wage) * 1.5
            print("Working hours " + str(hours) + "\n" + 
                "Extra hours: " + str(extra) + "\n" +
                "Normal salary: " + str(wage * 40) + "\n" +
                "Extra salary: " + str(extra_wage) + "\n" +
                "Total for this week: " + str((wage * 40) + extra_wage))       
        else:
            print("Working hours " + str(hours) + "\n" + 
                "Extra hours: 0" + "\n" +
                "Normal salary: " + str(wage * hour) + "\n" +
                "Extra salary: 0" + "\n" +
                "Total for this week: " + str(wage * hour))
              
    e_extra(hours, wage)
if __name__ == "__main__":
    run()