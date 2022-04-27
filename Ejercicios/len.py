# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario 
# lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de 
# usuario en mayúsculas y <n> es el número de letras que tienen el nombre.


def run():
    name = input("What's your name?: ")
    name = name.upper()
    lenght = len(name)
    print("the name " + name + " has " + str(lenght) + " letters")


if __name__ == "__main__":
    run()