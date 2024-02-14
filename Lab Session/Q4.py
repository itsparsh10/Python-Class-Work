# Q4 - 4,Wap to compare two dictionaries in Python?  (By using == operator)
#  i/p:  r1={'id':101,'name':'Amit','Age':21}
#        r2={'id':101,'name':'Amit','Age':21}
#        r3={'id':101,'name':'raheel','Age':26}

r1={'id':101,'name':'Amit','Age':21}
r2={'id':101,'name':'Amit','Age':21}
r3={'id':101,'name':'raheel','Age':26}
if r1==r3:
    print(r1)
    print(r3)
elif r2==r3:
    print(r2)
    print(r3)
else:
    print(r1)
    print(r2)