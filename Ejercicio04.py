import sqlite3

database = sqlite3.connect("Telefonos.db")

cursor = database.cursor()

cursor.execute("SELECT * FROM Fabricante")
print ("Mostrando todos los fabricantes: ")
for registro in cursor:
    print (registro)

query = "UPDATE Fabricante SET Email = 'nuevoemail@apple.es' WHERE id = 1"
cursor.execute(query)
database.commit()

cursor.execute("SELECT * FROM Fabricante")
print ("Mostrando todos los fabricantes después de la modificación: ")
for registro in cursor:
    print (registro)

database.close()