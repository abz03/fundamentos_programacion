'''
Programa: Sistema de bibliotecas.
Utilizar la lista de usuarios y personas definidas a continuación.
El programa debe mostrar un menú que permita:
1 - Buscar un usuario por su rut.
    1.1 - Si el usuario existe mostrar un menú para:
        1.1.1 - Realizar un préstamo de un libro, sólo si hay disponibles.
        1.1.2 - Realizar la devolución de un libro
            1.1.2.1 - Si el libro no existe, permitir registrar el libro que trajo la persona.
    1.2  - Si el usuario no existe, permitir registrar al usuario.
2 - Registrar un nuevo usuario.
3 - Registrar un nuevo libro.
4 - Salir

Debe hacer una función para:
1 - Buscar usuarios
2 - Registrar un usuario
3 - Registrar un libro

Debe usar try-except para verificar todos los posibles códigos peligrosos.
Debe usar mensajes amigables y coherentes con un programa pensado para el encargado de la 
biblioteca. Bien escritos y redactados, puede ayudarse de Chat GPT para esto.
'''

usuarios = [
    {"nombre": "Ana", "apellido": "González", "rut": "13816108-7", "libros": []},
    {"nombre": "Luis", "apellido": "Rodríguez", "rut": "13872719-2", "libros": []},
    {"nombre": "Camila", "apellido": "Pérez", "rut": "12182343-5", "libros": []},
    {"nombre": "Jorge", "apellido": "Muñoz", "rut": "14044461-9", "libros": []},
    {"nombre": "María", "apellido": "Rojas", "rut": "16149391-0", "libros": []},
    {"nombre": "Diego", "apellido": "Díaz", "rut": "10407062-4", "libros": [0]},
    {"nombre": "Lucía", "apellido": "Soto", "rut": "19306158-3", "libros": []},
    {"nombre": "Pablo", "apellido": "Torres", "rut": "14864522-5", "libros": []},
    {"nombre": "Valentina", "apellido": "Contreras", "rut": "15592214-1", "libros": []},
    {"nombre": "Tomás", "apellido": "Silva", "rut": "10516040-5", "libros": []}
]

