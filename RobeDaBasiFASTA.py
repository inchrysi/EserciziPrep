print("Bonjour, questi sono gli es della lezione 2 ed ecco le funzioni che ho creato:")

funzioncini = ["validSeq2", "contaBasi", "frequentBase", "frequentBase2", "confrontSeq", "complSeq"]

for funzione in funzioncini:
    print(funzione)
    
print("PS: Puoi creare una una seq di lunghezza n random usando generaLista(n)")

lista = ['c', 't', 'palle', 't', 'a', 'c', 'a', 'a', 'g']

def stampaBasi(filamento):
    l = len(filamento)
    for i in range(l):
        print(filamento[i])
    
    return

#===================================================validSeq

def validSeq1(filamento): #mi verifica ogni base e mi stampa t or f per ogni base
    l = len(filamento)
    basi = ['a', 't', 'c', 'g']
    
    for i in range(l):
        if filamento[i] in basi:
            print(True)
        else:
            print(False)
    return


def validSeq2(filamento): #voglio solo individuare l'erroe e quale indice
    l = len(filamento)
    basi = ['a', 't', 'c', 'g']
    errori = []
    
    for i in range(l):
        if filamento[i] not in basi:
            errori.append(filamento[i])
            print("Errore in posizione", (i))
            print("Elemento in questione:", filamento[i])
        
    print("Riassunto errori:", errori)
    
    return

def validSeq3(filamento): #t or f
    l = len(filamento)
    basi = ['a', 't', 'c', 'g']
    
    for i in range(l):
        if filamento[i] not in basi:
            return False
    
    return True

def validSeq4(filamento): #bool
    l = len(filamento)
    basi = ['a', 't', 'c', 'g']
    flag = True
    
    for i in range(l):
        if filamento[i] not in basi:
            flag = False
    
    return flag
#===================================================contaBasi

def contaBasi(filamento, baseDaCercare): #metto lista e mi dice quanti basi ho
    l = len(filamento)
    base = 0
    
    if baseDaCercare != 0:
        for i in range(l):
            if filamento[i] == baseDaCercare:
                base+= 1
        print(baseDaCercare, "appare nel filamento", base, "volte")
        
    else:
        for i in range(l):
            base+= 1
        print("Il filamento è lungo", base, "basi")
    
    return base

#==================================================frequentBase

def frequentBase1(filamento): #senza dictionary
    l = len(filamento)
    adenina = 0
    timina = 0
    citosina = 0
    guanina = 0
    
    for i in range(l):
        if filamento[i] == 'a':
            adenina+= 1
        elif filamento[i] == 't':
            timina+= 1
        elif filamento[i] == 'c':
            citosina+= 1
        elif filamento[i] == 'g':
            guanina+= 1
   
    robe = [adenina, timina, citosina, guanina]
    massimo = 0
    
    for x in robe:
        if int(x) > massimo:
            massimo = x
    
    print("La base più frequente appare", massimo, "volte ed è", )
    
    return


def frequentBase2(filamento): #con dictionary
    l = len(filamento)
    adenina = 0
    timina = 0
    citosina = 0
    guanina = 0
    
    for i in range(l):
        if filamento[i] == 'a':
            adenina+= 1
        elif filamento[i] == 't':
            timina+= 1
        elif filamento[i] == 'c':
            citosina+= 1
        elif filamento[i] == 'g':
            guanina+= 1
   
    robe = {'adenina' : adenina, 'timina' : timina, 'citosina' : citosina, 'guanina' : guanina}
    massimoNome = ''
    massimoValore = 0
    
    for nome, valore in robe.items():
        if valore > massimoValore:
            massimoValore = valore
            massimoNome = nome
    
    print(massimoNome, massimoValore)

    #print("La base più frequente appare", massimo, "volte ed è")
    
    return

def frequentBase3(filamento): #stubbato brutto 
    l = len(filamento)
    adenina = contaBasi(filamento, 'a')
    timina = contaBasi(filamento, 't')
    citosina = contaBasi(filamento, 'c')
    guanina = contaBasi(filamento, 'g')
    
    robe = [adenina, timina, citosina, guanina]
    massimo = 0
    
    for i in range(len(robe)):
        if robe[i] > massimo:
            massimo = robe[i]
    
    for i in range(len(robe)):
        if robe[i] == massimo:
            if i == 0:
                print('Adenina')
            if i == 1:
                print('Timina')
            if i == 2:
                print('Citosina')
            if i == 3:
                print('Guanina')
    
    print("La base più frequente appare", massimo)
    
    return massimo

