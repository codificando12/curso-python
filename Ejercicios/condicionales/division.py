# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.


def run():
    number_1 = int(input("Please, write a number: "))
    number_2 = int(input("Write another number: "))
    division = number_1 / number_2
    if number_2 == 0:
        print("can not divide in 0")
    else:
        print("the divison result is " + str(division))


if __name__ == "__main__":
    run()