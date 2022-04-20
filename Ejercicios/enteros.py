def run():
    n = int(input("Elige un numero entero: "))
    suma = (n*(n+1))/2
    print("la suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))


if __name__ == "__main__":
    run()