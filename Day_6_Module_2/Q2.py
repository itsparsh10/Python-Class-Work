# Write a Python program to remove an empty tuple(s) from a list of tuples.
  #Sample Date: [(),(),('',),('a','b'),('a','b','c'),('d')]
  #Expected outcome: [('',),('a','b'),('a','b','c'),'d']




a=[(),('',),('',),('a','b'),('a','b','c'),('d')]
a.reverse()
a.pop()
print(a)
a.pop()
print(a)
  
