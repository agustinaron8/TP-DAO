import sqlite3

class BaseDeDatos:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(BaseDeDatos, cls).__new__(cls)
        return cls._instance

    def __init__(self, nombre_db='biblioteca.db'):
        # Evita reinicialización si ya existe una instancia
        if not hasattr(self, 'conexion'):
            self.nombre_db = nombre_db
            self.conexion = None
            self.cursor = None
            self.conectar()
            self.crear_tablas()

    def conectar(self):
        """Establece la conexión con la base de datos y crea el cursor."""
        self.conexion = sqlite3.connect(self.nombre_db)
        self.cursor = self.conexion.cursor()

    def crear_tablas(self):
        """Crea las tablas necesarias si no existen."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Autor (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                nacionalidad TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Libro (
                isbn TEXT PRIMARY KEY,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                anio_publicacion INTEGER NOT NULL,
                autor_id INTEGER NOT NULL,
                cantidad INTEGER NOT NULL,
                FOREIGN KEY(autor_id) REFERENCES Autor(id)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                tipo_usuario TEXT NOT NULL,
                direccion TEXT NOT NULL,
                telefono TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Prestamo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                libro_isbn TEXT NOT NULL,
                fecha_prestamo TEXT NOT NULL,
                fecha_devolucion TEXT NOT NULL,
                FOREIGN KEY(usuario_id) REFERENCES Usuario(id),
                FOREIGN KEY(libro_isbn) REFERENCES Libro(isbn)
            )
        ''')
        self.conexion.commit()

    def cerrar(self):
        """Cierra la conexión con la base de datos."""
        if self.conexion:
            self.conexion.close()
            BaseDeDatos._instance = None  # Permite crear una nueva instancia después de cerrar