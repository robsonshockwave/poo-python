from abc import ABC, abstractmethod

class EmpDomestica(ABC):

    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone
    
    def getNome(self):
        return self.__nome

    def getTelefone(self):
        return self.__telefone
    
    @abstractmethod
    def getSalario(self):
        pass

class Horista(EmpDomestica):

    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorPorHora = valorPorHora
    
    def getHorasTrabalhadas(self):
        return self.__horasTrabalhadas
    
    def getValorPorHora(self):
        return self.__valorPorHora
    
    def getSalario(self):
        salario = self.getHorasTrabalhadas() * self.getValorPorHora()
        return salario

class Diarista(EmpDomestica):

    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorPorDia = valorPorDia
    
    def getDiasTrabalhados(self):
        return self.__diasTrabalhados
    
    def getValorPorDia(self):
        return self.__valorPorDia
    
    def getSalario(self):
        salario = self.getDiasTrabalhados() * self.getValorPorDia()
        return salario

class Mensalista(EmpDomestica):
  
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__ValorMensal = valorMensal
    
    def getValorMensal(self):
        return self.__ValorMensal
    
    def getSalario(self):
        return self.getValorMensal()
    
print('EMPREGADAS DISPONÍVEIS:\n')
horista = Horista('Arlinda Cruz', '1234567890', 150, 9)
print("""Nome: {}.
Telefone: {}.
Salário Mensal: {}.""".format(horista.getNome(), horista.getTelefone(), horista.getSalario()))
print()

diarista = Diarista('Cassia Eller', '0987654321', 19, 60)
print("""Nome: {}.
Telefone: {}.
Salário Mensal: {}.""".format(diarista.getNome(), diarista.getTelefone(), diarista.getSalario()))
print()

mensalista = Mensalista('Rauzete Seixas', '1234509876', 1000)
print("""Nome: {}.
Telefone: {}.
Salário Mensal: {}.""".format(mensalista.getNome(), mensalista.getTelefone(), mensalista.getSalario()))
print()

if horista.getSalario() < diarista.getSalario():
    if horista.getSalario() < mensalista.getSalario():
        print('A EMPREGADA NA QUAL O SALÁRIO MAIS BAIXO É:')
        print("""Nome: {}.
Telefone: {}.
Salário Mensal: {}.""".format(horista.getNome(), horista.getTelefone(), horista.getSalario()))

    else:
        print('A EMPREGADA NA QUAL O SALÁRIO MAIS BAIXO É:')
        print("""Nome: {}.
Telefone: {}.
Salário Mensal: {}.""".format(mensalista.getNome(), mensalista.getTelefone(), mensalista.getSalario()))

if diarista.getSalario() < horista.getSalario():
    if diarista.getSalario() < mensalista.getSalario():
        print('A EMPREGADA NA QUAL O SALÁRIO MAIS BAIXO É:')
        print("""Nome: {}.
Telefone: {}.
Salário Mensal: {}.""".format(diarista.getNome(), diarista.getTelefone(), diarista.getSalario()))

    else:
        print('A EMPREGADA NA QUAL O SALÁRIO MAIS BAIXO É:')
        print("""Nome: {}.
Telefone: {}.
Salário Mensal: {}.""".format(mensalista.getNome(), mensalista.getTelefone(), mensalista.getSalario()))