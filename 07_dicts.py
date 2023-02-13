### dictionaries ###

my_dict = dict()
my_dict = {"nombre": "Lucas"}

user = {"Nombre":"Lucas", "Nacionalidad":"Argentina", "edad":30, "lenguajes":{"javascript", "python"}}

print("linea 7", user)

user["lenguajes"] = {"javascript", "python", "HTML"}


print("linea 8", user)

# print(user.items()) # un listado de tuples
# print(user.keys()) # retorna claves
print("values", user.values()) # retorna valores
# print(user.fromkeys("Nombre","Nacionalidad")) # {'N': 'Nacionalidad', 'o': 'Nacionalidad', 'm': 'Nacionalidad', 'b': 'Nacionalidad', 'r': 'Nacionalidad', 'e': 'Nacionalidad'}
# print(user.fromkeys(("Nombre","Nacionalidad"))) # {'Nombre': None, 'Nacionalidad': None} - crea un nuevo dict sin valores

# print(user.fromkeys(("Nombre","nacionalidad")))
my_new_dict = dict.fromkeys(user)
# print(my_new_dict)

my_new_dict = dict.fromkeys(user, ("Daniel", "Hungara", 30, {}))
# print(my_new_dict)