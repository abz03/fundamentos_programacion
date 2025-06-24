# ======================================
# Sistema de Shows en Vivo - Comentado
# ======================================

# Función que verifica si una contraseña cumple con requisitos mínimos
# Requiere: al menos 9 caracteres, una mayúscula y un símbolo especial permitido

def verificar_passwd(passwd):
    mayus = False  # Variable para saber si hay al menos una mayúscula
    especial = False  # Variable para saber si hay al menos un carácter especial

    for caracter in passwd:  # Recorre cada letra/caracter de la contraseña
        if caracter.isupper():  # Si la letra es mayúscula
            mayus = True
        if caracter in ["*", "-", "!", "_", ",", "."]:  # Si es un carácter especial válido
            especial = True

    # Si alguna de las condiciones no se cumple, muestra mensajes y retorna False
    if not mayus or not especial or len(passwd) < 9:
        print("La contraseña debe contener al menos 9 caracteres")
        print("La contraseña debe contener al menos 1 mayúscula")
        print("La contraseña debe contener al menos 1 caracter especial de la lista: ", ["*", "-", "!", "_", ",", "."])
        return False
    else: 
        return True  # Si todo se cumple, devuelve True

# Muestra todos los artistas que tienen shows en un país específico

def artistas_por_pais(pais):
    shows_en_pais = []  # Lista vacía para guardar shows encontrados
    for key in shows:  # Recorre cada show
        if shows[key][1].lower() == pais.lower():  # Compara país ignorando mayúsculas
            shows_en_pais.append({"artista": shows[key][0], "fecha": shows[key][2]})

    if len(shows_en_pais) == 0:  # Si no se encontró ningún show
        print("No hay show en este país")
    else:
        print("Los shows en este país son: ")
        for i in shows_en_pais:
            print(i["artista"], i["fecha"])  # Muestra artista y fecha

# Calcula y muestra el porcentaje de shows que se realizan en un mes dado

def shows_por_mes(mes):
    cant_shows = 0  # Contador de shows en el mes
    for key in shows:  # Recorre cada show
        fecha = shows[key][2].split("-")  # Separa la fecha por "-" (día-mes-año)
        try:
            if int(fecha[1]) == mes:  # Compara el número de mes con el solicitado
                cant_shows += 1
        except ValueError as error:
            print("Error:", error)
            return
    print("El porcentaje de shows en ese mes es de: ", round((cant_shows * 100) / len(shows), 1))

# Diccionario con los usuarios y sus contraseñas
usuarios = {
    "admin": "Admin*2025"
}

# Diccionario con los shows. Cada show tiene un código, nombre de artista, país y fecha
shows = {
    "A001": ["Taylor Swift", "Estados Unidos", "15-09-2025"],
    "A002": ["Bad Bunny", "Puerto Rico", "03-08-2025"],
    "A003": ["Rosalía", "España", "21-10-2025"],
    "A004": ["BLACKPINK", "Corea del Sur", "05-07-2025"],
    "A005": ["Dua Lipa", "Reino Unido", "18-08-2025"],
    "A006": ["BTS", "Corea del Sur", "12-09-2025"],
    "A007": ["Shakira", "Colombia", "25-11-2025"],
    "A008": ["Karol G", "Colombia", "02-12-2025"],
    "A009": ["The Weeknd", "Canadá", "30-06-2025"],
    "A010": ["BTS", "Corea del Sur", "01-03-2025"],
    "A011": ["Taylor Swift", "Estados Unidos", "22-05-2025"],
    "A012": ["Rosalía", "España", "14-12-2025"],
    "A013": ["Dua Lipa", "Reino Unido", "09-11-2025"],
    "A014": ["BLACKPINK", "Corea del Sur", "20-04-2025"],
    "A015": ["Karol G", "Colombia", "10-07-2025"],
    "A016": ["Bad Bunny", "Puerto Rico", "27-09-2025"],
    "A017": ["Shakira", "Colombia", "03-06-2025"],
    "A018": ["The Weeknd", "Canadá", "17-10-2025"],
    "A019": ["Taylor Swift", "Estados Unidos", "06-01-2025"]
}

login = False  # Bandera que indica si el usuario inició sesión correctamente

# Bienvenida al sistema
print("#" * 41)
print("#Bienvenidos al sistema de shows en vivo#")
print("#" * 41)

# Bucle principal para ingresar o registrarse
while True:
    # Menú de inicio de sesión
    print('''
    1. Iniciar sesión
    2. Registrar nuevo usuario
    3. Salir
    ''')
    try:
        opcion = 0
        opcion = int(input())  # Se intenta convertir la entrada a número entero
    except ValueError as error:
        print("Ingrese un valor válido")
        print("Error: ", error)

    if opcion == 3:  # Salir del sistema
        print("Gracias por usar el sistema de shows en vivo")
        break

    if opcion == 1:  # Iniciar sesión
        user = input("Ingrese su nombre de usuario: ")
        passwd = input("Ingrese su contraseña: ")

        if user in usuarios:  # Verifica si el usuario existe
            if passwd == usuarios[user]:  # Verifica si la contraseña es correcta
                print("Usuario ingresado exitosamente!")
                login = True
                break
            else:
                print("Credenciales incorrectas!")
        else:
            print("Credenciales incorrectas!")

    if opcion == 2:  # Registro de nuevo usuario
        user = input("Ingrese el nombre de usuario: ")
        if user in usuarios:
            print("Este usuario no está disponible!")
        else:
            passwd = input("Ingrese la contraseña: ")
            if verificar_passwd(passwd):  # Valida la contraseña
                usuarios[user] = passwd  # Agrega nuevo usuario
                print("Usuario registrado correctamente!")
            else:
                print("No se pudo registrar el usuario")

# Menú principal del sistema (solo si se inició sesión correctamente)
while True and login:
    print('''
    *** SISTEMA DE SHOWS EN VIVO ***

    1. Mostrar artistas por país
    2. Porcentaje de shows en un mes
    3. Eliminar artista por nombre
    4. Salir

    ''')
    try:
        opcion = 0
        opcion = int(input())
        if not (1 <= opcion <= 4):
            print("Opción inválida")
    except ValueError as error:
        print("Valor inválido")
        print("Error: ", error)

    if opcion == 4:  # Salir del menú
        print("Gracias por usar el sistema de shows en vivo")
        break

    if opcion == 1:
        pais = input("Ingrese el nombre de un país: ")
        artistas_por_pais(pais)  # Llama a la función para mostrar artistas

    if opcion == 2:
        try:
            mes = int(input("Ingrese el mes a analizar: "))
            if 1 <= mes <= 12:
                shows_por_mes(mes)  # Llama a la función para mostrar porcentaje
            else:
                print("Tiene que elegir un valor entre 1 y 12 inclusive.")
        except ValueError as error:
            print("Valor inválido")
            print("Error: ", error)

    if opcion == 3:
        nombre_artista = input("Ingrese el nombre del artista que desea eliminar: ")
        encontrados = []  # Lista para guardar claves de shows que coincidan

        for clave, datos in list(shows.items()):  # Recorremos copia de items del diccionario
            if datos[0].lower() == nombre_artista.lower():  # Compara sin distinguir mayúsculas
                encontrados.append(clave)  # Guardamos la clave (ID del show)

        if not encontrados:
            print("No se encontró ningún show con ese nombre de artista.")
        else:
            for clave in encontrados:
                del shows[clave]  # Eliminamos el show del diccionario
            print(f"Se eliminaron {len(encontrados)} show(s) de {nombre_artista} exitosamente.")
