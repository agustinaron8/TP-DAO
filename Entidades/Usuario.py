# Clase UsuarioFactory para crear instancias de Usuario, Estudiante o Profesor
class UsuarioFactory:
    @staticmethod
    def crear_usuario(tipo_usuario, id, nombre, apellido, direccion, telefono):
        if tipo_usuario.lower() == "estudiante":
            return Estudiante(id, nombre, apellido, direccion, telefono)
        elif tipo_usuario.lower() == "profesor":
            return Profesor(id, nombre, apellido, direccion, telefono)
        else:
            raise ValueError("Tipo de usuario no reconocido")

# Clase base Usuario
class Usuario:
    def __init__(self, id, nombre, apellido, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

    def guardar(self, db):
        raise NotImplementedError("Este método debe ser implementado por subclases")

    @staticmethod
    def consultar(db, usuario_id):
        db.cursor.execute('SELECT * FROM Usuario WHERE id = ?', (usuario_id,))
        return db.cursor.fetchone()

    def modificar(self, db):
        raise NotImplementedError("Este método debe ser implementado por subclases")

    @staticmethod
    def eliminar(db, usuario_id):
        db.cursor.execute('DELETE FROM Usuario WHERE id = ?', (usuario_id,))
        db.conexion.commit()

# Subclase Estudiante
class Estudiante(Usuario):
    def __init__(self, id, nombre, apellido, direccion, telefono, tipo_usuario="Estudiante"):
        super().__init__(id, nombre, apellido, direccion, telefono)
        self.tipo_usuario = tipo_usuario

    def guardar(self, db):
        db.cursor.execute('''
            INSERT INTO Usuario (nombre, apellido, tipo_usuario, direccion, telefono) 
            VALUES (?, ?, ?, ?, ?)
        ''', (self.nombre, self.apellido, self.tipo_usuario, self.direccion, self.telefono))
        db.conexion.commit()

    def modificar(self, db):
        db.cursor.execute('''
            UPDATE Usuario 
            SET nombre = ?, apellido = ?, tipo_usuario = ?, direccion = ?, telefono = ?
            WHERE id = ?
        ''', (self.nombre, self.apellido, self.tipo_usuario, self.direccion, self.telefono, self.id))
        db.conexion.commit()

# Subclase Profesor
class Profesor(Usuario):
    def __init__(self, id, nombre, apellido, direccion, telefono, tipo_usuario="Profesor"):
        super().__init__(id, nombre, apellido, direccion, telefono)
        self.tipo_usuario = tipo_usuario

    def guardar(self, db):
        db.cursor.execute('''
            INSERT INTO Usuario (nombre, apellido, tipo_usuario, direccion, telefono) 
            VALUES (?, ?, ?, ?, ?)
        ''', (self.nombre, self.apellido, self.tipo_usuario, self.direccion, self.telefono))
        db.conexion.commit()

    def modificar(self, db):
        db.cursor.execute('''
            UPDATE Usuario 
            SET nombre = ?, apellido = ?, tipo_usuario = ?, direccion = ?, telefono = ?
            WHERE id = ?
        ''', (self.nombre, self.apellido, self.tipo_usuario, self.direccion, self.telefono, self.id))
        db.conexion.commit()