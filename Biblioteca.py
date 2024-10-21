#Administra el catalogo de libros, los usuarios y los prestamos
from models.Prestamo import Prestamo
from models.Usuario import Usuario
from models.Libro import Libro
from utils import fechaActual


"""

"""
class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.usuarios = []
        self.prestamosActivos = []
        self.historialPrestamos = []


    """
    doc2
"""
    def agregarLibro(self, libro):
        self.catalogo.append(libro)
    



    """
    doc3
"""
    def registrarUsuario(self, usuario):
        self.usuarios.append(usuario)





    """
    doc4
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