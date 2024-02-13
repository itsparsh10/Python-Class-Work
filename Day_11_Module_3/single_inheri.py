# Q1

# class Parent:
#     def add(a,b):
#         print(" Sum :",a+b)
        
# class child(Parent):
#     def take_value():
#         c = int(input (" Enter the value of A :"))
#         d = int(input (" Enter the value of B :"))
#         Parent.add(c,d)
    
    
    
# c=child
# c.take_value()







# Alternative Way :
# class Parent:
#     def add(self ,a,b):
#         # print(" Sum :",a+b)
#         return a + b
        
# class child(Parent):
#     def take_value(self):
#         c = int(input (" Enter the value of A :"))
#         d = int(input (" Enter the value of B :"))
#         # Parent.add(c,d)
#         return self.add(c,d)
    
    
    
# c=child()
# e=c.take_value()
# print(e)







# Q2 : Area of circle

# class Parent:
#     def area(self ,r):
#         # print(" Area  :", 3.14*r*r)
#         return 3.14*r*r
        
# class child(Parent):
#     def take_value(self):
#         c = int(input (" Enter the value of Radius :"))
        
#         # Parent.add(r)
#         return self.area(c)
    
    
    
# c=child()
# e=c.take_value()
# print(e)








# Q3 : All Shapes Area


# class All_shape_area:
#     def reactangle (self,l,b):
#         return l*b
#     def triangle (self,b,h):
#         return 0.5*b*h
#     def circle (self,r):
#         return 3.14*r*r
#     def square (self,s):
#         return s*s
    
# class Result (All_shape_area):
#     def take_value_of_rectangle(self):
#         l=int(input(" Enter The value of length :"))
#         b=int(input(" Enter The value of Bridth :"))
#         return self.reactangle(l,b)
    
#     def take_value_of_triangle(self):
#         h=int(input(" Enter The value of Height :"))
#         b=int(input(" Enter The value of Bridth :"))
#         return self.triangle(h,b)
    
#     def take_value_of_circle(self):
#         r=int(input(" Enter The value of Radius :"))
        
#         return self.circle(r)
    
#     def take_value_of_square(self):
#         s=int(input(" Enter The value of Side:"))
        
#         return self.square(s)
    

# r=Result()
# z=r.take_value_of_rectangle()
# y=r.take_value_of_triangle()
# w=r.take_value_of_circle()
# k=r.take_value_of_square()
# print(z)
# print(y,"\n")
# print(w,"\n")
# print(k)





# Q4

class Shape:     
    def formula(self, shape, side, width, height, base):
        if shape.lower() == "square":
            area = side * side
        elif shape.lower() == "rectangle":
            area = side * width
        elif shape.lower() == "triangle":
            area = 0.5 * base * height
        else:
            area = "Invalid shape"
        return area  

class Working(Shape):
    def area(self):
        shape = input("Enter the shape (square/rectangle/triangle): ")

        if shape.lower() == "square":
            side = float(input("Enter the length of a side: "))
            return self.formula(shape, side, 0, 0, 0)
        elif shape.lower() == "rectangle":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            return self.formula(shape, length, width, 0, 0)
        elif shape.lower() == "triangle":
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            return self.formula(shape, 0, 0, height, base)
        else:
            return "Wrong input"

calculate = Working()
a = calculate.area()
print(a)
