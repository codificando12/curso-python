def run():
    contador = 1
    print(contador)
    while contador < 1000:
        contador = contador + 1
        if contador % 2 != 0:
            continue
        elif contador == 700:
            break
        print(contador)

  
    


        


if __name__ == "__main__":
    run()