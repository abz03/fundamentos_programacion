# Diccionario con los datos de los turistas, donde la clave es un ID y el valor es una lista con [nombre, país, fecha]
turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

# Función que muestra los turistas de un país dado
def turistas_por_pais(pais):
    lista_turistas = []  # Lista para almacenar los nombres de los turistas encontrados
    for turista in turistas:  # Recorre cada clave (ID) del diccionario 'turistas'
        # Compara el país ingresado (en minúsculas) con el país del turista (también en minúsculas)
        if pais.lower() == turistas[turista][1].lower():
            print("Los turistas de ese país son:", turistas[turista][0])  # Imprime el nombre si coincide
            lista_turistas.append(turistas[turista][0])  # Agrega el nombre a la lista
    if len(lista_turistas) == 0:  # Si la lista está vacía, significa que no se encontró ningún turista del país
        print("No hay turistas de ese pais.")
    return  # Termina la función

# Función que muestra y calcula el porcentaje de turistas que llegaron en un mes específico
def turistas_por_mes(mes):
    lista_turistas_mes = []  # Lista para almacenar los turistas encontrados en el mes buscado
    cantidad_turistas = 0    # Contador de turistas del mes
    total_turistas = 0       # Contador total de turistas
    for turista in turistas:  # Recorre cada turista en el diccionario
        total_turistas += 1  # Suma 1 al total de turistas
        fecha = turistas[turista][2]  # Obtiene la fecha de ingreso del turista
        fecha_en_partes = fecha.split("-")  # Divide la fecha en día, mes, año (ej: "12-01-2024" → ["12", "01", "2024"])
        # Compara el mes dado con el mes del turista (convertido a int)
        if mes == int(fecha_en_partes[1]):
            cantidad_turistas += 1  # Suma 1 al contador de turistas de ese mes
            print("Los turistas de ese mes son:", turistas[turista][0])  # Muestra el nombre del turista
            lista_turistas_mes.append(turistas[turista][0])  # Agrega el nombre a la lista
    if len(lista_turistas_mes) == 0:  # Si no se encontró ningún turista en ese mes
        print("No hay turistas en ese mes.")
    else:
        print("Total de turistas: ", total_turistas)  # Muestra el total de turistas
        print("Total de turistas de ese mes son :", cantidad_turistas)  # Muestra cuántos son del mes buscado
        porcentaje_turistas = (cantidad_turistas * 100) / total_turistas  # Calcula el porcentaje
        print(f"El número de turistas equivale al {porcentaje_turistas}%  del total.")  # Muestra el porcentaje
    return  # Termina la función

# Función que elimina a un turista por su nombre (sin importar mayúsculas/minúsculas)
def eliminar_turista(nombre):
    nombre_bool = False  # Variable bandera para saber si se encontró el turista
    for turista in turistas:  # Recorre todos los turistas
        # Compara el nombre ingresado con el nombre del turista, ignorando mayúsculas/minúsculas
        if nombre.lower() == turistas[turista][0].lower():
            nombre_bool = True  # Marca como encontrado
            break  # Importante: salir del ciclo si ya se encontró
    if nombre_bool:  # Si el turista fue encontrado
        del turistas[turista]  # Elimina la entrada del turista del diccionario (por su clave/ID)
        print("Turista eliminado con exito")
    else:
        print("Turista no encontrado. No se pudo eliminar.")
    return  # Termina la función

# Función que agrega un nuevo turista si su nombre no está duplicado
def agregar_turista(nombre_agregar, pais_agregar, fecha_agregar):
    nuevo_id = 0  # Variable para calcular el nuevo ID del turista
    datos_nuevo_turista = []  # Lista donde se guardarán los datos del nuevo turista
    nombre_bool = False  # Bandera para verificar duplicidad
    for turista in turistas:  # Recorre todos los turistas existentes
        nuevo_id += 1  # Cuenta para generar un nuevo ID único
        if nombre_agregar.lower() == turistas[turista][0].lower():
            nombre_bool = True  # Marca que el nombre ya existe
    if nombre_bool:  # Si el nombre ya existe, no agrega el turista
        print("Turista encontrado. No se pudo agregar, no se permiten duplicados.")
    else:
        datos_nuevo_turista.append(nombre_agregar)  # Agrega el nombre a la lista de datos
        datos_nuevo_turista.append(pais_agregar)    # Agrega el país
        datos_nuevo_turista.append(fecha_agregar)   # Agrega la fecha
        turistas[str(nuevo_id+1)] = datos_nuevo_turista  # Agrega el nuevo turista al diccionario con ID único
        print("Turista agregado con exito")
    return  # Termina la función

# A partir de aquí puede seguir el menú principal usando while True, input y llamadas a estas funciones.

while True:  # Ciclo infinito para que el menú se repita hasta que el usuario decida salir
    print('''
    *** MENU PRINCIPAL ***
    1.- Turistas por país.
    2.- Turista por mes.
    3.- Eliminar turista.
    4.- Agregar un turista
    5.- Salir
          ''')  # Muestra el menú de opciones al usuario

    try:
        opcion = int(input("Ingrese una opción: "))  # Solicita al usuario que ingrese una opción (espera un número)
    except ValueError:
        opcion = 0  # Si el usuario ingresa algo que no es número, asigna 0 para activar la opción inválida

    # Opción 1: Buscar turistas por país
    if opcion == 1:
        try:
            pais = str(input("Ingrese pais a buscar: "))  # Solicita al usuario el nombre del país
            turistas_por_pais(pais)  # Llama a la función para mostrar turistas del país ingresado
        except:
            print("Ocurrio un error intentando obtener los datos, intente nuevamente")  # Si ocurre un error, muestra un mensaje

    # Opción 2: Buscar turistas por mes de ingreso
    elif opcion == 2:
        try:
            mes = int(input("Ingrese mes a buscar: "))  # Pide al usuario el número de mes (1 al 12)
            turistas_por_mes(mes)  # Llama a la función para mostrar turistas y porcentaje del mes indicado
        except ValueError:
            print("Ingrese un valor numerico por favor (Ej:01,02,03).")  # Si no se ingresa un número, muestra un mensaje

    # Opción 3: Eliminar un turista por nombre
    elif opcion == 3:
        try:
            nombre = str(input("Ingrese el nombre del turista a eliminar:"))  # Pide el nombre del turista a eliminar
            eliminar_turista(nombre)  # Llama a la función que elimina el turista
        except:
            print("Ocurrio un error intentando obtener los datos, intente nuevamente")  # Si ocurre error, muestra mensaje

    # Opción 4: Agregar un nuevo turista
    elif opcion == 4:
        try:
            nombre_agregar = str(input("Ingrese el nombre del turista a agregar: "))  # Pide nombre del turista nuevo
            pais_agregar = str(input("Ingrese el país del turista a agregar: "))      # Pide país de origen
            fecha_agregar = str(input("Ingrese la fecha del turista a agregar: (formato: dia-mes-año) "))  # Pide fecha

            agregar_turista(nombre_agregar, pais_agregar, fecha_agregar)  # Llama a la función para agregar al turista
        except:
            print("Ocurrio un error intentando obtener los datos, intente nuevamente")  # Si ocurre error, muestra mensaje

    # Opción 5: Salir del programa
    elif opcion == 5:
        print("Programa terminado...")  # Mensaje de despedida
        break  # Sale del ciclo while y termina el programa

    # Si la opción no es válida (no está entre 1 y 5)
    else:
        print("Debe ingresar una opción válida!!")  # Informa al usuario que debe ingresar una opción válida