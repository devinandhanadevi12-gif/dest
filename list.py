list = ["apple", "banana", "cherry"] #list variable
print(list)
print(list[0]) #accessing the first element of the list
print(list[1]) #accessing the second element of the list    
print(list[2]) #accessing the third element of the list
list[2] = "orange" #modifying the third element of the list
print(list) #printing the modified list
list.append("grape") #adding a new element to the end of the list
print(list) #printing the modified list
list.insert(1, "kiwi") #inserting a new element at index 1
print(list) #printing the modified list
list.remove("banana") #removing an element from the list
print(list) #printing the modified list
list.pop(1) #removing the last element from the list
print(list) #printing the modified list