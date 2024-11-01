class Prestamo(self):
    def __init__(self, ID, usuario, libro, fechaPrestamo, fechaDevolucion):
        self.ID = ID
        self.usuario = usuario
        self.libro = libro
        self.fechaPrestamo = fechaPrestamo
        self.fechaDevolucion = fechaDevolucion
    
    def guardar(self):
        cursor.execute('''
            INSERT INTO Prestamo (usuario_id, libro_isbn, fecha_prestamo, fecha_devolucion) 
            VALUES (?, ?, ?, ?)
        ''', (self.usuario_id, self.libro_isbn, self.fecha_prestamo, self.fecha_devolucion))
        conexion.commit()
    
    @staticmethod
    def registrar_devolucion(db, prestamo_id, en_condiciones=True):
        """
        Registra la devolución de un libro, actualizando la fecha de devolución y la cantidad en inventario.
        
        Args:
            db (BaseDeDatos): Instancia de la base de datos.
            prestamo_id (int): ID del préstamo a actualizar.
            en_condiciones (bool): Si el libro está en buenas condiciones al devolverlo.
        """
        if not en_condiciones:
            print("El libro no está en buenas condiciones. Anotar para revisar.")
        
        # Actualizar la fecha de devolución en el préstamo
        db.cursor.execute('''
            UPDATE Prestamo
            SET fecha_devolucion = date('now')
            WHERE id = ?
        ''', (prestamo_id,))
        
        # Obtener el ISBN del libro del préstamo
        db.cursor.execute('''
            SELECT libro_isbn FROM Prestamo WHERE id = ?
        ''', (prestamo_id,))
        libro_isbn = db.cursor.fetchone()[0]
        
        # Actualizar la cantidad disponible en el inventario de libros
        db.cursor.execute('''
            UPDATE Libro
            SET cantidad = cantidad + 1
            WHERE isbn = ?
        ''', (libro_isbn,))
        
        db.conexion.commit()