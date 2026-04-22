class Shapes:
    def area(self):
        pass

class Rectangle(Shapes):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print(self.length*self.width)
area_rectangle=Rectangle(int(input("Enter the length of the rectangle: ")),int(input("Enter the width of the rectangle: ")))
area_rectangle.area()
class Circle(Shapes):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(3.14*self.radius*self.radius)
area_circle=Circle(int(input("Enter the radius of the circle: ")))
area_circle.area()