cantidad = input("¿Qué quieres cambiar?: ")
if cantidad == "ars":
    pesos = input("¿Cuántos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 200
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif cantidad == "cop":
    pesos_cop = input("¿Cuántos pesos colombianos tienes?: ")
    pesos_cop = float(pesos_cop)
    valor_dolar = 3756
    dolares = pesos_cop / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
else:
    print("no disponemos de esa moneda")