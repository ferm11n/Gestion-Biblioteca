#Representa un prestamo de un libro a un usuario

"""
datetime: Lo utilizamos para menjar fecha y horas
timedelta: Permite realizar operaciones con fechas, como sumar o restar dias
"""
from datetime import datetime, timedelta
from models.Usuario import Usuario
from models.Libro import Libro 


"""
Constructor_ __init__

Parametros:
    Libro: Es un objeto de la clase Libro
    usuario: Es un objeto de la clase Usuario.
    fechaPrestamo: Es un objeto datetime que representa la fecha en que se hizo el prestamo.
    duracionDias: Es un numero entero que indica la duracion del prestamo en dias.

Atributos: 
- self.libro Almacena el objeto Libro
- self.usuario: Almacena el objeto usuario.
- self.fechaPrestamo: almacena la fecha en que se hizo el prestamo
- self.fechaDevolucion; Calcula lka fecha de de devolucion sumando la duracion del prestamo (en dias)
a la fecha del prestamo usando timedelta(days=duracionDias).
"""
class Prestamo:
    def __init__(self, libro, usuario, fechaPrestamo, duracionDias):
        self.libro = libro
        self.usuario = usuario
        self.fechaPrestamo = fechaPrestamo
        self.fechaDevolucion = fechaPrestamo + timedelta(days=duracionDias)


    """
    El metodo aDict convierte el objeto Prestamo a un diccionario.

    Su funcion es convertir el objeto Prestamo a un diccionario, convierte los atributos libros y usuarios a diccionarios
    usando sus respectivos metodos aDict(). Tambien convierte las fechas (fechasPrestamo y fechaDevolucion) a cadenas de
    texto con el formato "YYYY-MM-DD" usando strftime().
"""
    def aDict(self):
        return {
            "ibro": self.libro.aDict(),
            "usuario": self.usuario.aDict(),
            "fechaPrestamo": self.fechaPrestamo.strftime("%Y-%m-%d"),
            "fechaDevolucion": self.fechaDevolucion.strftime("%Y-%m-%d")
        }




    """
    El metodo estatico deDict() toma un diccionario de datos y crea una instancia de Prestamo.

    Parametros: data es un diccionario que contiene la informacion del prestamo.

    Proceso: Usa datetime.strptime para convertir las cadenas de fecha de fechaPrestamo y fechaDevolucion de vuelta a objetos datetime.
    Crea una instancia de Prestamo utilizando la informacion del diccionario:
    - Libro.aDict(data["libro"]) esto crea un objeto Libro desde el diccionario correspondiente
    - Usuario.aDict(data["usuario"]): Esto crea un objeto Usuario desde el diccionario correspondiente
    - fechaPrestamo: La fecha del prestamo convertida
    - La duracion del prestamo (en dias) se calcula restando fechaPrestamo de fechaDevolucion

    Retorno: Devuelve una instancia de Prestamo con los atributos cargados desde el diccionario
""" 
    @staticmethod
    def deDict(data):
        fechaPrestamo = datetime.strptime(data["fechaPrestamo"], "%Y-%m-%d")
        fechaDevolucion = datetime.strptime(data["fechaDevolucion"], "%Y-%m-%d")
        return Prestamo(Libro.aDict(data["libro"]), Usuario.aDict(data["usuario"]), fechaPrestamo, (fechaDevolucion - fechaPrestamo).days)
    