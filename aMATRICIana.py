
def setIncreasingMatrix(size):
    # m = [[default for _ in range(size)] for _ in range(size)]
    m = [[i + (j * size) for i in range(size)] for j in range(size)]
    
    return m

def manualSetIncreasingMatrix(size):
    m = []
    
    for j in range(size):
        l = []
        for i in range(size):
            l.append(i + (j * size))
        m.append(l)
        
    return m