import random 
carac = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
a = int(input("Numero de caracteres: "))
b = ""
for i in range(a):
    c = random.choice(carac)
    b += c
print(b)