from Elemento import Elemento

class No(object):
    def __init__(self,valor):
        self._elemento = Elemento(valor)
        self._filhoDireita = None
        self._filhoEsquerda = None
        
    def getElemento(self):
        return self._elemento
    def setElemento(self,valor):
        self._elemento = Elemento(valor)

    def getFilhoDireita(self):
        return self._filhoDireita
    def setFilhoDireita(self,no):
        self._filhoDireita = no

    def getFilhoEsquerda(self):
        return self._filhoEsquerda
    def setFilhoEsquerda(self,no):
        self._filhoEsquerda = no
    
    
