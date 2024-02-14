# 6
class Employee:
    def __init__(self,id,name,gender,city,salary):
        self.ID=id
        self.Name=name
        self.Gender=gender
        self.City=city
        self.Salary=salary
        
        print(f"My Id is {id}\n My Name {name}\n Gender {gender}\n  City Is : {city}\n  Salary : {salary}")
        
s=Employee(1,"Pankaj","Male","Delhi",55000)
s.__init__