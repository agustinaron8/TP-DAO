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

class Usuario(self):
    def __init__(self, ID, nombre, apellido, tipoUsuario, direccion, telefono):
        pass # Espero rta del profe para aplicar patrón Factory

class Prestamo(self):
    def __init__(self, ID, usuario, libro, fechaPrestamo, fechaDevolucion):
        self.ID = ID
        self.usuario = usuario # Ver que onda esto xq usuario es una clase
        self.libro = libro
        self.fechaPrestamo = fechaPrestamo
        self.fechaDevolucion = fechaDevolucion