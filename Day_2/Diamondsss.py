# num=int(input("Enter Number of Rows"))
# for i in range(1,num+1):
#     for j in range(num , i ,-1):
#         print(" ",end='')
#     for k in range(2*i-1):
#         print("*",end='')
#     print()
# for i in range(0,num):
#     for j in range(i ):
#         print(" ",end='')
#     for k in range(2*(num-i)-1):
#         print("*",end='')
#     print()
    
    
    
num=int(input("Enter Number of Rows"))
for i in range(1,num+1):
    for j in range(num , i ,-1):
        print(" ",end='')
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print("*",end='')
        else:
            print(" ",end='')
    print()
for i in range(0,num):
    for j in range(i ):
        print(" ",end='')
    for k in range(2*(num-i)-1):
        if k==0 or k==2*(num-i)-2:
            print("*",end='')
        else:
            print(" ",end='')
    print()
    
    

    
    