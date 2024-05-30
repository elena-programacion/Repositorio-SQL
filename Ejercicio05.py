import sqlite3

database = sqlite3.connect("Telefonos.db")

cursor = database.cursor()

cursor.execute("SELECT * FROM Telefono")
print ("Mostrando todos los teléfonos: ")
for registro in cursor:
    print (registro)

query = "UPDATE Telefono SET VersionSO = 'iOS 15' WHERE VersionSO = 'iOS 14'"
cursor.execute(query)
database.commit()

cursor.execute("SELECT * FROM Telefono")
print ("Mostrando todos los teléfonos después de la modificación: ")
for registro in cursor:
    print (registro)

database.close()