class Elemento(object):
    def __init__(self,valor):
        self._valor = valor
    
    def getValor(self):
        return self._valor
    def setValor(self,valor):
        self._valor = valor