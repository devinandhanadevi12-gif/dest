class person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age # private property
p1=person("Alice",30)
print(p1.name) #accessing the public attribute name 
print(p1._person__age) #accessing the private attribute age (will raise an error)