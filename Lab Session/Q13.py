# # 10 .wap function that checks weather a passed string is a palindrome or not
def palin(a):
    b=a[::-1]
    if b==a:
        print("String is a palindrome")
    else:
        print("String is not a palindrome")
a=input("Enter a string: ")
palin(a)

