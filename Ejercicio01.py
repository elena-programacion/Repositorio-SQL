 cimport sqlite3

database = sqlite3.connect("Telefonos.db")

#fabricante01 = (1, "Apple", "912345678", "Puerta del Sol 1, Madrid", "info@apple.es")
#print ("Registro a insertar: ", fabricante01)
#fabricante = (2, "Xiaomi", "999888777", "Centro Comercial de la Gavia", "hola@xiaomi.com")
#print ("Fabricante a insertar: ", fabricante)

cursor = database.cursor()
#cursor.execute("INSERT INTO Fabricante VALUES(?,?,?,?,?)", fabricante01)
#cursor.execute("INSERT INTO Fabricante VALUES(?,?,?,?,?)", fabricante02)

database.commit()
#print("Registro insertado")

telefono01 = (1, 1, "iPhone 12", 128,4.20,"iOS 14")
print("Teléfono a insertar: ", telefono01)
telefono02 = (2, 1, "iPhone XR", 512,6.30,"iOS 14")
print("Teléfono a insertar: ", telefono02)
telefono03 = (3, 2, "RedMi Note 9", 128,4.20,"Android 9")
print("Teléfono a insertar: ", telefono03)
telefono04 = (4, 2, "Mi 10", 128,4.20,"Android 10")
print("Teléfono a insertar: ", telefono04)

cursor.execute ("INSERT INTO Telefono VALUES(?,?,?,?,?,?)", telefono01)
cursor.execute ("INSERT INTO Telefono VALUES(?,?,?,?,?,?)", telefono02)
cursor.execute ("INSERT INTO Telefono VALUES(?,?,?,?,?,?)", telefono03)
cursor.execute ("INSERT INTO Telefono VALUES(?,?,?,?,?,?)", telefono04)

database.commit()
print("Teléfonos insertados")

database.close()