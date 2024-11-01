class Libro(self):
    def __init__(self, ISBN, titulo, genero, anioPublicacion, autor, cantidad):
        self.ISBN = ISBN
        self.titulo = titulo
        self.genero = genero
        self.anioPublicacion = anioPublicacion
        self.autor = autor
        self.cantidad = cantidad
    
    def guardar(self):
        cursor.execute('''
            INSERT INTO Libro (isbn, titulo, genero, anio_publicacion, autor_id, cantidad) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.isbn, self.titulo, self.genero, self.anio_publicacion, self.autor_id, self.cantidad))
        conexion.commit()
    
    @staticmethod
    def consultar(db, isbn):
        db.cursor.execute('SELECT * FROM Libro WHERE isbn = ?', (isbn,))
        return db.cursor.fetchone()

    def modificar(self, db):
        db.cursor.execute('''
            UPDATE Libro 
            SET titulo = ?, genero = ?, anio_publicacion = ?, autor_id = ?, cantidad = ?
            WHERE isbn = ?
        ''', (self.titulo, self.genero, self.anio_publicacion, self.autor_id, self.cantidad, self.isbn))
        db.conexion.commit()

    @staticmethod
    def eliminar(db, isbn):
        db.cursor.execute('DELETE FROM Libro WHERE isbn = ?', (isbn,))
        db.conexion.commit()
    
    @staticmethod
    def consultar_disponibilidad(isbn):
        cursor.execute('SELECT cantidad FROM Libro WHERE isbn = ?', (isbn,))
        cantidad = cursor.fetchone()
        if cantidad and cantidad[0] > 0:
            return True
        return False