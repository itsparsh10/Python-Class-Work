# #wap that forms a list of first characters of every word in another list
n=int(input("Enter number of elements: "))
lists=[]
list2=[]
for i in range(n):
    a=input("Enter word: ")
    lists.append(a)
print(lists)
for i in range(n):
    list2.append(lists[i][0])
print(list2)