
shows = {
    "fortificados": {
        "stock": 500,
        "tipos_entrada": ["G", "V"],
        "reglas_codigo": {
            "largo_minimo": 6,
            "mayusculas": 1,
            "numeros": 1,
            "espacios": False
        },
        "compras": {}
    },
    "iluminados": {
        "stock": 500,
        "tipos_entrada": ["CV", "PAL"],
        "reglas_codigo": {
            "largo_minimo": 5,
            "mayusculas": 3,
            "numeros": 1,
            "espacios": False
        },
        "compras": {}
    }
}

def verificar_codigo(show,codigo):
    reglas = shows[show]["reglas_codigo"]
    mayusculas = 0
    numeros = 0
    espacios = 0
    for char in codigo:
        if char.isupper():
            mayusculas += 1
        elif char.isdigit():
            numeros += 1
        elif char.isspace():
            espacios += 1
    if len(codigo) < reglas["largo_minimo"] or mayusculas < reglas["mayusculas"] or numeros < reglas["numeros"] or (reglas["espacios"] and espacios > 0):
        return False
    return True

def comprar_entrada(show):
    if shows[show]["stock"] <= 0:
        print(f"No hay entradas disponibles para '{show}'.")
        return
    
    nombre = input("Ingrese el nombre del comprador: ").lower()
    if nombre in shows[show]["compras"]:
        print("El nombre de comprador ya está registrado.")
        return
    
    tipo_entrada = input(f"Ingrese el tipo de entrada ({shows[show]['tipos_entrada']}): ").upper()
    if tipo_entrada not in shows[show]["tipos_entrada"]:
        print(f"Tipo de entrada inválido. Debe ser {shows[show]['tipos_entrada']}.")
        return
    
    codigo_confirmacion = input("Ingrese el código de confirmación: ")
    if not verificar_codigo(show, codigo_confirmacion):
        print("Código de confirmación inválido.")
        return
    
    shows[show]["compras"][nombre] = {'tipo': tipo_entrada, 'codigo': codigo_confirmacion}
    shows[show]["stock"] -= 1
    print(f"Entrada comprada exitosamente para '{show}'. Entradas restantes: {shows[show]['stock']}") 

def mostrar_stock():
    print("Stock de entradas:")
    for show in shows:
        stock = shows[show]["stock"]
        print(f" - {show}: {stock} entradas disponibles.")
        
while True:
    print("TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE")
    print("1.- Comprar entrada a “los Fortificados”.")
    print("2.- Comprar entrada a “los Iluminados”.")
    print("3.- Stock de entradas para ambos conciertos.")
    print("4.- Salir.")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        comprar_entrada("fortificados")
    elif opcion == '2':
        comprar_entrada("iluminados")
    elif opcion == '3':
        mostrar_stock()
    elif opcion == '4':
        print("Programa terminado...")
        break
    else:
        print("Debe ingresar una opción válida!!")