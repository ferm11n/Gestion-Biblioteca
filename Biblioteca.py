#Administra el catalogo de libros, los usuarios y los prestamos
from models.Prestamo import Prestamo
from models.Usuario import Usuario
from models.Libro import Libro
from utils import fechaActual
import json
from gestionarJSON import guardarDatos

"""
Clase biblioteca, esta clase gestiona el catalogo de libros, los usuarios, los prestamos activos y el historial de prestamos

Catalogo: Es una lista que almacena los objetos Libro disponibles en la biblioteca
Usuarios: Es una lista que almacena los objetos de Usuario registrados en la biblioteca
prestamosActivos: Es una lista que contiene los objetos Prestamo que estan actualmente activos (libros que no han sido devueltos)
historialPrestamos: Es una lista que contiene todos los prestamos que ua fueron completados (cuando los libros han sido devueltos)
"""
class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.usuarios = []
        self.prestamosActivos = []
        self.historialPrestamos = []


    
    
    """
    Metodo agregarLibro: Agrega un objeto Libro al catalogo de la biblioteca
    Parametros: Libro: El objeto Libro que se dea agregar al catalogo
"""
    def agregarLibro(self, libro):
        self.catalogo.append(libro)
        guardarDatos(self)
    



    """
    Metodo registrarUsuario: Agrega un objeto Usuario a la lista de usuarios de la biblioteca
    Parametros: Usuario: El objeto Usuario que se desea registrar en la biblioteca
"""
    def registrarUsuario(self, usuario):
        self.usuarios.append(usuario)
        guardarDatos(self)





    """
    Metodo prestarLibro, realiza un prestamo de un libro a un usuario
    Parametros:
    - libro: El objeto Libro que se desea prestar.
    - usuario: El objeto Usuario que solicita el prestamo
    - duracionDias: Un numero entero que indica la duracion del prestamo en dias

    Verifica si el libro esta disponible (libro.disponible). Si el libro esta disponible, crea un objeto Prestamo usando el libro,
    el usuario y la fecha actual y la duracion del prestamo.
    Marca el libro como no disponible (libro.disponible = false)
    Agrega el prestamo a la lista de prestamosActivos.
    Agrega el prestamo a la lista de prestamos del usuario (usuario.prestamos)

    Si el libro no esta disponible, imprime un mensaje diciendo que el libro no se puede prestar.
"""
    def prestarLibro(self, isbnlibro, idUsuario,):
        libroEncontrado = None
        for libro in self.catalogo:
            if libro.isbn == isbnlibro:
                libroEncontrado = libro
                break

        if libroEncontrado is None:
            raise ValueError(f"Libro con ISBN '{isbnlibro}' no encontrado en el catalogo.")
        
        #Buscar el usuario por su ID
        usuarioEncontrado = None
        for usuario in self.usuarios:
            if usuario.idUsuario == idUsuario:
                usuarioEncontrado = usuario
                break
        if usuarioEncontrado is None:
            raise ValueError(f"Usuario con ID '{idUsuario}' no encontrado.")
        
        #Verifica si el libro esta disponible
        if not libroEncontrado.disponible:
            raise ValueError(f"El libro '{libroEncontrado.titulo}' no esta disponible para prestar")
        
        #Registrar el prestamo
        prestamo = Prestamo(libroEncontrado, usuarioEncontrado, fechaActual())
        libroEncontrado.disponible = False
        self.prestamosActivos.append(prestamo)
        usuarioEncontrado.prestamos.append(prestamo)
        guardarDatos(self) #Guardamos los cambios automaticamente
        print(f"Libro '{libroEncontrado.titulo}' prestado exitosamente a {usuarioEncontrado.nombre}")








    """
    Metodo devolverLibro, marca un libro como devuelto

    Parametros:
        - libro: El objeto Libro que se esta devolviendo
        - Usuario: El objeto Usuario que devuelve el libro

    Busca en la lista de prestamosActivos el prestamo correspondiente al libro y al usuario.
    Si encuentra el prestamo: 
        - Marca el libro como disponible (libro.disponible = true)
        - Mueve el prestamo de la lista de prestamosActivos a historialPrestamos
        - Elimina el prestamo de prestamosActivados

    Si no encuentra un prestamo activo que coincida con el libro y el usuario, imprime
    un mensaje indicando que no se encontro un prestamo activo.
"""
    def devolverLibro(self, libro, usuario):
        for prestamo in self.prestamosActivos:
            if prestamo.libro == libro and prestamo.usuario == usuario:
                libro.disponible = True  # Corrige la asignación aquí
                self.historialPrestamos.append(prestamo)        
                self.prestamosActivos.remove(prestamo)
                guardarDatos(self)  # Llamada para guardar los datos después de devolver el libro
                print(f"El libro '{libro.titulo}' ha sido devuelto exitosamente.")
                break
        else:
            # Cambia esto para lanzar un ValueError en lugar de un print
            raise ValueError("No se pudo encontrar un préstamo activo para este libro y usuario.")     