class Autor(self):
    def __init__(self, ID, nombre, apellido, nacionalidad):
        self.ID = ID
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
    
    def guardar(self):
        cursor.execute('''
            INSERT INTO Autor (nombre, apellido, nacionalidad) 
            VALUES (?, ?, ?)
        ''', (self.nombre, self.apellido, self.nacionalidad))
        conexion.commit()
    
    @staticmethod
    def consultar(db, autor_id):
        db.cursor.execute('SELECT * FROM Autor WHERE id = ?', (autor_id,))
        return db.cursor.fetchone()

    def modificar(self, db, autor_id):
        db.cursor.execute('''
            UPDATE Autor 
            SET nombre = ?, apellido = ?, nacionalidad = ?
            WHERE id = ?
        ''', (self.nombre, self.apellido, self.nacionalidad, autor_id))
        db.conexion.commit()

    @staticmethod
    def eliminar(db, autor_id):
        db.cursor.execute('DELETE FROM Autor WHERE id = ?', (autor_id,))
        db.conexion.commit()