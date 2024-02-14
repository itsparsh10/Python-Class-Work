# lab question Another Day 
# 
# 
# 1
def max_value(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = int(input("Enter the value: "))
b = int(input("Enter the value: "))
c = int(input("Enter the value: "))

result = max_value(a, b, c)
print("Maximum value is:", result)

