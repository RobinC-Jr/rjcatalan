print("¿Hola?")
Respuesta = input("1: ¡Hola!   2: Chao.")
while Respuesta != "1" and Respuesta != "2":
    Respuesta = input("Nono. 1: ¡Hola!   2: Chao.")
else:
    if Respuesta == "1":
        print("¡Hola mundo!")
    elif Respuesta == "2":
        print("Chao mundo...")