# wap that scans an email adress  and forms a tuple of user name and domain
# for e in range (5):
#     print
# # e=str(input("Enter 5 Email Id)"))

# b=(e.split("@"))
# c=(b[0])
# d=(b[1])
# print("User Name :",c)
# print("Domain : ",d ,"\n")


email=int(input("Enter number of email"))
for i in range(0,email):
    x=str(input("Enter your email address: ")).split("@")
    s=(x[0])
    d=(x[1])
    print('Username :',s)
    print('Domain :',d)

