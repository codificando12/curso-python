# def run():
#     a = ((1, 2, 3), 
#          (4, 5, 6))
#     b = ((-1, 0),
#          (0, 1),
#          (1, 1))
#     result = [[0, 0],
#               [0, 0]]
#     for i in range(len(a)):
#         for j in range(len(b[0])):
#             for k in range(len(b)):
#                 result[i] [j] += a[i][k] * b[k][j]
#     for i in range(len(result)):
#         result[i] = tuple(result[i])
#     result = tuple(result)
#     for i in range(len(result)):
#         print(result[i])           
        


# if __name__ == "__main__":
#     run()

cel = input("Write your city temperature in celcius: ")
far = 0
try:
    celc = float(cel)
    far = (celc * (9/5)) + 32
except:
    print("write a proper number")

print(str(far))