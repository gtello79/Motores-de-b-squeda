from Estructura.Trienode import Trienode 
import copy as cp

class Trie:
    #Se inicializa el Tree
    def __init__(self, library):
        self.root = Trienode("")
        self.data = library
        for text in self.data:
            for word in text:
                self.agregar(word)
        self.updateProb()
            
        
    #Se agregan palabras al Trie
    def agregar(self, palabra):
        actual = self.root
        for letra in palabra:
            encontrado = False
            for child in actual.son:
                if child.element == letra:
                    child.counter +=1
                    actual = child
                    encontrado = True
                    break

            if (not(encontrado)):
                nuevo = Trienode(letra)
                actual.addChild(nuevo)
                actual = nuevo
    

    #Se busca un elemento en el trie
    def searchWord(self,palabra):
        word = ""
        node = cp.deepcopy(self.root)
        for l in palabra:
            finded = False
            for n in node.son:
                if(l == n.element):
                    word+=l
                    node = n
                    finded = True
                    break
            if(not(finded)):
                break
        
        if(word != palabra):    
            while(node is not None):
                node = node.getPredicted()
                if(node is None):
                    word+=""
                else:
                    word += node.element

        self.agregar(palabra)
        self.updateProb()
        return word






    def updateProb(self):
        self.root.updateProb(self.root.counter)
    
    def findInData(self,w):
        for text in self.data:
            for word in text:
                if w == word:
                    return (word)

    def findWord(self, word):
        final = ""
        actual = self.root
        for w in word:
            for n in actual.son:
                if w == n.element:
                    final += w
                    actual = n
                    break
        print(final)