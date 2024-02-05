# find the lcm of any two user entered number 
a=int(input("Enter your First Number :"))
b=int(input("Enter your Second  Number :"))
if a>b:
    c=a
else:
    c=b
while True:
    if c%a==0 and c%b==0:
        lcm=c
        break
    c+=1
print("LCM of",a,"and",b,"is",lcm)
    
    









