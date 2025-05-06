min = 0
max = 0
i = 0
x = int(input())

while x != 0:
    if x <= min:
        min = x
    if x >= max:
        max = x
    x = int(input())
    i+=1
    if min == 0 or max == 0:
        print ("metti un altro input coglions")
    else:
        print ("min:", min, "max:", max)


