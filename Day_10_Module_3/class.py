class Student:
    # class veriable : becoz it is not define in any function
    count=0
    # constructor
    # 
    def __init__(self,name,age):
      # obj.name
      self.name=name
      self.age=age
      Student.count+=1
    
    def display(self):
      print("name :" , self.name )
      print("age :" , self.age)

obj = Student("xyzqwe" ,300)
obj1 = Student("xyz" ,30)
obj.display()
obj1.display()

print(Student.count)


        
