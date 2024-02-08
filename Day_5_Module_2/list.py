# list is muatable

# to demonstrate different methords of list
# Step.1 - Make a list 
x=[1,"Hello world","Ipl",986]
print(x)

# Method 1 - Extand the value 
x.append(12)
print(x)

# Method 2 - Put the value in a list
x.extend([10,11])
print(x)

# Method 3 - Pop - in pop you need to mantion the position of removed values
x.pop(4)
print(x)

# Method 4 - Reverse the values
x.reverse()
print(x)

# Method 5 - x.insert(i,item) - Exchange the value
x.insert(0,5)
print(x)

# Method 6 - x.remove(item) - give the element and find then remove it 
x.remove(986)
print(x)

# Method 7 - x.sort() - sort the values
x.sort(reverse=True)
print(x) 

x.sort()
print(x) 

