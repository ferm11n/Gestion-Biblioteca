#Representa un prestamo de un libro a un usuario
class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo