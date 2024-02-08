# wap to find the smallest and the largest values in the list

x=int(input(" Enter The Number of elements : "))
list=[]
for i in range(x):
    a=int(input(" Enter The Number : "))
    list.append(a)
print (list)
list.sort()
print("Smallest Number is :",list[0])
print("largest Number is :",list[x-1])


    
    
