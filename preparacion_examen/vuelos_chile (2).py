
# Estructura de datos para almacenar información de las compras
'''
pasajes_comprados = {
    "SAPA": {
        },
    "ARCO": {
        "3A": ["carlos torres", "45678901-2"],
        "3B": ["laura martinez", "56789012-3"],
        "3C": ["jose ramirez", "67890123-4"],
        "3J": ["paula gonzalez", "78901234-5"],
    }
}

# Para saber qué pasajero está en un asiento específico de un vuelo, accedemos a el de la siguiente manera:
pasajero = pasajes_comprados["SAPA"]["3A"]
print(pasajero)
print(pasajes_comprados)
del (pasajes_comprados["SAPA"]["3A"])  # Para eliminar un pasajero de un asiento específico
print(pasajes_comprados)
pasajes_comprados["SAPA"]["3B"] = ["jose maria lopez", "12345678-9"]  # Para agregar un pasajero a un asiento específico
pasajes_comprados["COTO"] = {} # Agregar un vuelo nuevo
print(pasajes_comprados)
pasajes_comprados["COTO"]["3A"] = ["maria lopez", "12345678-9"]  # Agregar un pasajero a un asiento específico en otro vuelo
print(pasajes_comprados)
'''

from random import randint

pasajes_comprados = {}

vuelos_chile = {
    "SAPA": ["Santiago", "Punta Arenas", "2025-07-10", "08:30", "Puerta 1"],
    "ARCO": ["Arica", "Concepción", "2025-07-11", "14:45", "Puerta 2"],
    "COTO": ["Copiapo", "Tocopilla", "2025-07-12", "10:20", "Puerta 3"],
    "ANTI": ["Antofagasta", "Iquique", "2025-07-13", "07:15", "Puerta 4"],
    "VAOS": ["Valdivia", "Osorno", "2025-07-14", "09:50", "Puerta 5"],
    "SELA": ["Serena", "La Serena", "2025-07-15", "13:00", "Puerta 6"],
    "RIAN": ["Rancagua", "Antofagasta", "2025-07-16", "17:25", "Puerta 7"],
    "TEAR": ["Temuco", "Arica", "2025-07-17", "12:10", "Puerta 8"],
    "CHIQ": ["Chillán", "Quellón", "2025-07-18", "11:30", "Puerta 9"],
    "PACO": ["Puerto Aysén", "Coyhaique", "2025-07-19", "15:40", "Puerta 10"],
    "PUAN": ["Puerto Aysén", "Antofagasta", "2025-07-30", "09:15", "Puerta 11"],
    "SEPU": ["Serena", "Puerto Aysén", "2025-07-31", "07:30", "Puerta 12"],
    "VIAR": ["Viña del Mar", "Arica", "2025-08-01", "10:45", "Puerta 13"],
    "COTE": ["Copiapo", "Temuco", "2025-08-02", "06:50", "Puerta 14"],
    "AROS": ["Arica", "Osorno", "2025-08-03", "14:10", "Puerta 15"],
    "PUVI": ["Puerto Aysén", "Villarrica", "2025-08-04", "16:20", "Puerta 1"],
    "RITE": ["Rancagua", "Temuco", "2025-08-05", "11:35", "Puerta 2"],
    "CHCO": ["Chillán", "Coquimbo", "2025-08-06", "12:45", "Puerta 3"],
    "COAR": ["Coquimbo", "Arica", "2025-08-07", "13:55", "Puerta 4"],
    "TEPU": ["Temuco", "Puerto Aysén", "2025-08-08", "15:10", "Puerta 5"],
    "VAQU": ["Valdivia", "Quellón", "2025-08-09", "17:00", "Puerta 6"],
    "QUSE": ["Quellón", "Serena", "2025-08-10", "08:10", "Puerta 7"],
    "SERO": ["Serena", "Rancagua", "2025-08-11", "09:45", "Puerta 8"],
    "VIAN": ["Viña del Mar", "Antofagasta", "2025-08-12", "11:20", "Puerta 9"],
    "SERI": ["Santiago", "Rancagua", "2025-08-13", "06:30", "Puerta 10"],
    "IQPU": ["Iquique", "Puerto Aysén", "2025-08-14", "13:25", "Puerta 11"],
    "ANOS": ["Antofagasta", "Osorno", "2025-08-15", "10:00", "Puerta 12"],
    "QUCO": ["Quellón", "Concepción", "2025-08-16", "16:40", "Puerta 13"],
    "VALA": ["Valparaíso", "La Serena", "2025-08-17", "12:00", "Puerta 14"],
    "PUVA": ["Puerto Aysén", "Valparaíso", "2025-08-18", "14:20", "Puerta 15"]
}

