class triangle:
    def __init__(self):
        self.a = int(input('Enter first side of the triangle: '))
        self.b = int(input('Enter second side of the triangle: '))
        self.c = int(input('Enter third side of the triangle: '))

    def perimeter(self):
        print(self.a + self.b + self.c)
    
    def area(self):
        self.s = (self.a + self.b + self.c)/2
        print((self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c)) ** 0.5)

tri = triangle()
tri.perimeter()
tri.area()