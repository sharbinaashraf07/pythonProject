class Rectangle :
   def __init__(self,length,breadth):
     self.__length = length
     self.__breadth = breadth
     self.__area = length*breadth
   def __lt__(self, obj):
     if (self.__area<obj.__area):
        return "Rectangle 1 has larger area"
     else:
       return "Rectangle 1 does not have larger area"
rec1 = Rectangle(3,40)
rec2 = Rectangle(12,2)
print(rec1>rec2)
