from Elemento import Elemento
from No import No

class ArvoreBinaria(object):
    def __init__(self):
        self._raiz = None

    def getRaiz(self):
        return self._raiz
    def setRaiz(self,raiz):
        self._raiz = raiz

    def insere(self,valor):
        if self._raiz == None:
            self._raiz = No(valor)
        else:
            self.insereSistema(None,self._raiz,valor)

    def insereSistema(self,pai,atual,valor):
        if atual != None:
            if valor < atual.getElemento().getValor():
                self.insereSistema(atual,atual.getFilhoEsquerda(),valor)
            else:
                self.insereSistema(atual,atual.getFilhoDireita(),valor)
        else:
            x = No(valor)
            if valor < pai.getElemento().getValor():
                pai.setFilhoEsquerda(x)
            else:
                pai.setFilhoDireita(x)

    def preOrdem(self,no):
	    if no != None:
		    self.emOrdem(no.getFilhoEsquerda())
		    
		    self.emOrdem(no.getFilhoDireita())
            print(no.getElemento().getValor())

    def emOrdem(self,no):
	    if no != None:
		    self.emOrdem(no.getFilhoEsquerda())
		    print(no.getElemento().getValor())
		    self.emOrdem(no.getFilhoDireita())

    def remover(self,valor):
        if self._raiz != None:
            x = self._raiz
            if n == x.getElemento().getValor():
                if x.getFilhoEsquerda() == None and x.getFilhoDireitaa() == None:
                    self.setRaiz(None)
                elif x.getFilhoEsquerda() != None and x.setFilhoDireita() == None:
                    self.setRaiz(x.getFilhoEsquerda())
                    x.setFilhoEsquerda(None)
                elif x.getFilhoEsquerda() == None and x.getFilhoDireitaa() != None:
                    self.setRaiz(x.getFilhoDireita())
                    x.setFilhoDireita(None)
            else:
                

                




arvore = ArvoreBinaria()

arvore.insere(5)
arvore.insere(4)
arvore.insere(6)
arvore.insere(3)
arvore.insere(8)
arvore.insere(2)
arvore.insere(9)
arvore.emOrdem(arvore.getRaiz())