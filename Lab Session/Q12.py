# # 8 wap function function that accepts a string and counts the number of upper and lower case letters
def lucount(a):
    lcount=0
    ucount=0
    for i in a:
        if i.islower():
            lcount+=1
        else:
            ucount+=1
    print("Lower case letters:",lcount)
    print("Upper case letters:",ucount)
a=input("Enter a string: ")
lucount(a)
