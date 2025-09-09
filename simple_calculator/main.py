# -*- coding: utf-8 -*-
import other as o
import paquete.modulo1 as modulo1
import re
from paquete import modulo1
from classes import *
from simple_calculator.classes.Libro import Libro
import numpy as np


class SimpleCalculator:

    def add(self, *args):
       return sum(args)



lista = [True, "hey"]

lista.insert(1, "yiji")
lista.append("heyy")
lista.extend([1, 2, 3])
lista.remove("heyy")
print(lista.index("hey"))
print(lista)
print(lista.count(1))
lista.reverse()
print(lista)


dict = {
    "cbro": "chey"
}

dict["bro"] = "hey"
dict["abro"] = "ahey"
print("bro" in dict.values())
print(dict)
print(list(dict.keys()))
print(list(dict.values()))

set = set([1, "bro"])
print(set)


x = 0
while(x < 5):
    print("eyoo")
    x+=1

for i in range(10, 100, 3):
    print(i)


cadena = "eyooooo"
iterador = iter(cadena)


print(next(iterador))

print(o.afunction())
print(modulo1.func_modulo_1())
print(help(modulo1))


libro = Libro("Don quijote")

print(libro.nombre)
print(libro.leer("comer"))
print(help(libro))


mensaje = "Que onda monda"
try:
    print(re.search("e", mensaje).start())
except:
    print(mensaje)
else:
    print(mensaje+"1")
finally:
    print(mensaje+"finally")

#raise TypeError("QUE ONDA BRO NO SE PUEDE CON ESTE TIPO INVERVE")



lista = [1, 2, 3, 4, 5]

result = [x**3 for x in lista if not x % 2 == 0]

dict = {key: value for key, value in zip(lista, result)}
other_dict = {x: x+1 for x in range(5) if x % 2 == 0}
print(result)
print(dict)
print(other_dict)


array = np.array([1, 2, 3, 4, "b"])
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(array)



