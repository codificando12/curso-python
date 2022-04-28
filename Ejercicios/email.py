# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo 
# electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.


def run():
    email = input("Write your e-mail address: ")
    print(email[:email.find("@")] + "@ceu.es")


if __name__ == "__main__":
    run()