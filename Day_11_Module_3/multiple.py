# In this inheritence there is 2 parent class and 1 child class
# class LU:
#     subject=["Python Zero To Hero"," Cloud Computing "," AR/VR Zero to Hero ","21 Din Paisa Double"]
#     teacher=["Sai Sir","Prasad Sir","Nidhi Mam"," Swpnil Sir "]
#     duration=["55 Min","60 Min","90 Min"]
# class ITM:
#     subject=[" PGDM ","B-Tech"]
#     teacher=[" Any Teacher "," Sumit Sir "]
#     duration=["Matpucho","Jubtak Man Karta Hai Tub Tak Padhate Hai"]
# class BTech(LU,ITM):
#     print("LU Course are in \n")
#     a=LU.subject
#     j=1
#     for i in range(len(a)):
#         print(j,LU).subject
#         j+=1
        

class LU:
    subjects=["AI/ML","AR/VR","Cloud Computing","Full Stack Developer"]
    teachers=["Sai Sir","Swapnil Sir","ABC","XYZ"]
    duration=["60 days","30 days","50 days","55 days"]
class ITM:
    subjects=["Hotel management","BTECH CSE","Design","Business"]
    teachers=["abc","sumit sir","xyz","qwer"]
    duration=["90 days","120 days","60 days","30 days"]
class Btech(LU,ITM):
    print("LetsUpgrade courses are:\n")
    a=LU.subjects
    j=1
    for i in range(len(a)):
        print(j,LU.subjects[i],"by",LU.teachers[i],"for",LU.duration[i])
        j+=1
    c=[]
    d=int(input("How many subjects you want to select: "))
    for i in range(d):
        e=int(input("Select your interested course: "))
        c.append(e)
    print("\nITM courses are:\n")
    j=1
    b=ITM.subjects
    for i in range(len(b)):
        print(j,ITM.subjects[i],"by",ITM.teachers[i],"for",ITM.duration[i])
        j+=1
    f=[]
    d=int(input("How many subjects you want to select: "))
    for i in range(d):
        e=int(input("Select your interested course: "))
        f.append(e)
    j=1
    print("\nYour selected courses are :\n")
    for i in range(len(c)):
        print(j,LU.subjects[i],"by",LU.teachers[i],"for",LU.duration[i])
        j+=1
    for i in range(len(f)):
        print(j,ITM.subjects[i],"by",ITM.teachers[i],"for",ITM.duration[i])
        j+=1




# class LU:
#     subject=["Python Zero To Hero"," Cloud Computing "," AR/VR Zero to Hero ","21 Din Paisa Double"]
#     teacher=["Sai Sir","Prasad Sir","Nidhi Mam"," Swpnil Sir "]
#     duration=["55 Min","60 Min","90 Min"]
# class ITM:
            
#     subject=[" PGDM ","B-Tech"]
#     teacher=[" Any Teacher "," Sumit Sir "]
#     duration=["Matpucho","Jubtak Man Karta Hai Tub Tak Padhate Hai"]
# class BTech(LU,ITM):
#     def 
