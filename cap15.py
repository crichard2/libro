#capitulo 15: Bash

#bash es un comand line interface, todo lo que se escriba no corre en python sino en Terminal

#comandos:

#echo es como print

#ej.: echo Hello, World!

#se puede ejecutar python

#python 3

#para cerrar poner: exit()

#para saber en que direccion del pc estoy: pwd

#cambiar directorio: "cd" mas un path absoluto o relativo a la psocion donde estoy

#absoluto: parte con / desde el inicio hasta donde se encuentro
#relatio: parto sin / desde dodne estoy a donde quiero abrir

#para mostrar las direcciones en el lugar donde estoy: ls

#crear una nueva direccion: mkdir

#moverse para atras en un directorio: cd ..

#eliminar un directory: rmdir

#Flags: pueden ser True o False, por default todas parten false

#las flas modifican los comandos

# para ver el autor de una lista de archivos: ls -author
# para ver archivos ocultos: ls -a

#touch: comando para crear un archvo nuevo

#para crear un archivo oculto: poner un . antes del nombre usando touch

#pipes: "|"

#ej.: ls | less
#crea un archivo de texto con los nombres de lso directorios dentro

#variables:

# para referenciarlas se debe poner un signo $ antres

#ej:
#export x=100
#echo $x

