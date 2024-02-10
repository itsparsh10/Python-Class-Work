# composition
# import math

# def dist ( x1,y1,x2,y2):
#     dist_x1 = abs(x1-x2)
#     dist_x2 = abs(y1-y2)

#     distance = math.sqrt((dist_x1*dist_x1) + (dist_x2*dist_x2))
#     print("Distance : ",dir())
#     return distance


# def cirumference(x1,y1,x2,y2):
   
#     r = dist(x1,y1,x2,y2)
#     print("Circle : ",dir())
#     return ((22/7)*r*r)


# print(f"{cirumference(0,0,4,6)}")




def fact(num):

    if(num < 0):
        return "We don't perform for negative values"
    
    if(num<2):
        return 1
    
    else:
        factorial = num * fact(num-1)
        return factorial

n = 1.2

while(not(int(n) == n)):
    try:
        n = int(input("Enter the num : "))
    except:
        print("We take input as integer only")

    
print(fact(n))