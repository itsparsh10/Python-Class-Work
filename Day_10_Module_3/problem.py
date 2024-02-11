class College:
    count=0
    def getData(self,i):
        for n in range(i):
          
          self.name = str(input("Enter Your name: "))
          self.age = int(input("Enter your age: "))
          self.address = str(input("Enter your address: "))
          College.count+=1
          print
          self.department =input("Which Department Do you Want : B-Tech / Pgdm :")
          if self.department == "B-Tech":
            self.department="B=Tech"
          else:
            self.department="Pgdm"
        
         

    def setData(self,x):
        for i in range(x):
            print(self.department)
            
            print("Your Name Is:", self.name)
            print("Your Age:", self.age)
            print("Your Address:", self.address)
            print(str.sort(self.department))
            
        
            
        

obj = College()
a=int(input("No. of Students: "))
obj.getData(a)
obj.setData(a)
print("Num is :" , College.count)







# class Student:
#     count = 0
#     def getData(self,i):
#         for n in range(i):
#             self.name=input("Enter your Name: ")
#             self.roll=input("Enter your Roll no.: ")
#             self.age=input("Enter your Age: ")
#             Student.count+=1
#             self.department =input("Which Department Do you Want : B-Tech / Pgdm")
#             if self.department == "B-Tech":
#                 self.department="B=Tech"
#             else:
#                 self.department="Pgdm"
#     print()
#     def setData(self,x):
#         for i in range(x):
#             print("Name:",self.name)
#             print("Roll no.:",self.roll)
#             print("Age:",self.age)

# s=Student()
# a=int(input("Enter Number of Students Is : "))
# s.getData(a)
# s.setData(a)
# print(Student.count)

       
       
      