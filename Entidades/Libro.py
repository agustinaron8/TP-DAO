class Libro:
    def __init__(self, ISBN, titulo, genero, anioPublicacion, autor, cantidad):
        self.ISBN = ISBN
        self.titulo = titulo
        self.genero = genero
        self.anioPublicacion = anioPublicacion
        self.autor = autor
        self.cantidad = cantidad

    @staticmethod
    def validar_ISBN(isbn):
        """
        Valida el ISBN ingresado. Puede ser un ISBN-10 o ISBN-13.
        Retorna True si es válido, de lo contrario, False.
        """
        isbn = isbn.replace("-", "")  # Eliminar cualquier guión en el ISBN
        if len(isbn) == 10:
            # Validación para ISBN-10
            total = sum((i + 1) * int(d) for i, d in enumerate(isbn[:-1]))
            check_digit = total % 11
            return str(check_digit) == isbn[-1] or (check_digit == 10 and isbn[-1] == "X")
        elif len(isbn) == 13:
            # Validación para ISBN-13
            total = sum((1 if i % 2 == 0 else 3) * int(d) for i, d in enumerate(isbn))
            return total % 10 == 0
        return False

    def guardar(self, db):
        if not self.validar_ISBN(self.ISBN):
            return ValueError("ISBN no válido.")
        try:
            db.cursor.execute('''
                INSERT INTO Libro (isbn, titulo, genero, anio_publicacion, autor_id, cantidad) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (self.ISBN, self.titulo, self.genero, self.anioPublicacion, self.autor, self.cantidad))
            db.conexion.commit()
            return True
        except Exception as e:
            return e

    @staticmethod
    def consultar(db, isbn):
        try:
            db.cursor.execute('SELECT * FROM Libro WHERE isbn = ?', (isbn,))
            resultado = db.cursor.fetchone()
            return resultado if resultado else None
        except Exception as e:
            return e

    def modificar(self, db):
        if not self.validar_ISBN(self.ISBN):
            return ValueError("ISBN no válido.")
        try:
            db.cursor.execute('''
                UPDATE Libro 
                SET titulo = ?, genero = ?, anio_publicacion = ?, autor_id = ?, cantidad = ?
                WHERE isbn = ?
            ''', (self.titulo, self.genero, self.anioPublicacion, self.autor, self.cantidad, self.ISBN))
            db.conexion.commit()
            return True
        except Exception as e:
            return e

    @staticmethod
    def eliminar(db, isbn):
        try:
            db.cursor.execute('DELETE FROM Libro WHERE isbn = ?', (isbn,))
            db.conexion.commit()
            return True
        except Exception as e:
            return e

    @staticmethod
    def consultar_disponibilidad(db, isbn):
        try:
            db.cursor.execute('SELECT cantidad FROM Libro WHERE isbn = ?', (isbn,))
            cantidad = db.cursor.fetchone()
            return cantidad[0] > 0 if cantidad else False
        except Exception as e:
            return e