#cap 16: regular expresions

#para buscar una palabra en un archivo .txt

#primero crear una variable

#export GREP_OPTIONS='--color=always'

#despues, escribir en el terminal el comando grep mas lo que se busca y despues en archivo

#grep Beautiful zen.txt

#se puede usar el flag -i para ignorar las mayusculas

#grep -i beautiful zen.txt

#tambien se puede usar en python importando un modulo

import re

l = "Beautiful is better than ugly"

matches = re.findall("Beautiful",l)

print(matches)

matches = re.findall("beautiful",l,re.IGNORECASE)

print(matches)

#en el terminal: se pueden usar caracteres especiales para buscar patrones especificos en el texto

#grep ^If zen.txt

#lo de arriba buscará solo cuando if aparezca al principio de una linea

#grep idea.$ zen.txt

#lo de arruba buscara solo cuando idea. aparezca al final de una linea

#tambien se puede usar en python:

zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!
"""

m = re.findall("^If",zen,re.MULTILINE)
n = re.findall("idea.$",zen,re.MULTILINE)

print(m + n)

#otra forma de buscar patrones

#buscara si existe la palabra que parta con t y termine con o y tenga una o o una w entre medio

string = 'Two too.'

m = re.findall('t[ow]o',string,re.IGNORECASE)

print(m)

#buscar numero (en consola)

#grep [[:digit:]]

#en python

line = '123?34 hello?'

m = re.findall("\d",line,re.IGNORECASE)

print(m)

#asterisco * añade repeticiones

#echo two twoo not too. | grep -o two*

#usar punto para identificar cualquier cosa entre dos caracteres, buscará todos los que encuentre

#echo __hello__there | grep -o __.*__

#para que encuentre solo 1 ponemos __.*?__

#en python

t = "__one__ __two__ __three__"

found = re.findall("__.*?__",t)

for i in found:
    print(i)

text = """Giraffes have aroused
 the curiosity of __PLURAL_NOUN__
 since earliest times. The
 giraffe is the tallest of all
 living __PLURAL_NOUN__, but
 scientists are unable to
 explain how it got its long
 __PART_OF_THE_BODY__. The
 giraffe's tremendous height,
 which might reach __NUMBER__
 __PLURAL_NOUN__, comes from
 it legs and __BODYPART__.
"""


def mad_libs(mls):
    """
    :param mls: String
    with parts the user
    should fill out surrounded
    by double underscores.
    Underscores cannot
    be inside hint e.g., no
    __hint_hint__ only
    __hint__.
    """
    hints = re.findall("__.*?__",
                      mls)
    if hints is not None:
        for word in hints:
            q = "Enter a {}"\
                   .format(word)
            new = input(q)
            mls = mls.replace(word,
                              new,
                              1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("invalid mls")

mad_libs(text)

#para encontrar el signo $, y evitar que sea como ultimo en la linea

#echo I love $ | grep \\$

nueva = "I love $"

m = re.findall("\\%$",nueva,re.IGNORECASE)

print(m)


