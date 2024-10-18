"""
o Libro: Código ISBN, título, género, año de publicación, autor, cantidad 
disponible.
o Autor: ID, nombre, apellido, nacionalidad.
o Usuario: ID, nombre, apellido, tipo de usuario (estudiante, profesor), 
dirección, teléfono.
o Prestamo: ID, usuario, libro, fecha de préstamo, fecha de devolución.
*/
"""

class Libro(self):
    def __init__(self, ISBN, titulo, genero, anioPublicacion, autor, cantidad):
        self.ISBN = ISBN
        self.titulo = titulo
        self.genero = genero
        self.anioPublicacion = anioPublicacion
        self.autor = autor # Ver que onda esto xq autor es una clase
        self.cantidad = cantidad

class Autor(self):
    def __init__(self, ID, nombre, apellido, nacionalidad):
        self.ID = ID
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad

## Implementación de Patrón Factory
class UsuarioFactory:
    @staticmethod
    def crear_usuario(tipo_usuario, id, nombre, apellido, direccion, telefono):
        if tipo_usuario == "estudiante":
            return Estudiante(id, nombre, apellido, direccion, telefono)
        elif tipo_usuario == "profesor":
            return Profesor(id, nombre, apellido, direccion, telefono)
        else:
            raise ValueError("Tipo de usuario no reconocido")

class Usuario:
    def __init__(self, id, nombre, apellido, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

class Estudiante(Usuario):
    pass

class Profesor(Usuario):
    pass


class Prestamo(self):
    def __init__(self, ID, usuario, libro, fechaPrestamo, fechaDevolucion):
        self.ID = ID
        self.usuario = usuario # Ver que onda esto xq usuario es una clase
        self.libro = libro
        self.fechaPrestamo = fechaPrestamo
        self.fechaDevolucion = fechaDevolucion