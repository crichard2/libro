#capitulo 5: contenedores

#metodos:funciones relacionadas con ciertos tipos de datos
print("hello".upper())
print("hello".replace("h","!")

#listas: contenedor que guarda objetos en un orden especifico

#formas de crear listas
lista1 = list()
lista2 = []
      
#agregar un elemento al final lista.append("elemento")
lista1.append("fruta")

#pueden guardar cualquier tipo de dato, y al mismo tiempo

lista2 = [True, 100, 1.1, "fruta"]

#eliminar el ultimo elemento de la lista lista.pop()
#se pueden combinar dos listas sumandolas lista1+lista2

print(lista1+lista2)

#verificar si existe un elemento en la lista con "elemento" in lista o si no esta con "not in"

print("fruta" in lista2)
print("amalacatantan" not in lista2)

#largo de una lista con len(lista)

print(len(lista2))

#tuplas: contenedor que guarda objetos en un orden especifico, pero son innmutables (su contenido no puede cambiar)

#formas de crear tuplas

tupla1 = tuple()
tupla2 = ()

tupla1 = ("callampin",)

#se puede recuperar un elemento de la tupla igual que de una lista, pero no se puede cambiar
# se puede revisar si un elemento esta en la tupla con "in" o si no esta con "not in", igual que en las listas

#diccionarios: contenedores que usan una "key" para acceder a otro valor que llamamos "value"

#formas de crear diccionarios

diccionario1 = dict()
diccionario2 = {}

#agregar pares key-value

diccionario = {"manzana":"verde","platano":"amarillo"}

#los valores son  mutables pero las key no, las llaves pueden ser un string o tupla, pero no una lista o un diccionario
      

hechos = dict()
hechos["codigo"] = "perkin"
hechos["codigo"]
hechos["fundador"] = 1776

#"in" se puede usar para buscar una key en un diccionario, pero no un valor

#borrar un par key.value con la keyword del

del diccionario["manzana"]

#se pueden guardar listan en listas
