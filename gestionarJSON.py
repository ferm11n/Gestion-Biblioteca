import json
import Biblioteca
from models.Libro import Libro
from models.Usuario import Usuario
from models.Prestamo import Prestamo

def guardarDatos(biblioteca, archivo="biblioteca.json"):
    # Cargar los datos existentes, si el archivo ya existe
    try:
        with open(archivo, 'r') as f:
            datos_existentes = json.load(f)
    except FileNotFoundError:
        datos_existentes = {"catalogo": [], "usuarios": [], "prestamos_activos": []}

    # Agregar nuevos libros sin sobrescribir los existentes
    for libro in biblioteca.catalogo:
        if libro.aDict() not in datos_existentes["catalogo"]:
            datos_existentes["catalogo"].append(libro.aDict())

    # Agregar nuevos usuarios sin sobrescribir los existentes
    for usuario in biblioteca.usuarios:
        if usuario.aDict() not in datos_existentes["usuarios"]:
            datos_existentes["usuarios"].append(usuario.aDict())

    # Agregar nuevos préstamos sin sobrescribir los existentes
    for prestamo in biblioteca.prestamosActivos:
        if prestamo.aDict() not in datos_existentes["prestamos_activos"]:
            datos_existentes["prestamos_activos"].append(prestamo.aDict())

    # Guardar los datos actualizados
    with open(archivo, 'w') as f:
        json.dump(datos_existentes, f, indent=4)
    print("Datos guardados exitosamente.")


def cargarDatos(biblioteca, archivo="biblioteca.json"):
    try:
        with open(archivo, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"No se encontró el archivo {archivo}, comenzando con una biblioteca vacía.")
        return

    # Cargar los libros
    biblioteca.catalogo = [Libro(**libro) for libro in data["catalogo"]]

    # Cargar los usuarios
    biblioteca.usuarios = [Usuario(**usuario) for usuario in data["usuarios"]]

    # Cargar los préstamos activos
    for prestamo_data in data["prestamos_activos"]:
        libro_dict = prestamo_data['libro']
        usuario_dict = prestamo_data['usuario']
        fecha_prestamo = prestamo_data['fecha_prestamo']

        # Crear los objetos correspondientes de libro y usuario
        libro = Libro(**libro_dict)
        usuario = Usuario(**usuario_dict)

        # Crear el objeto préstamo
        prestamo = Prestamo(libro, usuario, fecha_prestamo)

        # Agregar a los préstamos activos
        biblioteca.prestamosActivos.append(prestamo)

    print("Datos cargados exitosamente.")