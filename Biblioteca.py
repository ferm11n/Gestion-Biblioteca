#Administra el catalogo de libros, los usuarios y los prestamos
from models.Prestamo import Prestamo
from models.Usuario import Usuario
from models.Libro import Libro
from utils import fechaActual

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.usuarios = []
        self.prestamos_activos = []

    def agregarLibro(self, libro):
        self.catalogo.append(libro)
    
    def registrarUsuario(self, usuario):
        self.usuarios.append(usuario)

    def prestarLibro(self, libro, usuario):
        if libro.disponible:
            prestamo = Prestamo(libro, usuario, fechaActual())
            libro.disponible = False
            self.prestamosActivos.append(prestamo)
            usuario.prestamos.append(prestamo)
        else:
            print(f"El libro '{libro.titulo}' no está disponible.")    