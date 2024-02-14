# # 9 .wap function to check weather a number is perfect or not
def perfect(a):
    total=0
    for i in range(1,a):
        if a%i==0:
            total+=i
    if total==a:
        print(a,"is a perfect number")
    else:
        print(a,"is not a perfect number")
a=int(input("Enter a number: "))
perfect(a)
