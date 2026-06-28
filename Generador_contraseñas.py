# Generador Seguro de Contraseñas
respuesta = "si"
while respuesta == "si":
    Usuario = input("Ingrese su nombre: ")
    N_caracteres = int(input("Ingrese el numero de caracteres: "))
    Letras = input("Desea incluir letras? (si/no): ")
    Numeros = input("Desea incluir numeros? (si/no): ")
    Simbolos = input("Desea incluir simbolos? (si/no): ")
    contrasena = ""
    if Letras == "si":
        contrasena = contrasena + "ABCDEFGHIJ"
    if Numeros == "si":
        contrasena = contrasena + "12345"
    if Simbolos == "si":
        contrasena = contrasena + "@#/"
    if Letras == "si" and Numeros == "si" and Simbolos == "si":
        print("Nivel de seguridad: Muy segura")
    elif Letras == "si" and Numeros == "si":
        print("Nivel de seguridad: Segura")
    elif Letras == "si":
        print("Nivel de seguridad: Basica")
    else:
        print("No se puede generar una contraseña porque no seleccionó suficientes elementos")

    print("Usuario:", Usuario)
    print("Numero de caracteres solicitado:", N_caracteres)
    print("Contraseña generada:", contrasena)

    respuesta = input("Desea generar otra contraseña? (si/no): ")

print("Programa finalizado")