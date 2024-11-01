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
    
    def guardar(self, db):
        raise NotImplementedError("Este método debe ser implementado por subclases")

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, direccion, telefono, tipo_usuario="Estudiante"):
        super().__init__(nombre, apellido, direccion, telefono)
        self.tipo_usuario = tipo_usuario

    def guardar(self, db):
        db.cursor.execute('''
            INSERT INTO Usuario (nombre, apellido, tipo_usuario, direccion, telefono) 
            VALUES (?, ?, ?, ?, ?)
        ''', (self.nombre, self.apellido, self.tipo_usuario, self.direccion, self.telefono))
        db.conexion.commit()

class Profesor(Usuario):
    def __init__(self, nombre, apellido, direccion, telefono, tipo_usuario="Profesor"):
        super().__init__(nombre, apellido, direccion, telefono)
        self.tipo_usuario = tipo_usuario

    def guardar(self, db):
        db.cursor.execute('''
            INSERT INTO Usuario (nombre, apellido, tipo_usuario, direccion, telefono) 
            VALUES (?, ?, ?, ?, ?)
        ''', (self.nombre, self.apellido, self.tipo_usuario, self.direccion, self.telefono))
        db.conexion.commit()
