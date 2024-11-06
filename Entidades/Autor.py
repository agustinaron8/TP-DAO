class Autor:
    def __init__(self, ID, nombre, apellido, nacionalidad):
        self.ID = ID
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad

    def guardar(self, db):
        try:
            db.cursor.execute('''
                INSERT INTO Autor (nombre, apellido, nacionalidad) 
                VALUES (?, ?, ?)
            ''', (self.nombre, self.apellido, self.nacionalidad))
            db.conexion.commit()
            return True
        except Exception as e:
            return e

    @staticmethod
    def consultar(db, autor_id):
        try:
            db.cursor.execute('SELECT * FROM Autor WHERE id = ?', (autor_id,))
            resultado = db.cursor.fetchone()
            return resultado if resultado else None
        except Exception as e:
            return e

    def modificar(self, db, autor_id):
        try:
            db.cursor.execute('''
                UPDATE Autor 
                SET nombre = ?, apellido = ?, nacionalidad = ?
                WHERE id = ?
            ''', (self.nombre, self.apellido, self.nacionalidad, autor_id))
            db.conexion.commit()
            return True
        except Exception as e:
            return e

    @staticmethod
    def eliminar(db, autor_id):
        try:
            db.cursor.execute('DELETE FROM Autor WHERE id = ?', (autor_id,))
            db.conexion.commit()
            return True
        except Exception as e:
            return e