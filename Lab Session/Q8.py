# 3
def multiple(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
list = [59, 12, 13, 54, 75]
result = multiple(list)
print(result)  
