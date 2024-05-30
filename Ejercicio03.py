import sqlite3
database = sqlite3.connect("Telefonos.db")
cursor = database.cursor()

cursor.execute("SELECT * FROM Fabricante")
for registro in cursor:
    print ("Mostrando  todos los teléfonos del fabricante: ", registro[1])
    cursortelefonos = database.cursor()
    parametro = (registro[0],)
    cursortelefonos.execute("SELECT NombreModelo, MemoriaRAM, CamaraMPixeles, VersionSO FROM Telefono where FabricanteId = ?", parametro)
    for registrotelefono in cursortelefonos:
        print (registrotelefono[0], ", ",registrotelefono[1], ", ",registrotelefono[2], ", ",registrotelefono[3])

database.close()