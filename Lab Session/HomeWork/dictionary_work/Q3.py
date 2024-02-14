#Q 3
# Wap for removing element from a dictionary.  
#     i/p:  record={'id':101,'name':'Amit Kumar','Age':21}
#     1.By Using Del Keyword.
#     2.By using pop.

record={'id':101,'name':'Amit Kumar','Age':21}
del record ['name']
print (record)
record.pop('id')
print (record)
