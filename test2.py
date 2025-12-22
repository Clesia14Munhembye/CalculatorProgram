#list empty

my_list = set()

print ("empty list:" , type (my_list) )

# append elements

my_list = [10, 34, 54, 12]
my_list.append(15)
print ("insert Value upgrade:" , my_list)

#using extend, join

my_list = [10, 34, 54, 12]
print ("print my firt list:" , my_list)

my_list2 = [50, 60, 70]
print ("print my second list:" , my_list2)
#join two list
my_list.extend(my_list2)

print (my_list)

del(my_list[-1])
print(my_list)

#print in ascending order
my_list.sort()
print(f"Lista ordenada: {my_list}")


#index of value 30
my_list = [10, 30, 34, 54, 12]
indice = my_list.index(30)
print(f"O índice do valor 30 é: {indice}")