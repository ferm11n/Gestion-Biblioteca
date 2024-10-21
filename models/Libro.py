#Representa un libro en la biblioteca
class Libro:
    """
    El metodo __init__ es el constructor de la clase, se encarga de inicializar los atributos del objeto Libro cada vez que se crea una instancia
    Parametros: titulo, autor e isbn, son los valores que se pasan al crear un libro.
    Atributos: Estos valores se asignan a los atributos de la instancia (self.titulo, self.autor, self.isbn).
    Self.disponible: El atributo disponible se incializa como TRUE por defecto, ya que indica que el libro si esta disponible.
"""
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    """
    El metodo aDict convierte el objeto Libro en un diccionario Python. Es muy util para serializar el objeto (por si hay que
    almacenarlo en un archivo JSON o enviarlo en una API)
    El retorno: Un diccionario con los atributos del objeto, donde las claves son los nombres de los atributos y los valores son sus valores en el objeto
"""
    def aDict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.sibn,
            "disponible": self.disponible
        }
    
    @staticmethod #Indicamos con @staticmethod que va a ser un metodo estatico
    def deDict(data):
        libro = Libro(data["titulo"], data["autor"], data["isbn"])
        libro.disponible = data["disponible"]
        return libro
    
    """
    Este metodo es un metodo estatico, significa que no necesita una instancia de la clase para ser llamado. Toma un diccionario y
    crea una instancia de Libro usando los datos del diccionario

    Parametro: Data es un diccionario que tiene informacion para crear un objeto Libro
    Proceso: Primero se crea un nuevo objeto Libro utilizando los valores titulo, autor e isbn extraidos previamente del diccionario data,
    el atributo disponible se ajusta segun el valor presente en el diccionario.
    Retorno: Devuelve la instancia de Libro creada.
"""