n=int(input("enter the range "))
for i in range(1 , n+1):
    for b in range(n+1-i,1,-1):
        print(" ",end="")
    for a in range(0,2*i-1):
        print("*",end = "")
    for b in range(2*(n+1-i),1,-1):
        print(" ",end="")
    for a in range(0,2*i-1):
        print("*",end = "")
    
    print()

    
