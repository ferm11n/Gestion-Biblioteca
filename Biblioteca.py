#Administra el catalogo de libros, los usuarios y los prestamos
class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.usuarios = []
        self.prestamos_activos = []