# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.


def run():
    word = input("write a word: ")
    print(word[: : -1])


if __name__ == "__main__":
    run()

