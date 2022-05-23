def run():
    hours = float(input("How many hours did you work last week?: "))
    wage = float(input("How much is your salary per hour? "))
    if hours > 40:
        extra = hours - 40
        extra_wage = (extra * wage) * 1.5
        print("Your week salary for this week is " + str(((wage * 40) + extra_wage)))
        


if __name__ == "__main__":
    run()