class Rectangle:
    def __int__(self,length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return (self.length*self.breadth)
    def perimeter(self):
        return(2*(self.length+self.breadth))

r1 = Rectangle(2,8)
r2 = Rectangle(4,9)
print(r1.area())
print(r2.area())
print(r1.perimeter())
print(r2.perimeter())
a1=r1.area()
a2=r2.area()
if(a1>a2):

   print("first rectangle is bigger tha second")
else:
   print("second rectangle is bigger than first")

