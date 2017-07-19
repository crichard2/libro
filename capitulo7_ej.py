#desafios

#1
lista = ["the walking dead","the sopranos","the vampire diaries"]
for i in lista:
    print(i)

#2

for i in range(25,51):
    print(i)

#3
i = 0
for show in lista:
    print(show,i)
    i += 1

#4

while True:
    print("type q to quit")
    a = input("adivina un numero")
    numeros = [1,2,3,4,5,6,7,8,9,11]
    if a == "q":
        break
    elif int(a) in numeros:
        print("correcto, uno de mis numeros es "+a+".A ver si adivinas otro saco wea.")
    elif int(a) not in numeros:
        print("Incorrecto")

#5

lista1 = [8,19,148,4]
lista2 = [9,1,33,83]
mult = []
for i in lista1:
    for j in lista2:
        mult.append(j*i)
print(mult)

