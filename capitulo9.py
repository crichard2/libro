#capitulo 9: archivos

#en vez de escribir la direccion, mejor usar la funcion path del modulo os, para juntar los nombres de las carpetas
#asi vana  funcionar sin importar el sistema operativo donde se corran

import os

os.path.join("Users","bob","st.txt") #ojo que falta algo que poner antes que User

# r obre archuvos solo para leer
# w abre archvios solo para escribir, los sobreescribe si ya existen
# w+  abre archivos para leer y escribiry, sobreescribe el archvio si ya existe

#se debe cerrar un archivo con close despues de abirlo

st = open("nuevo_archivo.txt","w")
st.write("Hola desde python")
st.close()

#para cerrarlo automaticamente se puede usar

with open("otro_archivo","w") as f:
    f.write("Hi from python")

#leyendo archivos

with open("otro_archivo","r") as f:
    print(f.read())

my_list = list()

with open("otro_archivo","r") as f:
    my_list.append(f.read())
print(my_list)

# archivos CSV, terminan en .csv, comma separeted values
# cada dato separado por una coma o una linea certival representa una cell
# cada linea represena una fila

import csv

with open("st.csv","w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(["one","two","three"])
    write.writerow(["four","five","six"])

with open("st.csv","r") as f:
    r = csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))
