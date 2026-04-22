class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        return f"Hi, I'm {self.name} and I am {self.age} years old."
    def __repr__(self):
        return f"Person(name='{self.name!r}', age={self.age!r})"
p1 = Person("Alice",30)
p2 = Person("Bob",25)

print(p1)
print(p1.greet())
print(p2.name,p2.age)