#===================================================confrontSeq
lista1 = ['t', 'c', 't', 'g', 'c', 'c', 't']
lista2 = ['t', 't', 'a', 'c', 't', 't', 'c', 't', 'c']

def confrontSeq(fil1, fil2):
    l1 = len(fil1)
    l2 = len(fil2)
    match = []
    
    differenza = l1 - l2
    
    if l1 < l2:
        size = l1
    else:
        size = l2
        
    for i in range(size):  #mi dà errore index out of range
        
        if fil1[i] == fil2[i]:
            match.append(fil1[i])
        else:
            match.append('X')
    
    for n in range(abs(differenza)):
        match.append('-')
    
    nMismatch = 0
    nMatch = 0
    
    for x in match:
        if x == 'X':
            nMismatch+= 1
        else:
            nMatch+= 1
    
    print("Le tue seq corrispondono di", nMatch, "basi.")
    print("Il numero di mismatch sono:", nMismatch)
    print("Ecco la sequenza matching:", match)
    
    return

#===================================================complSeq

def complSeq(fil1, fil2):
    l1 = len(fil1)
    l2 = len(fil2)
    differenza = l1 - l2
    
    compAT = 0
    compGC = 0
    posizione = []
    
    if l1 < l2:
        size = l1
    else:
        size = l2
    
    for i in range(size):
        if fil1[i] == 'a' and fil2[i] == 't' or fil1[i] == 't' and fil2[i] == 'a':
            compAT+= 1
            posizione.append(i)
        if fil1[i] == 'g' and fil2[i] == 'c' or fil1[i] == 'c' and fil2[i] == 'g':
            compGC+= 1
            posizione.append(i)
    
    print("Ci sono A-T =", compAT, "e G-C =", compGC)
    
    if len(posizione) > 1:
        print("Gli appaiamenti si verificano nelle posizioni:", posizione)
    else:
        print("L'appaiamento si verifica nella posizione:", posizione)
    
# FASTA =============================================
def readFASTA(txtfile):
    basi = ['A', 'T', 'C', 'G']
    with open(txtfile, "r") as input:
        for riga in input:
            f = riga.strip()
            intero+= f
        
        seq = intero.split(">") #ho la lista con ognuno le sequenze con identificativo
        nome = ""
        listanomi = []
        
        for x in seq:
            for i in range(0, len(x)):
                if x[i] not in basi:
                    nome+= x[i]
            listanomi.append(nome)
            nome = ""
        listanomi.pop(0)
        
        #for ident in listanomi:
    return listanomi

def readFASTA1(txtfile):
    nomi = []
    sequenze = []
    seq = ""
    
    with open(txtfile, "r") as input:
        for riga in input:
            f = riga.strip()
            if riga.startswith(">"):
                nomi.append(f)
                sequenze.append(seq)
                seq = ""
            else:
                seq+= f
        sequenze.append(seq)
        sequenze.pop(0)
    
    return nomi, sequenze

def readFASTA2(txtfile):
    nomieseq = {}
    
    with open(txtfile, "r") as input:
        for riga in input:
            f = riga.strip()
            if riga.startswith(">"):
                chiave = f[1:]
                nomieseq[chiave] = ""
            else:
                nomieseq[chiave]+= f
            
    return nomieseq

# FASTA in testo con nome e poi sequenza ============================

def FASTAintxt(FASTAfile):
    
    coso = readFASTA2(FASTAfile)
    
    with open("convertito.txt", "w") as f:
        for x, y in coso.items():
            f.write(x)
            f.write(":")
            f.write(y)
            f.write("\n")
    
    return

# GCcontent of a seq =========================
def GCcontent(sequenza):
    GC = 0
    
    for x in sequenza:
        if x == "G" or x == "C":
            GC+=1
    
    GCperc = GC * 100 / len(sequenza)
    
    return GCperc

# FASTA GCcontent ===================================
def FASTAGCcontent(FASTAfile):
    conv = readFASTA2(FASTAfile)
    GCqt = {}
    
    for x, y in conv.items():
        GCqt[x] = GCcontent(y)
    
    return GCqt

# most GCcontent ================================
def mostGC(dic):
    maggiore = 0
    
    for x, y in dic.items():
        if y > maggiore:
            maggiore = y
    
    print(x, maggiore)
    
    return 