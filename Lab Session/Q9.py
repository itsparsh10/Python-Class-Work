# 4 Write a python function to reverse a string

def reverse(word):
    reversed_word = word[::-1]
    return reversed_word

user_input = input("Enter the string: ")
reversed_result = reverse(user_input)

print("Reversed string:", reversed_result)