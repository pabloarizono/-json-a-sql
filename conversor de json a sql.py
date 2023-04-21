import sqlite3
import json


with open('archivo.json') as f:
    data = json.load(f)
    # Aca seleccionamos el archivo json a insertar en db

# aca hago la coneccion a la bd sql
conn = sqlite3.connect('datos.db')
c = conn.cursor()

# Creo una tabla n caso de que no exista..
c.execute('''CREATE TABLE IF NOT EXISTS datos
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre TEXT,
             edad INTEGER,
             ciudad TEXT)''')

#aca a modo de ejemplo inserto los datos:(persona['nombre'], persona['edad'], persona['ciudad'])) 
# del archivo json a la  bdatos
for persona in data:
    c.execute("INSERT INTO datos (nombre, edad, ciudad) VALUES (?, ?, ?)",
              (persona['nombre'], persona['edad'], persona['ciudad']))

# Guardar cambios  y cierro conexion
conn.commit()
conn.close()