info_vuelos = {
    "SAPA": [75000, 45, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B', '7C', '7D', '7E', '7F', '7J', '7K', '7L', '8A', '8B', '8C']],
    "ARCO": [68000, 30, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F']],
    "COTO": [72000, 20, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E']],
    "ANTI": [59000, 50, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B', '7C', '7D', '7E', '7F', '7J', '7K', '7L', '8A', '8B', '8C', '8D', '8E', '8F', '8J', '8K']],
    "VAOS": [65000, 25, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A']],
    "SELA": [40000, 60, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B', '7C', '7D', '7E', '7F', '7J', '7K', '7L', '8A', '8B', '8C', '8D', '8E', '8F', '8J', '8K', '8L', '9A', '9B', '9C', '9D', '9E', '9F', '9J', '9K', '9L']],
    "RIAN": [88000, 15, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L']],
    "TEAR": [91000, 35, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B']],
    "CHIQ": [56000, 40, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B', '7C', '7D', '7E', '7F', '7J']],
    "PACO": [97000, 10, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D']],
    "PUAN": [89000, 22, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J']],
    "SEPU": [67000, 27, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C']],
    "VIAR": [84000, 18, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C']],
    "COTE": [71000, 33, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L']],
    "AROS": [76000, 19, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D']],
    "PUVI": [88000, 24, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L']],
    "RITE": [73000, 28, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D']],
    "CHCO": [61000, 31, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J']],
    "COAR": [86000, 16, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A']],
    "TEPU": [93000, 13, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J']],
    "VAQU": [78000, 21, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F']],
    "QUSE": [65000, 36, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B', '7C']],
    "SERO": [69000, 29, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E']],
    "VIAN": [92000, 12, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F']],
    "SERI": [54000, 48, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B', '7C', '7D', '7E', '7F', '7J', '7K', '7L', '8A', '8B', '8C', '8D', '8E', '8F']],
    "IQPU": [96000, 11, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E']],
    "ANOS": [88000, 26, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B']],
    "QUCO": [67000, 23, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K']],
    "VALA": [60000, 38, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B', '7C', '7D', '7E']],
    "PUVA": [94000, 14, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K']],
}

def ver_vuelos_disponibles(tipo_busqueda = 0, ciudad = ""):
    encontrado = False
    if tipo_busqueda not in [0, 1]:
        print("Tipo de búsqueda no válido. Use 0 para origen, 1 para destino.")
        return
    for vuelo in vuelos_chile:
        if vuelos_chile[vuelo][tipo_busqueda].lower() == ciudad.lower():
            encontrado = True
            print(f"Vuelo: {vuelo}, Origen: {vuelos_chile[vuelo][0]}, Destino: {vuelos_chile[vuelo][1]}, Fecha: {vuelos_chile[vuelo][2]}, Hora: {vuelos_chile[vuelo][3]}, Puerta: {vuelos_chile[vuelo][4]}")
            print(f"Precio: {info_vuelos[vuelo][0]}, Asientos disponibles: {info_vuelos[vuelo][1]}")
    if not encontrado:
        if tipo_busqueda == 0:
            print("No se encontraron vuelos con ese origen.")
        elif tipo_busqueda == 1:
            print("No se encontraron vuelos con ese destino.")
        else:
            print("Tipo de búsqueda no válido.")

def ver_vuelos_origen_destino(origen, destino):
    encontrado = False
    for vuelo in vuelos_chile:
        if vuelos_chile[vuelo][0].lower() == origen.lower() and vuelos_chile[vuelo][1].lower() == destino.lower():
            encontrado = True
            print(f"Vuelo: {vuelo}, Origen: {vuelos_chile[vuelo][0]}, Destino: {vuelos_chile[vuelo][1]}, Fecha: {vuelos_chile[vuelo][2]}, Hora: {vuelos_chile[vuelo][3]}, Puerta: {vuelos_chile[vuelo][4]}")
            print(f"Precio: {info_vuelos[vuelo][0]}, Asientos disponibles: {info_vuelos[vuelo][1]}")
    if not encontrado:
        print("No se encontraron vuelos con ese origen y destino.")

def ver_asientos_disponibles():
    vuelo = input("Ingrese el código del vuelo: ")
    if vuelo not in info_vuelos:
        print("Vuelo no encontrado.")
        return # Si la clave vuelo no está en el diccionario info_vuelos, se sale de la función.

    print(f"La cantidad de asientos disponibles para el vuelo con origen {vuelos_chile[vuelo][0]} y destino {vuelos_chile[vuelo][1]} es :", info_vuelos[vuelo][1])

def comprar_pasaje(vuelo):
    
    if vuelo not in info_vuelos:
        print("Vuelo no encontrado.")
        return

    asientos_disponibles = info_vuelos[vuelo][2]
    if len(asientos_disponibles) == 0:
        print("No hay asientos disponibles para este vuelo.")
        return

    print(f"El precio del pasaje para el vuelo {vuelo} es: {info_vuelos[vuelo][0]}")
    print("Asientos disponibles:", info_vuelos[vuelo][1])

    nombre_pasajero = input("Ingrese su nombre completo: ")
    rut_pasajero = input("Ingrese su RUT (sin puntos ni guion): ")
    
    if vuelo not in pasajes_comprados:
        pasajes_comprados[vuelo] = {}
        
    for pasajero in pasajes_comprados[vuelo]:
        if rut_pasajero == pasajes_comprados[vuelo][pasajero][1]:
            print("Ya existe un pasaje comprado con ese RUT.")
            return
    
    asiento_seleccionado = info_vuelos[vuelo][2].pop(randint(0, len(info_vuelos[vuelo][2]) - 1))  # Selecciona un asiento aleatorio de los disponibles
    info_vuelos[vuelo][1] -= 1  # Reduce la cantidad de asientos disponibles
    
    # Guardo la información del pasaje comprado en el diccionario pasajes_comprados

    pasajes_comprados[vuelo][asiento_seleccionado] = [nombre_pasajero, rut_pasajero]
    
    print(f"Pasaje comprado exitosamente para {nombre_pasajero} en el vuelo {vuelo} con origen {vuelos_chile[vuelo][0]}, destino {vuelos_chile[vuelo][1]}, asiento {asiento_seleccionado}.")

def ver_pasajes_comprados(vuelo):
    if vuelo not in pasajes_comprados or len(pasajes_comprados[vuelo]) == 0:
        print("No hay pasajes comprados para este vuelo.")
        return

    print(f"Pasajes comprados para el vuelo {vuelo} (Origen: {vuelos_chile[vuelo][0]}, Destino: {vuelos_chile[vuelo][1]}):")
    for asiento in pasajes_comprados[vuelo]:
        info = pasajes_comprados[vuelo][asiento]
        print(f"Asiento: {asiento}, Pasajero: {info[0]}, RUT: {info[1]}")
     
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++   Bienvenido a la aerolínea Vuelos Chile   ++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

while True:
    print("\n++++++++++++++++   Menú principal   +++++++++++++++++++++++")
    print("1. Ver vuelos disponibles ")
    print("2. Ver asientos disponibles")
    print("3. Comprar pasaje")
    print("4. Ver pasajes comprados")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1-5): ")
    
    if opcion == "5":
        print("Gracias por usar Vuelos Chile. ¡Hasta luego!")
        break
    
    elif opcion == "1":
        print("\n++++++++++++++   Vuelos disponibles   +++++++++++++++++++++")
        while True:
            print("Seleccione una opción de filtro:")
            print("1. Ver todos los vuelos")
            print("2. Ver vuelos por origen")
            print("3. Ver vuelos por destino")
            print("4. Ver vuelos por origen - destino")
            print("5. Volver al menú principal")
            
            filtro = input("Seleccione una opción (1-5): ")
            
            if filtro == "5":
                break
            elif filtro == "1":
                print("Lista de vuelos disponibles:")
                for vuelo in vuelos_chile: # El iterador toma los valores de las claves del diccionario vuelos_chile
                    # Se realiza una asignación múltiple para obtener los valores de cada vuelo.
                    origen, destino, fecha, hora, puerta = vuelos_chile[vuelo] # Se accede a los valores del vuelo usando la clave, el valor es una lista.
                    ''' FORMA LARGA DE ASIGNACION:
                    origen = vuelos_chile[vuelo][0]
                    destino = vuelos_chile[vuelo][1]
                    fecha = vuelos_chile[vuelo][2]
                    hora = vuelos_chile[vuelo][3]
                    puerta = vuelos_chile[vuelo][4]
                    '''
                    print(f"Vuelo: {vuelo}, Origen: {origen}, Destino: {destino}, Fecha: {fecha}, Hora: {hora}, Puerta: {puerta}")
            elif filtro == "2":
                print("Ingrese el origen del vuelo:")
                origen = input("Origen: ")
                ver_vuelos_disponibles(0,origen)
            elif filtro == "3":
                print("Ingrese el destino del vuelo:")
                destino = input("Destino: ")
                ver_vuelos_disponibles(1,destino)
            elif filtro == "4":
                print("Ingrese el origen y destino del vuelo (formato: origen-destino):")
                origen = input("Origen: ")
                destino = input("Destino: ")
                ver_vuelos_origen_destino(origen, destino)
            else:
                print("Opción no válida. Intente nuevamente.")
    elif opcion == "2":
        print("\n++++++++++++++   Asientos disponibles   ++++++++++++++++++")
        ver_asientos_disponibles()
    elif opcion == "3":
        print("\n++++++++++++++   Comprar pasaje   +++++++++++++++++++++++++")
        vuelo = input("Ingrese el código del vuelo: ")
        comprar_pasaje(vuelo)
    elif opcion == "4":
        print("\n++++++++++++++   Pasajes comprados   ++++++++++++++++++++++")
        vuelo = input("Ingrese el código del vuelo: ")
        ver_pasajes_comprados(vuelo)
