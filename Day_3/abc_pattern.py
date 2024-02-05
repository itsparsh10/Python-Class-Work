val=65
for i in range (1,4):
        val=65+i-1
        for j in range (i):
            print(" ",end='')
        for k in range (6-i):
            print(chr(val),end=' ')
            val+=1
        print()
        
# print()
# val=66
# for j in range (0, 4):
#         ch =chr(val)
#         print(ch,end=" ")
#         val=val+1
# print()
# val=67
# for k in range (0, 3):
#         ch =chr(val)
#         print(ch,end=" ")
#         val=val+1
# print()
