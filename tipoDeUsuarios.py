from models.Usuario import Usuario

"""
Estas 2 clases heredan de la clase Usuario, lo que significa que reutilizan la funcionalidad
de la clase base, pero modifican el valor de tipoDeUsuario en el constructor

Clase Alumno: El constructor llama al constructor de la clase base (super().__init__) con nombre, idUsuario y define
el tipoDeUsuario como "Alumno".

Herencia; Al heredar de Usuario, la clase Alumno tiene todos los metodos y atributos de Usuario, pero con la particularidad de que
siempre sera del tipo ALUMNO.
"""
class Alumno(Usuario):
    def __init__(self, nombre, idUsuario):
        super().__init__(nombre, idUsuario, tipoDeUsuario="Alumno")





"""
Clase Profesor: De manera similar, esta clase define que el tipoDeUsario siempre sera "Profesor".

Herencia: Al heredar de Usuario, Profesor tambien hereda los atributos y metodos de la clase base.
"""
class Profesor(Usuario):
    def __init__(self, nombre, idUsuario):
        super().__init__(nombre, idUsuario, tipoDeUsuario="Profesor")