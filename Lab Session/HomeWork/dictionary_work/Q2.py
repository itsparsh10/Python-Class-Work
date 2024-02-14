# Q 2
#Wap for accessing elements from a dictionary. i/p: r1={'id':101,'name':'Amit','Age':21}
#   a. By using key name.
#   b. By using get() method.

R={'id':101,'name':'Amit','Age':21}
print("Accessing elements using key name:")
print("ID:", R['id'])
print("Name:", R['name'])
print("Age:", R['Age'])
print("Accessing elements using get() method:")
print("ID:", R.get('id'))
print("Name:", R.get('name'))
print("Age:", R.get('Age'))
print("Accessing a key that doesn't exist using get() with a default value:")
print("Gender:", R.get('Gender', 'Not specified'))

