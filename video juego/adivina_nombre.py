import random


def run():
    vidas = 5
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un numero del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Elige un número más grande")
            vidas -= 1
        elif numero_elegido > numero_aleatorio:
            print("Elige un número más chico")
            vidas -= 1
        if vidas == 0:
            print("game over ")
            break
        print("Tienes " + str(vidas) + " vidas")
            
        numero_elegido = int(input("Elige otro número: "))
        if numero_elegido == numero_aleatorio:
            print("¡Ganaste!")


if __name__ == "__main__":
    run()