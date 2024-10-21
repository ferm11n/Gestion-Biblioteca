#Representa a una persona que puede tomar libros prestados
class Usuario:
    def __init__(self, nombre, idUsuario):
        self.nombre = nombre
        self.idUsuario = idUsuario
        self.prestamos = []