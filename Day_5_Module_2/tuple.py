# Normal tuple
a=("apple","orange","cherry")
print(a[0])

# Tuple With If
if "orange" in a:
    print("Yes")
    
# check length
print(len(a))

# value count
a=("apple","orange","cherry","mango","banana","pineapple","apple","apple","apple")
print(a.count("apple"))

# start and stop (check between range)
a=("apple","orange","cherry","mango","banana","pineapple","apple","apple","apple")
print(a.index("apple",1,7))

