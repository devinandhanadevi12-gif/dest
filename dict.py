dict= {"name":"Alice", "age":30, "city":"New York","height":160.5,"sem":"True"} #dictionary variable
print(dict)
print(dict["name"]) #accessing the value of the key "name"     
print(dict["age"]) #accessing the value of the key "age"
print(dict["city"]) #accessing the value of the key "city"
dict["age"]=31 #modifying the value of the key "age"
print(dict) #printing the modified dictionary
dict.pop("height") #removing the key "height" from the dictionary
print(dict) #printing the modified dictionary