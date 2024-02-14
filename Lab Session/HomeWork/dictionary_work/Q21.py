# 4
z = int(input("Enter The Word/Int: "))

binary_digits = set([0, 1])

for digit in str(z):
    if int(digit) in binary_digits:
        print("It is Binary :)")
    else:
        print("It is not a binary digit.")

