num=int(input("Enter Your Number 1 :"))
num2=int(input("Enter Your Number 2 :"))
for i in range(num,num2):
    for j in range(65,i+1):
        print(chr(j),end="")
    print()