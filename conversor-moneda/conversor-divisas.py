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


def conversor(moneda):
    pesos = input("¿Cuántos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = moneda
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


menu = """
    ¿Qué quieres cambiar? elige una opcion:
    1 - ars
    2 - cop
 """

cantidad = input(menu)




if cantidad == "1":
   moneda = 200
elif cantidad == "2":
    moneda = 3756
else:
    print("no disponemos de esa moneda")