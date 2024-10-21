#Administra el catalogo de libros, los usuarios y los prestamos
from models.Prestamo import Prestamo
from models.Usuario import Usuario
from models.Libro import Libro
from utils import fechaActual


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
    



    """
    Metodo registrarUsuario: Agrega un objeto Usuario a la lista de usuarios de la biblioteca
    Parametros: Usuario: El objeto Usuario que se desea registrar en la biblioteca
"""
    def registrarUsuario(self, usuario):
        self.usuarios.append(usuario)





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
    def prestarLibro(self, libro, usuario):
        if libro.disponible:
            prestamo = Prestamo(libro, usuario, fechaActual())
            libro.disponible = False
            self.prestamosActivos.append(prestamo)
            usuario.prestamos.append(prestamo)
        else:
            print(f"El libro '{libro.titulo}' no está disponible.")






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
                libro,disponible = True
                self.historialPrestamos.append(prestamo)        
                self.prestamosActivos.remove(prestamo)
                break
        else:#reemplazar con ValueError -> Raise
            print("No se pudo encontrar un prestamo activo para este libro y usuario.")        