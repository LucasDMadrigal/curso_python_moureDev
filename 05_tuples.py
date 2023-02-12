### tuplas ###
# conjunto de valores

my_tuple = tuple()

my_tuple = (30, 1.87, "Lucas", "mochis")
print(my_tuple)

"""
en principio son lo mismo que las listas.

hasta ahora solo tenemos dos operaciones posibles,
index y count

si intento modificar un elemento de la tupla se rompe

en definitiva la tupla es inmutable, son valores constantes
"""

### para convertir una tupla a un array reasigno la variable

my_tuple = list(my_tuple)
print(my_tuple)