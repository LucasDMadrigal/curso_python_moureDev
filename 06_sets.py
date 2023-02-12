### Sets ###
"""

Un set no es una estructura ordenada de elementos.

"""

my_set = set()  ## tipo de dato como tal
my_other_set = {} ## tipo dict - estructura clave valor

my_other_set = {"nombre":"Lucas","coso":"coso", "edad_ya_quiere": 28}
my_other_set = {"Lucas","coso", 28} ## tipo set

print(type(my_other_set))
print((my_other_set))

my_other_set = {"Lucas","coso", 28} ## tipo set

my_other_set.add("Lucas")
print((my_other_set)) ## esto no modifica nada

my_other_set.add("Daniel")
print((my_other_set)) ## esto si