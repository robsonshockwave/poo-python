def mdc(m, n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

def fracaoIgual(f1, f2):
    return (f1.getNumerador() == f2.getNumerador()) and (f1.getDenominador() == f2.getDenominador())    
 
class Fracao:
    
    def __init__(self, numerador, denominador):
        self.__numerador = numerador        
        self.__denominador = denominador     

    def __str__(self):
        return str(self.__numerador) + "/" + str(self.__denominador)

    def getNumerador(self):
        return self.__numerador

    def getDenominador(self):
        return self.__denominador       

    def simplifica(self):
        divComum = mdc(self.__numerador, self.__denominador)
        self.__numerador = self.__numerador // divComum
        self.__denominador = self.__denominador // divComum 

    def __add__(self, outraFrac):
        novonumerador = self.__numerador * outraFrac.getDenominador() + self.__denominador * outraFrac.getNumerador()
        novodenominador = self.__denominador * outraFrac.getDenominador()
        divComum = mdc(novonumerador, novodenominador)
        novaFracao = Fracao(novonumerador//divComum, novodenominador//divComum)
        if novaFracao.getNumerador() / novaFracao.getDenominador() < 1:
            return novaFracao
        if novaFracao.getNumerador() / novaFracao.getDenominador() == 1:
            novaFracao = 1
            return novaFracao
        else:
            parteInteira = novaFracao.getNumerador() // novaFracao.getDenominador()
            novonumerador2 = novaFracao.getNumerador() - parteInteira * novaFracao.getDenominador()
            fracMista = fracaoMista(parteInteira, novonumerador2, novaFracao.getDenominador())
            return fracMista

    def transformaEmFracaoMista(self):
        parteInt = self.getNumerador() // self.getDenominador()
        novoNum = self.getNumerador() - parteInt * self.getDenominador()
        fracTransformadaMista = fracaoMista(parteInt, novoNum, self.getDenominador())
        return fracTransformadaMista
        
class fracaoMista(Fracao):
    def __init__(self, parteInteira, num, den):
        super().__init__(num, den)
        self.__parteInteira = parteInteira

    def getParteInteira(self):
        return self.__parteInteira
    
    def __str__(self):
        return str(self.__parteInteira) + ' ' + str(self.getNumerador()) + "/" + str(self.getDenominador())

fracao1 = Fracao(7, 6)
fracao2 = Fracao(13, 7)
soma = fracao1 + fracao2
print()
print("""{} + {} = {}""".format(fracao1, fracao2, soma))

fracao3 = Fracao(1, 3)
fracao4 = Fracao(2, 3)
soma2 = fracao3 + fracao4
print()
print("""{} + {} = {}""".format(fracao3, fracao4, soma2))

fracao5 = Fracao(7, 2)
fracao6 = Fracao(14, 3)
soma3 = fracao5 + fracao6
print()
print("""{} + {} = {}""".format(fracao5.transformaEmFracaoMista(), fracao6.transformaEmFracaoMista(), soma3))