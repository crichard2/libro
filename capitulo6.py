seccion = input("Ingresa el numero de la seccion a ejecutar:")
seccion = int(seccion)
if seccion == 1:
    #1.capitulo 6: manipulacion de strings

    hola = "hola"

    a = hola[0]
    b = hola[1]
    c = hola[-2]
    d = hola[-1]

    print (a+b+c+d)

    print(hola*3)

    print("me gusta la mazacaaaa".upper())
    print("EN VERDA NO TANTO".lower())
    print("me gusta la manzacaa".capitalize())

elif seccion == 2:
    #2.format, para crear nuevos strings

    print("Hemelelele {}".format("Yujin"))

    n1 = input("Ingresa un sustantivo:")
    v = input("Ingresa un verbo:")
    adj = input("Ingresa un adjetivo:")
    n2 = input("ingresa un sustantivo:")

    r = "El {} {} el {} {}".format(n1,v,adj,n2)
    print(r)

elif seccion == 3:
    #3.split se usa para separar strings en dos o mas strings

    banana_split="Hola Banana. Que tal".split(".")
    print(banana_split)

elif seccion == 4:
#4.join se usa para agregar nuevos caracteres entre cada caracter en un string

    joanna = "joaaana"
    resultado = "+".join(joanna)
    print(resultado)

    palabras = ["El ","perro ","se ","ilumino."]
    uno = "".join(palabras)
    print(uno)
    dos = "-".join(palabras)
    print(dos)

elif seccion == 5:
    #5. strip se usa para eliminar espacios
    s = "                jaja "
    s = s.strip()
    print(s)

    #replace, se usa para reemplazar
    animal = "Ya cama maca"
    animal = animal.replace("a","o")
    print(animal)

elif seccion == 6:
    #6. index se usa para determinar el indice en el que se encuentra un valor en el string
    arroz = "yo una vez vi television"
    indice1 = arroz.index(" ")
    indice2 = "arroz".index("z")
    print(indice1,indice2)
    try:
        "arroz".index("w")
    except:
        print("Not found.")

    # in , para ver si el string esta dentro del string
    print("Tangananica" in "Tanganana","Todo lo explica" not in "no explica na")

elif seccion == 7:
    #7. se usa \ para poder usar comillas dentro de comillas
    print("Ella dijo \"Si como no.\"")
    # se usa \n para saltar a otra linea
    print("-No-\n-Que dices?-\n-Que no-")

elif seccion == 8:
    #8. slicing, seleccionar una parte
    lista = [1,2,3,4,5,6,7]
    print(lista[0:2])
    print("Habia una vez truz"[0:5])
    print("Habia una vez truz"[:5])
    print("Habia una vez truz"[5:])
    
else:
    print("no existe esa seccion")
