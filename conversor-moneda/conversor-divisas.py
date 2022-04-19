# def divisas(mensaje,valor_peso):
#     peso = input("Cuantos pesos " + mensaje + " tienes?: ")
#     peso = float(peso)
#     dolares = peso / valor_peso
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("tienes $" + dolares + "dolares")


# menu = """
# Que moneda deseas cambiar, elige una opcion:

# 1 - pesos argentinos
# 2 - pesos colombianos
# """

# cantidad = input(menu)


def suma(a, b):
    print("se suman dos numeros")
    resultado = a + b
    return resultado

sumatoria = suma(1, 4)

print(sumatoria)



# if cantidad == "1":
#     divisas("argentinos", 200)
# elif cantidad == "2":
#     divisas("colombianos", 3576)
# else:
#     print("elige la opcion correcta")

































# cantidad = input("¿Qué quieres cambiar?: ")
# if cantidad == "ars":
#     pesos = input("¿Cuántos pesos argentinos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar = 200
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dólares")
# elif cantidad == "cop":
#     pesos = input("¿Cuántos pesos colombianos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar = 3756
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dólares")
# else:
#     print("no disponemos de esa moneda")



















# menu = """
#     ¿Qué quieres cambiar? elige una opcion:
#     1 - ars
#     2 - cop
#  """

# cantidad = input(menu)

# def conversor(mensaje,moneda):
#     pesos = input(mensaje)
#     pesos = float(pesos)
#     valor_dolar = moneda
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dólares")


# if cantidad == "1":
#     conversor("Cuantos pesos argentinos tienes?", 200)
    
   
# elif cantidad == "2":
#     conversor("Cuantos pesos colombianos tienes?", 3756)    
# else:
#     print("no disponemos de esa moneda")