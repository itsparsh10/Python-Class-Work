# def print_diamond(n):
#     for i in range(n):
#         print(" " * (n - i - 1) + "*" * (2 * i + 1))
#     for i in range(n - 2, -1, -1):
#         print(" " * (n - i - 1) + "*" * (2 * i + 1))

# print_diamond(5)

def print_hollow_diamond(rows):
    for i in range(rows):
        for j in range(rows - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    
    for i in range(rows - 2, -1, -1):
        for j in range(rows - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_hollow_diamond(5)


