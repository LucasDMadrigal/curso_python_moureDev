### Strings ###

my_string = "Palalalala"
my_string_multiplicado = my_string*5

print(len(my_string))
print(len(my_string_multiplicado))

print((my_string))
print((my_string_multiplicado))

my_string_con_salto = "esto es un string \n \t con salto de linea"
my_string_con_tabulacion = " \t esto es un string con TABs"

print(my_string_con_salto)
print(my_string_con_tabulacion)

## Formateo de strings

name = "Lucas"
surname = "madrigal"
age = 30

print("Hola soy %s %s y tengo %d años" %(name, surname, age))
print("Hola soy {} {} y tengo {} años".format(name, surname, age))
print(f"Hola soy {name} {surname} y tengo {age} años")


### Desempaquetado de caracteres

a,b,c,d,e,f = "python"

print(a)
print(f)

my_other_string = "javascript"

string_slice = my_other_string[1:]
print(string_slice)

string_slice = my_other_string[:5]
print(string_slice)

string_slice = my_other_string[::-1]
print(string_slice)

string_slice = my_other_string[-2]
print(string_slice)

string_slice = my_other_string[-1]
print(string_slice)

print(my_other_string.capitalize())
print(my_other_string.count("a"))
print(my_other_string.encode())
print(my_other_string.upper())
print(my_other_string.upper().isupper())
print(my_other_string.upper().islower())
print(my_other_string.startswith("ja"))
print(my_other_string.startswith("je"))
print(my_other_string.startswith("JA"))