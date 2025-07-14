# Diccionarios para guardar las entradas de cada concierto
entradas_fortificados = {}   # Guarda entradas de "Los Fortificados", clave: id, valor: [nombre, tipo, código]
entradas_iluminados = {}     # Guarda entradas de "Los Iluminados", clave: id, valor: [nombre, tipo, código]

# Variables para los IDs y stock de entradas
id_fortificados = 1
id_iluminados = 1
total_entrada_los_iluminados = 500
total_entrada_los_fortificados = 500

def comprar_entrada_los_fortificados():
    try:
        global total_entrada_los_fortificados
        global entradas_fortificados
        global id_fortificados

        nombre_comprador = input("Ingrese nombre de comprador: ")

        # CORRECCIÓN: Validar nombre duplicado correctamente
        # Antes, solo se validaba el último elemento, permitiendo duplicados.
        # Ahora, si encuentra el nombre repetido, sale de la función y no registra la compra.
        for entrada in entradas_fortificados.values():
            if entrada[0] == nombre_comprador:
                print("Nombre repetido, ingrese otro")
                return  # Sale de la función si encuentra el nombre repetido

        tipo_entrada = input("Ingrese tipo de entrada (G/V): ")
        tipo_entrada_mayus = tipo_entrada.upper()
        valido_entrada = validar_tipo_entrada_fortificados(tipo_entrada_mayus)
        if valido_entrada:
            while True:
                codigo_confirmacion = input("Ingrese código de confirmación: ")
                valido_codigo = validar_codigo_confirmacion_fortificados(codigo_confirmacion)
                if valido_codigo:
                    print("Código validado.")
                    print("¡Entrada registrada con éxito para “los Fortificados”!")
                    # CORRECCIÓN: Guardar usando el id actual y luego incrementar.
                    # Antes se sobrescribían los datos porque el id no se incrementaba realmente.
                    entradas_fortificados[str(id_fortificados)] = [nombre_comprador, tipo_entrada_mayus, codigo_confirmacion]
                    id_fortificados += 1  # Incrementa el id para la próxima entrada
                    total_entrada_los_fortificados -= 1  # Descuenta stock
                    break
                else:
                    print("Código no válido. Intente otra vez")
        else:
            print("Entrada no válida. Intente otra vez con G o con V")
    except:
        print("Ha ocurrido un error, intente nuevamente")

def validar_codigo_confirmacion_fortificados(codigo_confirmacion):
    # Validaciones: largo, mayúscula, número y sin espacios
    tiene_mayus = False
    tiene_numero = False
    no_tiene_espacio = True

    for i in codigo_confirmacion:
        if i.isupper():
            tiene_mayus = True
        if i.isdigit():
            tiene_numero = True
        if i.isspace():
            no_tiene_espacio = False

    # Devuelve True solo si cumple todas las condiciones
    if len(codigo_confirmacion) >= 6 and tiene_mayus and tiene_numero and no_tiene_espacio:
        return True
    else:
        return False

def validar_tipo_entrada_fortificados(tipo_entrada_mayus):
    # Valida si la entrada es G o V, sin espacios y de largo 1
    tiene_letra = False
    no_tiene_espacio = True

    for i in tipo_entrada_mayus:
        if i == "G" or i == "V":
            tiene_letra = True
        if i.isspace():
            no_tiene_espacio = False
    if len(tipo_entrada_mayus) == 1 and tiene_letra and no_tiene_espacio:
        return True
    else:
        return False

def comprar_entrada_los_iluminados():
    try:
        global total_entrada_los_iluminados
        global entradas_iluminados
        global id_iluminados

        nombre_comprador = input("Ingrese nombre de comprador: ")

        # CORRECCIÓN: Validar nombre duplicado también en Iluminados
        for entrada in entradas_iluminados.values():
            if entrada[0] == nombre_comprador:
                print("Nombre repetido, ingrese otro")
                return  # Sale si encuentra el nombre repetido

        tipo_entrada = input("Ingrese tipo de entrada (CV/PAL): ")
        tipo_entrada_mayus = tipo_entrada.upper()
        valido_entrada = validar_tipo_entrada_iluminados(tipo_entrada_mayus)
        if valido_entrada:
            while True:
                codigo_confirmacion = input("Ingrese código de confirmación: ")
                valido_codigo = validar_codigo_confirmacion_iluminados(codigo_confirmacion)
                if valido_codigo:
                    print("Código validado.")
                    print("¡Entrada registrada con éxito para “los Iluminados”!")
                    # CORRECCIÓN: Guardar usando el id actual y luego incrementar.
                    entradas_iluminados[str(id_iluminados)] = [nombre_comprador, tipo_entrada_mayus, codigo_confirmacion]
                    id_iluminados += 1
                    total_entrada_los_iluminados -= 1
                    break
                else:
                    print("Código no válido. Intente otra vez")
        else:
            print("Entrada no válida. Intente otra vez con PAL o con CV")
    except:
        print("Ha ocurrido un error, intente nuevamente")

def validar_codigo_confirmacion_iluminados(codigo_confirmacion):
    # Validaciones: largo, 3 mayúsculas, número, sin espacios
    tiene_mayus = False
    tiene_numero = False
    no_tiene_espacio = True
    mayus = 0

    for i in codigo_confirmacion:
        if i.isupper():
            mayus += 1
        if i.isdigit():
            tiene_numero = True
        if i.isspace():
            no_tiene_espacio = False
    if mayus >= 3:
        tiene_mayus = True

    if len(codigo_confirmacion) >= 5 and tiene_mayus and tiene_numero and no_tiene_espacio:
        return True
    else:
        return False

def validar_tipo_entrada_iluminados(tipo_entrada_mayus):
    # Valida si es "PAL" o "CV" (sin espacios)
    if tipo_entrada_mayus == "PAL" or tipo_entrada_mayus == "CV":
        return True
    else:
        return False

def stock_de_entradas():
    # Muestra las entradas restantes de ambos conciertos
    print("Entradas disponibles para los Fortificados: ", total_entrada_los_fortificados)
    print("Entradas disponibles para los Iluminados: ", total_entrada_los_iluminados)

# Menú principal que se repite hasta que el usuario quiera salir
while True:
    print('''
    TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE
    1.- Comprar entrada a “los Fortificados”.
    2.- Comprar entrada a “los Iluminados”.
    3.- Stock de entradas para ambos conciertos.
    4.- Salir.
          ''')
    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        opcion = 0

    if opcion == 1:
        comprar_entrada_los_fortificados()
    elif opcion == 2:
        comprar_entrada_los_iluminados()
    elif opcion == 3:
        stock_de_entradas()
    elif opcion == 4:
        print("Programa terminado...")
        break
    else:
        print("Debe ingresar una opción válida!!")
