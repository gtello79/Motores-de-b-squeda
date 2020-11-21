import numpy as np
import os
from Estructura.Trie import Trie

def loadData(dataPath):
    countLine = 0
    struct = None
    dataFile = open(dataPath,'r')
    parsedText = []
    
    for line in dataFile:        
        if countLine == 0:
            #Se omite la primera linea del archivo de texto
            struct = line
        else:
            #Se procede a almacenar el texto de la ultima columna del csv
            wordList = []
            text = line.strip().split(',')[-1]
            parsed = text.strip().split()
            for word in parsed:
                if(word.isalpha()):
                    x = word.upper()
                    wordList.append(x)
            parsedText.append(wordList)
        countLine+=1
    
    return parsedText


def main():
    dataPath = 'Dataset/inaug_speeches.csv'
    data = loadData(dataPath)
    trie = Trie(data)
    intro = True

    #Menu de ingreso
    while(intro):
        print("CADENA A PREDECIR")
        phrase = input("")
        words = phrase.strip().split()
        chain = []
        for word in words:
            if(word.isalpha()):
                w = word.upper()
                x = trie.searchWord(w)
                chain.append(x)
        print(" ".join(chain))
        print("")
        print("INGRESA 1 SI QUIERES PREDECIR OTRA CADENA")
        print("CUALQUIER OTRA OPCION SALDRA DEL PROGRAMA")
        x = int(input("OPCION: "))
        if(x != 1):
            break
        
    
    

main()