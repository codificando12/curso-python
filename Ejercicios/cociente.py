def run():
    n = input("Escribe un número: ")
    m = input("Escribe otro número: ")
    c = float(n) // float(m)
    r = float(n) % float(m)
    print(str(n) + " entre " + str(m) + " da un cociente de " + str(c) + " y un resto de " + str(r))


if __name__ == "__main__":
    run()