import sqlite3
con = sqlite3.connect("inventario2.db")

print("Conexión establecida exitosamente.")


cur = con.cursor()

cur.execute('''
CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    categoria TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL
)
''')

print("Tabla productos creada exitosamente.")

con.close()

print("Tabla productos fue cerrada exitosamente.")
