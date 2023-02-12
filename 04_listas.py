### listas ###

my_list = list()
my_other_list = [1,65,"lucas","daniel"]
var = 32165
print(len(my_list))
print(len(my_other_list))
print(my_other_list)

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])

my_other_list.append("ultimo elemento")
print(my_other_list)
my_other_list.insert(2,"inserto elemento en posicion")
print(my_other_list)
my_other_list.remove("inserto elemento en posicion")
print(my_other_list)

del my_other_list[2]
print(my_other_list)

# my_other_list.sort() ---/// esto no es posible por que no puede ordenar int y str
my_new_list = my_other_list[:5]
print(my_new_list)