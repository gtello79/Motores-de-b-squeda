class Trienode:
    #Se inicializa el nodo
    def __init__(self, element):
        self.element = element
        self.counter = 1
        self.prob = 0
        self.son = []
    

    def addChild(self,child):    
        self.son.append(child)

    #Retorna una prediccion obtenida a partir de las probabilidades de sus hijos
    def getPredicted(self):
        maxProb = 0
        maxSon = None
        for s in self.son:
            if(s.prob >= maxProb):
                maxSon = s
                maxProb = s.prob
        return maxSon

    #Se actualiza la probabilidad de las palabras
    def updateProb(self, rootVal):
        self.prob = self.counter/rootVal
        for s in self.son:
            s.updateProb(self.counter)

    def infoSons(self):
        print("Este nodo tiene un total de " + str(len(self.son)) + " hijos")

    