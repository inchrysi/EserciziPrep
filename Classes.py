class Gene:
    def __init__(self, name, length):
        self.setNome(name)
        self.length = length
        
    def setNome(self, newName):
        newName = newName
        self.__name = newName
        
    def describe(self):
        print('Gene ' + self.__name + ' is long ' + str(self.length) + ' bp')

class Sample:
    def __init__(self, name, expressedGenes):
        self.setName(name)
        self.expressedGenes = expressedGenes
        
    def addGene(self, geneName):
        self.expressedGenes.append(geneName)
    
    def showGenes(self):
        print(self.expressedGenes)
    
    def setName(self, newName):
        newName = newName
        self.__name = newName

class DNASequence:
    def __init__(self, sequence):
        self.sequence = sequence
    
    def GCcontent(self):
        seq = self.sequence
        count = 0
        
        for x in seq:
            if x == 'G' or x == 'C':
                count+=1
        
        GC = count * 100 / len(seq)
        
        return GC

class Experiment:
    def __init__(self, name, Sample):
        self.name = name
        self.Sample = Sample
    
    def addSample(self, sample):
        self.Sample.append(sample)
    
    def listSamples(self):
        print(self.Sample)


#DA RIVEDERE
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Patient(Person):
    def __init__(self, name, age, diagnosis):
        super().__init__(name, age) #MA IN CHE SESNOSOS
        self.diagnosis = diagnosis
    
    def summary(self):
        print(self.name, self.age, '-', self.diagnosis)
