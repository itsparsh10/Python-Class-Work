# nested Tuple 
# wap to print the name of the topper and his/her marks in for subjects where in the marks are specifed as a list in the tuple topper
# topper=str(input("Enter Student Name :"))
# Mark_1=int(input("Enter Your Mark :"))
# Mark_2=int(input("Enter Your Mark :"))
# Mark_3=int(input("Enter Your Mark :"))
# Mark_4=int(input("Enter Your Mark :"))
# sum=0
# if sum>100:
#     print("avg")
# elif sum>200:
#     print("avg2")
n = ""
topper = (0,)
while(n != "0" ):
    l = []
    n = input("Enter the name of topper (0 to exit)")
    if(n != "0"):
        for i in range(1,5):
            a = int(input(f"Enter marks for sub {i} : "))
            l.append(a)

        topper+=((n,l))
max = 0
index = 0
for i in range(2,len(topper) , 2):
    sum = 0
    for j in topper[i]:
        sum += j

    if(sum>max):
        max = sum
        index = i
        
t = (topper[index-1] , topper[index])
print(t)

    

