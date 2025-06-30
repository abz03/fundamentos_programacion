
'''
 Diccionarios: Los diccionarios son una estructura de datos
 que guarda los datos según la combinación clave:valor.
 Por lo tanto, accedemos a los datos a través de su clave.
'''
#Ejemplo de diccionario simple

estudiante = {
    "nombre": "Óscar",
    "edad":37,
    "email":"oscar.badilla@profesor.duoc.cl",
    "esta_matriculado": True,
    "estatura":1.69
}

#Se acceden a los valores de los datos a través de su clave

#print("El nombre del estudiante es", estudiante["nombre"], "y su edad es:", estudiante["edad"])

estudiantes = []

estudiantes.append(estudiante)

estudiantes.append({
    "nombre": "Juan",
    "edad":25,
    "email":"juan@duocuc.cl",
    "esta_matriculado": True,
    "estatura":1.75
})

#print(estudiantes)


#print("La edad del segundo estudiante es: ",estudiantes[1]["edad"])
