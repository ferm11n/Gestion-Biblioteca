from Biblioteca import Biblioteca
from models.Libro import Libro
from models.Usuario import Usuario
from tipoDeUsuarios import Alumno
from tipoDeUsuarios import Profesor
from gestionarJSON import guardarDatos
from gestionarJSON import cargarDatos

biblioteca = Biblioteca()

def menu():
    while True:
        print("\n--- Menú Biblioteca ---")
        print("1. Agregar libro")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Guardar y salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, isbn)
            biblioteca.agregarLibro(libro)
        elif opcion == "2":
            nombre = input("Nombre: ")
            idUsuario = input("ID: ")
            tipo = input("Tipo de usuario (Alumno/Profesor): ")
            if tipo.lower() == "alumno":
                usuario = Alumno(nombre, idUsuario)
            elif tipo.lower() == "profesor":
                usuario = Profesor(nombre, idUsuario)
            else:
                usuario = Usuario(nombre, idUsuario)
            biblioteca.registrarUsuario(usuario)
        elif opcion == "3":
            isbn = input("Ingrese el ISBN del libro: ")
            idUsuario = input("Ingrese el ID del usuario: ")

            # Buscar el libro por ISBN
            libro = next((l for l in biblioteca.catalogo if l.isbn == isbn), None)
            
            # Buscar el usuario por ID
            usuario = next((u for u in biblioteca.usuarios if u.idUsuario == idUsuario), None)

            if libro and usuario:
                biblioteca.prestarLibro(libro, usuario)
            else:
                print("Libro o usuario no encontrado.")
        elif opcion == "4":
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            idUsuario = input("Ingrese el ID del usuario: ")

            # Buscar el usuario por ID
            usuario = next((u for u in biblioteca.usuarios if u.idUsuario == idUsuario), None)

            # Encontrar el préstamo activo del usuario
            if usuario:
                prestamo = next((p for p in usuario.prestamos if p.libro.isbn == isbn and not p.devuelto), None)
                
                if prestamo:
                    prestamo.libro.disponible = True
                    prestamo.devuelto = True
                    print(f"El libro '{prestamo.libro.titulo}' ha sido devuelto exitosamente.")
                else:
                    print("No se encontró un préstamo activo para este libro.")
            else:
                print("Usuario no encontrado.")
        elif opcion == "5":
            guardarDatos(biblioteca)
            print("Datos guardados, saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

menu()
