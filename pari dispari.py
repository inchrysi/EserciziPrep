pari = 0
dispari = 0
i = 1

x = int(input())

while i < 10:
    if x % 2 == 0:
        pari = pari + 1
    else:
        dispari = dispari + 1
    x = int(input())
    i+= 1

print ("Pari:", pari, "Dispari:", dispari) 