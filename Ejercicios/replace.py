# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y 
# después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.


def run():
    phrase = input("Write a phrase: ")
    vowell = input("Write a vowell in lower case: ")
    print(phrase.replace(vowell, vowell.upper()))



if __name__ == "__main__":
    run()