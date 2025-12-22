
#Using append to add an element to the end of the list
# Primeiro, você precisa criar as listas
list_a = []
list_names = []

# Agora você pode usar o append
list_a.append(99)
list_names.append("Hannah")

# Verificando o resultado
print(list_a)  
print (list_names)    

#Join two list ( using extends)
prime_numbers = [2, 3, 5]
print ("Prime Numbers:", prime_numbers)
even_numbers = [2, 4, 6]
print ("Even Numbers:", even_numbers)
 
prime_numbers.extend(even_numbers)
print("list after append:", prime_numbers)

#Change List Items  
languges = ["Python", "Java", "C++", "JavaScript"]
print("Original List:", languges)   
languges[1] = "Ruby"
print("List after changing an item:", languges)     
#Insert Items

languges.insert(2, "C#")
print("List after inserting an item:", languges)     
#Remove List Items
languges.remove("C++")
print("List after removing an item:", languges)     
#Pop Items
popped_item = languges.pop(3)
print("Popped item:", popped_item)
print("List after popping an item:", languges)     
#Clear the List
languges.clear()
print("List after clearing all items:", languges)           
#You can also use del to remove an item at a specific index
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)     
del numbers[2]
print("List after deleting an item:", numbers)  