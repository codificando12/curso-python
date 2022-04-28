# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e 
# imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.


def run():
    password = input("Please, write a password: ")
    answer = input("What is your password?: ")
    
    if answer == password.lower():
        print("The password is correct")
    else:
        print("Please, write the right password.")


if __name__ == "__main__":
    run()
