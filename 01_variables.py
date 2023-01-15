my_string_variable = "variables string"
my_int_variable = 5
my_complex_variable = 1 + 5j
my_string_variable = "variables string 2"

my_string_variable = False

print(my_string_variable)
print(type(my_string_variable))

print(my_int_variable)
print(type(my_int_variable))

print(my_complex_variable)
print(type(my_complex_variable))

#conversión a cadena de texto
my_complex_variable_to_string = str(my_complex_variable)

print(my_complex_variable_to_string)
print(type(my_complex_variable_to_string))

print("concatenando en print", my_complex_variable_to_string, my_complex_variable)

# Variables en una sola linea
name, surname, alias, age = "Lucas", "Madriguera", "el mocho", 30

print("Holis, mi nombre es", name, surname, ". Me dicen", alias, "y tengo", age)

#inputs

address = input("cual es tu direccion?")
print("tu direccion es:", address)