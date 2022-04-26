# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima 
# por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.


def run():
    name = input("What is your name?: ")
    n = input("write a number: ")
    print((name + "\n") * int(n))


if __name__ == "__main__":
    run()