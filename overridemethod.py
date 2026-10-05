class Shape:
    def area(self):
        print("Area of shapes")

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
       print(3.14*self.radius*self.radius )

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(self.length*self.breadth)

class Triangle(Shape):
        def __init__(self,base,height):
            self.base = base
            self.height = height

        def area(self):
            print(0.5*self.base*self.height)

c1 = Circle(5)
r1 = Rectangle(15,25)
t1 = Triangle(5,20)

c1.area()
r1.area()
t1.area()
            