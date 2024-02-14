# 2
# Write a python function to sum all numbers in a list

def calculate_sum():
    sum = 0
    for i in range(1, 11):
        sum += i
        print(i)  

    return sum

result = calculate_sum()
print("The sum is:", result)
