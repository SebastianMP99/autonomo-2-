# Generador Seguro de Contraseñas
respuesta = "si"
# Lista de letras
letras = ["A", "B", "C", "D", "E", "F"]
# Tupla de números
numeros = ("1", "2", "3", "4", "5", "6")
# Lista de símbolos
simbolos = ["@", "#", "$", "%"]
print("========== GENERADOR SEGURO DE CONTRASEÑAS ==========")
while respuesta == "si":
    usuario = input("Ingrese su nombre: ")
    n_caracteres = int(input("Ingrese el número de caracteres: "))
    usar_letras = input("¿Desea incluir letras? (si/no): ")
    usar_numeros = input("¿Desea incluir números? (si/no): ")
    usar_simbolos = input("¿Desea incluir símbolos? (si/no): ")
    contrasena = ""
    if n_caracteres <= 0:
        print("Debe ingresar un número mayor que cero.")

    else:

        for i in range(n_caracteres):

            if usar_letras == "si":
                contrasena = contrasena + letras[i % 6]

            if usar_numeros == "si":
                contrasena = contrasena + numeros[i % 6]

            if usar_simbolos == "si":
                contrasena = contrasena + simbolos[i % 4]

        if usar_letras != "si" and usar_numeros != "si" and usar_simbolos != "si":
            print("No se puede generar una contraseña porque no seleccionó elementos.")
        else:
            print("\nUsuario:", usuario)
            print("Contraseña generada:", contrasena)
            if n_caracteres >= 10 and usar_letras == "si" and usar_numeros == "si" and usar_simbolos == "si":
                print("Nivel de seguridad: MUY SEGURA")
            elif n_caracteres >= 8 and usar_letras == "si" and usar_numeros == "si":
                print("Nivel de seguridad: SEGURA")
            elif n_caracteres >= 6:
                print("Nivel de seguridad: MEDIA")
            else:
                print("Nivel de seguridad: BÁSICA")
    respuesta = input("\n¿Desea generar otra contraseña? (si/no): ")
print("Programa finalizado")