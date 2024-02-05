val=65
for i in range (1,4):
        val=65+i-1
        for j in range (i):
            print(" ",end='')
        for k in range (6-i):
            print(chr(val),end=' ')
            val+=1
        print()
        
