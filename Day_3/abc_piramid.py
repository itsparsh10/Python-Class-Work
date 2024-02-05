#pentagon alphabetical pattern
val=65
for i in range(1,3):
    val=65-i+3
    for j in range(3,i,-1):
        print(" ",end='')
    for k in range(1,i+3):
        print(chr(val),end=' ')
        val+=1
    print()
val=65
for i in range(3,6):
    val=(65+i-3)
    for j in range(i-3):
        print(" ",end='')
    for k in range(8-i):
        print(chr(val),end=' ')
        val+=1
    print()