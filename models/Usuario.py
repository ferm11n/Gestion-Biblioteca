#Representa a una persona que puede tomar libros prestados



"""
El metodo __init__ es el constructor de la clase Usuario, inicializa los atributos del objeto cuando se crea una instancia

Parametros:
    nobre: El nombre del usuario
    idUsuario: Un identificador unico para el usuario
    tipoDeUsuario: Por defecto es "General" pero se puede cambiar cuando se crea un usario con un tipo diferente como "Alumno" o "Profesor"
Atributos:
    self.nombre, self.idUsuario, self.TipoDeUsuario: Se asignan con los valores proporcionados al contructor
    self.prestamos: Se incializa como una lista vacia para almacenar los prestamos que el usuario realiza
"""
class Usuario:
    def __init__(self, nombre, idUsuario, tipoDeUsuario="General"):
        self.nombre = nombre
        self.idUsuario = idUsuario
        self.tipoDeUsuario = tipoDeUsuario
        self.prestamos = []




    """
    El metodo aDict convierte el objeto Usuario en un diccionario, osea, convierte los atributos del usuario en un formato de diccionario,
    incluyendo los prestamos que ha realizado (estos tambien se convierten a diccionarios en -> 'p.aDict()')
"""
    def aDict(self):
        return {
            "nombre": self.nombre,
            "idUsuario": self.idUsuario,
            "tipoDeUsuario": self.tipoDeUsuario,
            "prestamos": [p.aDict() for p in self.prestamos]
        }
    





    """
    Este metodo estatico (deDict), crea una instancia de Usuario a partir de un diccionario de datos.

    Parametro: Data es un diccionario que contiene la informacion del usuario.

    Flujo: Se crea una instancia de Usuario usando los valores del diccionario, si el diccionario tiene prestamos,
    tambien se crea instancias de Prestamo a partir de esos datos y las añade a la lista de prestamos del usuario.

    Retorno: Devuelve una instancia de Usuario con todos los atributos cargados desde el diccionario.

    """
    
    @staticmethod
    def deDict(data):
        from models.Prestamo import Prestamo
        usuario = Usuario(data["nombre"], data["idUsuario"], data["tipoDeUsuario"])
        usuario.prestamos = [Prestamo.deDict(p) for p in data["prestamos"]]
        return usuario
    

