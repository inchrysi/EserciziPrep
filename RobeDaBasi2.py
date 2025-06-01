import random

# CREA SEQUENZA ===============================
def creaSeq(n):
    lista = []
    
    for i in range(n):
        x = random.randint(1,4)
        if x == 1:
            lista.append('a')
        if x == 2:
            lista.append('t')
        if x == 3:
            lista.append('c')
        if x == 4:
            lista.append('g')
            
    print('Ecco il tuo filamento:', lista)
    
    return lista

# CERCA PATTERN =============================== da rivedere
def searchPattern1(filamento, pattern): #senza conversioni
    lfil = len(filamento)
    lpatt = len(pattern)
    found = 0
    pos = []
    diff = lfil - lpatt
    
    if diff >= 0:
        for i in range(lfil - lpatt + 1): #
            n = i + lpatt
            if filamento[i : n] == pattern:
                found+=1
                pos.append(i)
    else:
        print('Pattern più lungo di seq')
        return
    
    if found != 0:
        print('Il pattern si ripete', found, 'volte')
        print('Si trova in posizione:', pos)
    
    else:
        print('non si ripetono i pattern')
                
    return


def searchPattern2(filamento, pattern): #con conversioni str a lista
    robino = list(pattern)
    lfil = len(filamento)
    lpatt = len(robino)
    found = 0
    pos = []
    diff = lfil - lpatt
    
    if diff > 0:
        for i in range(lfil):
            n = i + lpatt
            if filamento[i : n] == robino:
                found+=1
                pos.append(i)
    
    if found != 0:
        print('Il pattern si ripete', found, 'volte')
        print('Si trova in posizione:', pos)
    
    else:
        print('non si ripetono i pattern')
                
    return

# PERCENTUALE DI MATCH ==============================
def matchPercent(fil1, fil2):
    l1 = len(fil1)
    l2 = len(fil2)
    size = 0
    match = 0
    diff = abs(l1-l2)
    
    if l1 < l2:
        size = l1
    else:
        size = l2
    
    for i in range(size):
        if fil1[i] == fil2[i]:
            match+= 1
            
    if diff != 0:    
        percMatch = (match * 100) / (size + diff)
    else:
        percMatch = (match * 100) / size
        
    return percMatch

# PULIRE FILAMENTO =================================
def cleanSeq1(filamento): #con ASCII cuz my bb said so <3
    l = len(filamento)
    errori = 0
    lista = []
    basi = ['a', 't', 'c', 'g']
    
    for i in range(l):
        if filamento[i] not in basi:
            filamento.pop(i)
            errori+= 1
        correct = chr(ord(filamento[i]) - 32)
        lista.append(correct)
        
    return lista
    
def cleanSeq2(filamento): #con py string methods
    l = len(filamento)
    basi = ['a', 't', 'c', 'g']
    lista = []
    
    for i in range(l):
        if filamento[i] not in basi:
            filamento.pop(i)
        
        correct = filamento[i].upper()
        lista.append(correct)
    
    return lista

# GENERA FILAMENTO PALINDROMO !!! ======================


# FILAMENTO PALINDROMO ??? =============================
def palindromeSeq(filamento):
    l = int(len(filamento))
    half = int(l/2)
    
    if l%2 == 0:
        p1 = filamento[0 : half]
        p2 = filamento[half : l]
        p2.reverse()
        
        if p1 == p2:
            print('SI ZIO PERA')
        else:
            print('HELL NO')
    
    else:
        p1 = filamento[0 : round(half)]
        p2 = filamento[round(half + 1) : l]
        
        print(p1, p2)
        
        if p1 == p2:
            print('Strano ma si')
        else:
            print('not even close')
        
    
    return

