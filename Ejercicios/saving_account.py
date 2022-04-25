# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al 
# balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la 
# cantidad de dinero depositada en la cuenta de ahorros, 
# introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la 
# cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.


def run():
    account = int(input("How much money do you want to deposit?: "))
    interest = 4
    first = round(account * (interest / 100 + 1) ** 1, 2)
    second = round(account * (interest / 100 + 1) ** 2, 2)
    thrid = round(account * (interest / 100 + 1) ** 3, 2)
    print("the first year your account will have: $ " + str(first) + ", the second year your account will have: $" 
          + str(second) + ", and the third year your accont will have: $" + str(thrid) )

if __name__ == "__main__":
    run()