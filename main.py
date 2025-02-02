temp = ""

def hola():
    global temp
    list=["H", "o", "l", "a"]

    for i in list:
        temp += i

    print(temp)

hola()