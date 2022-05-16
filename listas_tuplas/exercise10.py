def run():
    vec1 = [1, 2, 3]
    vec2 = [-1, 0, 2]
    product = 0
    for i in range(len(vec1)):
        product += vec1[i] * vec2[i]
    print("The product of vectors " + str(vec1) + " " + str(vec2) + " is: " + str(product))


if __name__ == "__main__":
    run()