cel = input("Write your city temperature in celcius: ")
far = 0
try:
    celc = float(cel)
    far = (celc * (9/5)) + 32
except:
    print("write a proper number")

print(str(far))
