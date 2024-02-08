#wap to print index at which a particular value exists. if the value exists at multiple locations in the list, then print all the indices. also count number of times the value is repeated in the list.
search=int(input("Enter number of elements: "))
list=[]
flag=0
for i in range(search):
    a=int(input("Enter element: "))
    list.append(a)
print(list)
b=int(input("Enter element to search for: "))
for i in range(search):
    if list[i]==b:
        flag+=1
        print("Index:",i)
print("\nCount:",flag)
