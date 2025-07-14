
# Definición de variables globales
stock_fortificados = 500
stock_iluminados = 500

compras_fortificados = {}
compras_iluminados = {}


def verificar_codigo_fortificados(codigo):
    tiene_mayuscula = any(c.isupper() for c in codigo)
    tiene_numero = any(c.isdigit() for c in codigo)
    tiene_espacio = any(c.isspace() for c in codigo)
    return len(codigo) >= 6 and tiene_mayuscula and tiene_numero and not tiene_espacio

def verificar_codigo_iluminados(codigo):
    tiene_mayuscula = sum(1 for c in codigo if c.isupper()) >= 3
    tiene_numero = any(c.isdigit() for c in codigo)
    tiene_espacio = any(c.isspace() for c in codigo)
    return len(codigo) >= 5 and tiene_mayuscula and tiene_numero and not tiene_espacio

'''
Otra forma de verificar codigo de confirmacion para "los Fortificados" puede hacerse lo mismo para "los Iluminados":

def verificar_codigo_fortificados(codigo):
    if len(codigo) < 6:
        return False
    if not any(c.isupper() for c in codigo):
        return False
    if not any(c.isdigit() for c in codigo):
        return False
    if any(c.isspace() for c in codigo):
        return False
    return True
'''

def comprar_entrada_fortificados():
    global stock_fortificados
    if stock_fortificados <= 0:
        print("No hay entradas disponibles para 'los Fortificados'.")
        return # Si no hay stock, salimos de la función
    
    nombre = input("Ingrese el nombre del comprador: ")
    if nombre in compras_fortificados:
        print("El nombre de comprador ya está registrado.")
        return # Si el nombre ya existe, salimos de la función
    
    tipo_entrada = input("Ingrese el tipo de entrada (G para General, V para VIP): ").upper()
    if tipo_entrada not in ['G', 'V']:
        print("Tipo de entrada inválido. Debe ser 'G' o 'V'.")
        return # Si el tipo de entrada no es válido, salimos de la función
    
    codigo_confirmacion = input("Ingrese el código de confirmación (mínimo 6 caracteres, al menos 1 mayúscula, 1 número, sin espacios): ")
    if not verificar_codigo_fortificados(codigo_confirmacion):
        print("Código de confirmación inválido. Debe tener al menos 6 caracteres, al menos 1 letra mayúscula, al menos 1 número y no puede tener espacios.")
        return
    
    compras_fortificados[nombre] = {'tipo': tipo_entrada, 'codigo': codigo_confirmacion}
    stock_fortificados -= 1
    print(f"Entrada comprada exitosamente para 'los Fortificados'. Entradas restantes: {stock_fortificados}")

def comprar_entrada_iluminados():
    global stock_iluminados
    if stock_iluminados <= 0:
        print("No hay entradas disponibles para 'los Iluminados'.")
        return # Si no hay stock, salimos de la función
    
    nombre = input("Ingrese el nombre del comprador: ")
    if nombre in compras_iluminados:
        print("El nombre de comprador ya está registrado.")
        return # Si el nombre ya existe, salimos de la función
    
    tipo_entrada = input("Ingrese el tipo de entrada (CV para Cancha VIP, PAL para Palco): ").upper()
    if tipo_entrada not in ['CV', 'PAL']:
        print("Tipo de entrada inválido. Debe ser 'CV' o 'PAL'.")
        return # Si el tipo de entrada no es válido, salimos de la función
    
    codigo_confirmacion = input("Ingrese el código de confirmación (mínimo 5 caracteres, al menos 3 mayúsculas, 1 número, sin espacios): ")
    if not verificar_codigo_iluminados(codigo_confirmacion):
        print("Código de confirmación inválido. Debe tener al menos 5 caracteres, al menos 3 letras mayúsculas, al menos 1 número y no puede tener espacios.")
        return
    
    compras_iluminados[nombre] = {'tipo': tipo_entrada, 'codigo': codigo_confirmacion}
    stock_iluminados -= 1
    print(f"Entrada comprada exitosamente para 'los Iluminados'. Entradas restantes: {stock_iluminados}")

def mostrar_stock():
    print(f"Stock de entradas para 'los Fortificados': {stock_fortificados}")
    print(f"Stock de entradas para 'los Iluminados': {stock_iluminados}")
    print("Compras realizadas para 'los Fortificados':")
    for nombre, datos in compras_fortificados.items():
        print(f"Nombre: {nombre}, Tipo: {datos['tipo']}, Código: {datos['codigo']}")
    
    print("Compras realizadas para 'los Iluminados':")
    for nombre, datos in compras_iluminados.items():
        print(f"Nombre: {nombre}, Tipo: {datos['tipo']}, Código: {datos['codigo']}")

while True:
    print("TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE")
    print("1.- Comprar entrada a “los Fortificados”.")
    print("2.- Comprar entrada a “los Iluminados”.")
    print("3.- Stock de entradas para ambos conciertos.")
    print("4.- Salir.")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        comprar_entrada_fortificados()
    elif opcion == '2':
        comprar_entrada_iluminados()
    elif opcion == '3':
        mostrar_stock()
    elif opcion == '4':
        print("Programa terminado...")
        break
    else:
        print("Debe ingresar una opción válida!!")