libros = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "ISBN": "978-0307474728", "paginas": 432, "cantidad_disponible": 5},
    {"id": 2, "titulo": "1984", "autor": "George Orwell", "ISBN": "978-0451524935", "paginas": 328, "cantidad_disponible": 3},
    {"id": 3, "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "ISBN": "978-1451673319", "paginas": 194, "cantidad_disponible": 7},
    {"id": 4, "titulo": "Don Quijote", "autor": "Miguel de Cervantes", "ISBN": "978-0060934347", "paginas": 992, "cantidad_disponible": 2},
    {"id": 5, "titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "ISBN": "978-1400034956", "paginas": 128, "cantidad_disponible": 4},
    {"id": 6, "titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "ISBN": "978-0156013987", "paginas": 96, "cantidad_disponible": 10},
    {"id": 7, "titulo": "Ensayo sobre la ceguera", "autor": "José Saramago", "ISBN": "978-0156007757", "paginas": 352, "cantidad_disponible": 3},
    {"id": 8, "titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "ISBN": "978-0143034902", "paginas": 512, "cantidad_disponible": 6},
    {"id": 9, "titulo": "El túnel", "autor": "Ernesto Sabato", "ISBN": "978-9500420305", "paginas": 160, "cantidad_disponible": 2},
    {"id": 10, "titulo": "Pedro Páramo", "autor": "Juan Rulfo", "ISBN": "978-6073142360", "paginas": 144, "cantidad_disponible": 8}
]


# ----------------------------
# Función: buscar usuario por RUT
# ----------------------------
# Esta función recibe un RUT como texto y busca en la lista de usuarios si existe uno con ese RUT
# Si lo encuentra, devuelve el diccionario con la información del usuario
# Si no lo encuentra, devuelve None

def buscar_usuario(rut):
    for usuario in usuarios:
        if usuario["rut"] == rut:
            return usuario
    return None

# ----------------------------
# Función: registrar un nuevo usuario
# ----------------------------
# Pide al encargado de la biblioteca que escriba los datos del nuevo usuario por consola
# Valida que el RUT no esté repetido antes de agregarlo

def registrar_usuario():
    try:
        print("\n--- Registro de nuevo usuario ---")
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        rut = input("Ingrese el RUT: ")

        if buscar_usuario(rut):
            print("El RUT ingresado ya está registrado en el sistema.")
            return

        nuevo_usuario = {"nombre": nombre, "apellido": apellido, "rut": rut, "libros": []}
        usuarios.append(nuevo_usuario)
        print("Usuario registrado exitosamente.")
    except Exception as e:
        print("Ocurrió un error al registrar al usuario:", e)

# ----------------------------
# Función: registrar un nuevo libro
# ----------------------------
# Pide los datos de un libro y lo agrega a la lista
# El ID se genera automáticamente sumando 1 al último ID registrado

def registrar_libro():
    try:
        print("\n--- Registro de nuevo libro ---")
        titulo = input("Título del libro: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        paginas = int(input("Cantidad de páginas: "))  # Convertimos a número entero
        cantidad = int(input("Cantidad disponible: "))  # Convertimos a número entero

        nuevo_id = libros[-1]["id"] + 1  # Esta línea genera un nuevo ID para un libro, sumando 1 al ID del último libro en la lista
        nuevo_libro = {"id": nuevo_id, "titulo": titulo, "autor": autor, "ISBN": isbn, "paginas": paginas, "cantidad_disponible": cantidad}
        libros.append(nuevo_libro)
        print("Libro registrado exitosamente.")
    except Exception as e:
        print("Error al registrar libro:", e)

# ----------------------------
# Función: prestar libro a un usuario
# ----------------------------
# Muestra la lista de libros disponibles y permite al encargado elegir uno por su ID
# Si el libro está disponible (cantidad > 0), se le asigna al usuario

def prestar_libro(usuario):
    try:
        print("\n--- Libros disponibles ---")
        for libro in libros:
            print(f"{libro['id']} - {libro['titulo']} ({libro['cantidad_disponible']} disponibles)")

        id_libro = int(input("Ingrese el ID del libro que desea prestar: "))
        libro = next((l for l in libros if l["id"] == id_libro), None)# Esta línea busca un libro específico dentro de la lista libros, comparando su "id" con el valor id_libro.
        # Si lo encuentra, lo guarda en la variable libro.
        # Si o lo encuentra, devuelve None (vacío).

        if libro and libro["cantidad_disponible"] > 0:
            usuario["libros"].append(id_libro)  # Agrega el ID del libro a la lista del usuario
            libro["cantidad_disponible"] -= 1  # Resta uno a la cantidad disponible
            print("El libro ha sido prestado exitosamente.")
        else:
            print("No hay ejemplares disponibles o el ID ingresado no existe.")
    except Exception as e:
        print("Error al prestar el libro:", e)

# ----------------------------
# Función: devolver libro
# ----------------------------
# Muestra los libros que el usuario tiene prestados y permite seleccionar uno para devolverlo
# Si el libro no está registrado en la lista de libros, se da la opción de registrarlo

def devolver_libro(usuario):
    try:
        if not usuario["libros"]:
            print("El usuario no tiene libros para devolver.")
            return

        print("\n--- Libros prestados ---")
        for i, id_libro in enumerate(usuario["libros"]):
            libro = next((l for l in libros if l["id"] == id_libro), None)
            if libro:
                print(f"{i+1}. {libro['titulo']}")

        seleccion = int(input("Ingrese el número del libro que desea devolver: ")) - 1
        id_devuelto = usuario["libros"].pop(seleccion)
        libro = next((l for l in libros if l["id"] == id_devuelto), None)

        if libro:
            libro["cantidad_disponible"] += 1
            print("Libro devuelto correctamente.")
        else:
            print("Libro no encontrado. Registrando nuevo libro...")
            registrar_libro()
    except Exception as e:
        print("Error al devolver el libro:", e)

# ----------------------------
# Función principal: Menú del sistema
# ----------------------------
# Muestra el menú principal del sistema y permite elegir qué acción realizar
# Esta función se repite en un ciclo hasta que el usuario decida salir

def menu():
    while True:
        print("\n=== MENÚ DEL SISTEMA DE BIBLIOTECA ===")
        print("1. Buscar usuario por RUT")
        print("2. Registrar nuevo usuario")
        print("3. Registrar nuevo libro")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            rut = input("Ingrese el RUT del usuario: ")
            usuario = buscar_usuario(rut)

            if usuario:
                print(f"Bienvenido/a {usuario['nombre']} {usuario['apellido']}")
                print("1. Realizar préstamo")
                print("2. Devolver libro")
                sub_opcion = input("Seleccione una opción: ")

                if sub_opcion == "1":
                    prestar_libro(usuario)
                elif sub_opcion == "2":
                    devolver_libro(usuario)
                else:
                    print("Opción no válida.")
            else:
                print("Usuario no encontrado.")
                if input("¿Desea registrarlo? (s/n): ").lower() == "s":
                    registrar_usuario()

        elif opcion == "2":
            registrar_usuario()

        elif opcion == "3":
            registrar_libro()

        elif opcion == "4":
            print("Gracias por utilizar el sistema. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida. Por favor, elija una opción del 1 al 4.")

# ----------------------------
# Iniciar el sistema ejecutando el menú principal
# ----------------------------
menu()
