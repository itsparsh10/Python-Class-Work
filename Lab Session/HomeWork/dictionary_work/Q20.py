# 3
a = str(input("Enter Your First String: "))
b = str(input("Enter Your Second String: "))

word_a = a.split()
word_b = b.split()

uncommon_words = []

for i in word_a:
    if i not in word_b and i not in uncommon_words:
        uncommon_words.append(i)

for i in word_b:
    if i not in word_a and i not in uncommon_words:
        uncommon_words.append(i)

print("The Uncommon Words are:", uncommon_words)