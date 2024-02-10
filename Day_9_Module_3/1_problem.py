#Wap to count number of vowels in a given string, considering both uppercase and lower case


#WAP that takes a sentence a input and counts the no of words in it


#Wap to check if 2 string are anagrams of each others


#WAP that converts camelcase string to snake case


#Wap that takes a list of strings as input and sorts them based on their length.


# vovel="A","E","I","O","U"
# a=(str(input("Enter Char of Vovel")))
# for a in vovel:
#     print(a)





# Question 1 :
# vowel = ["A","E","I","O","U"]
# a = input("Enter the word : ")
# count = 0
# for i in a:
#     if i.upper() in vowel:
#         count+=1
# print(count)





# Question 3 :
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")

# string1 = string1.replace(" ", "").lower()
# string2 = string2.replace(" ", "").lower()

# if sorted(string1) == sorted(string2):
#     print(f"{string1} and {string2} are anagrams.")
# else:
#     print(f"{string1} and {string2} are not anagrams.")
    
    
    
# Question 4 :
# a = input("Enter  : ").split(" ")
# for i in range(0,len(a)):
#     str1 = ""
#     for j in range(0,len(a[i])):
        
#         if(a[i][j] == a[i][j].upper()):
#             if(j == 0):
#                 str1 += a[i][j]
#             else:
#                 str1 += a[i][j].lower()
#         else:
#             str1 += a[i][j]
    
#     a[i] = str1


# for i in a:
#     print(i="")










# Question 5 :
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)





