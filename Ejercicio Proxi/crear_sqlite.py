import sqlite3

conn = sqlite3.connect('Ejercicio Proxi/usuarios.db')
cursor = conn.cursor()

# Crear tabla de usuarios si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        usuario TEXT PRIMARY KEY,
        contraseña TEXT
    )
''')

# Crear tabla de estructura de archivos si no existe
cursor.execute('DROP INDEX IF EXISTS idx_unique_usuario')

# Modificar la tabla "sesiones" eliminando la restricción única en "usuario"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sesiones (
        usuario TEXT,
        hora_inicio_sesion TEXT,
        FOREIGN KEY (usuario) REFERENCES usuarios(usuario)
    )
''')

# Agregar un índice normal (no único) si es necesario
cursor.execute('CREATE INDEX IF NOT EXISTS idx_usuario ON sesiones(usuario)')

conn.commit()
conn.close()


