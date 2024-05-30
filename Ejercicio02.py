import sqlite3
database = sqlite3.connect("Telefonos.db")
cursor = database.cursor()

cursor.execute("SELECT * FROM Telefono")
print ("Mostrando todos los teléfonos: ")
for registro in cursor:
    print (registro)

database.close