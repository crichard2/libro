#challenges

a = input("ejecutar ejercicio:")
a = int(a)
#1
if a == 1:
    path = "/iCloud Drive/universidad/9 semestre/Gramática española/I4 Gramática española.docx"
    print(path)
    with open(path,"r") as archivo:
     print(archivo.read())

#2
elif a==2:
    answer = input("Hola señor como se llama?")
    with open("ejercicio2","w") as archivo:
        archivo.write(answer)

#3

elif a==3:
    lista = [["top gun","risky business","minority report"],["titanic","the revenant","inception"],["training day","man on fire","flight"]]
    import csv
    with open("ej3.csv","w",newline='') as f:
        write = csv.writer(f,delimiter=",")
        write.writerow(lista[0])
        write.writerow(lista[1])
        write.writerow(lista[2])
