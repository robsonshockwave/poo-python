from abc import ABC, abstractmethod

class titulacaoNaoEDoutor(Exception):
    pass

class idadeMenorQuePermitida(Exception):
    pass

class cursoInvalido(Exception):
    pass

class cpfDuplicado(Exception):
    pass

class Pessoa(ABC):
    def __init__(self, nome, idade, endereco, cpf):
        self.__nome = nome
        self.__idade = idade 
        self.__endereco = endereco
        self.__cpf = cpf

    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def getEndereco(self):
        return self.__endereco

    def getCpf(self):
        return self.__cpf
    
    @abstractmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, idade, endereco, cpf, titulacao):
        super().__init__(nome, idade, endereco, cpf)
        self.__titulacao = titulacao
    
    def getTitulacao(self):
        return self.__titulacao
    
    def printDescricao(self):
        print("""PROFESSOR: {} IDADE: {} TITULACAO: {} ENDERECO: {} CPF: {}""".format(self.getNome(),self.getIdade(), self.getTitulacao(), self.getEndereco(), self.getCpf()))

class Aluno(Pessoa):
    def __init__(self, nome, idade, endereco, cpf, curso):
        super().__init__(nome, idade, endereco, cpf)
        self.__curso = curso
    
    def getCurso(self):
        return self.__curso
    
    def printDescricao(self):
        print("""ALUNO: {} IDADE: {} CURSO: {} ENDERECO: {} CPF: {} """.format(self.getNome(),self.getIdade(), self.getCurso(), self.getEndereco(), self.getCpf()))

Professores = [
("John Lennon", 50, "Los Angeles, The Street Nine, n° 9", "123.456.789-12", "Mestre"),
("Kurt Cobain", 27, "Rio Branco, Rua Dino Sauro, n° 123", "123.456.789-14", "Especializado"),
("Layne Staley", 30, "Carmo de Minas, Rua dos Operários, n° 106", "123.456.789-13", "Doutor"),
("Serj Tankian", 56, "Chicago, Street Megan, n° 178", "123.456.789-13", "Mestre"),
("Amy Lee", 34, "Jordânia, Street Juscelino Kubitscheck, n° 1510", "123.456.789-15", "Especializado"),
("Robson", 24, "New York,The Garden, n° 1", "123.456.789-16", "Doutor"),
]

Alunos = [
("Silvio Santos", 18, "São Paulo, Maaaôooeee, n° 123", "123.456.789-20", "SIN"),
("Ratinho", 19, "Rio de Janeiro, Rua TIROlesa, n° 145", "123.456.789-21", "SIN"),
("Hebe", 15, "Rio de Janeiro, Rua do Maracujá, n° 999", "123.456.789-22", "CCO"),
("Galo Cego", 24, "Maringá, Rua Cinco Reais, n° 888", "123.456.789-23", "SIN"),
("Vin Diesel", 99, "Orlando, Street 300KM/H, nº 1235", "123.456.789-23", "SIN"),
("Pica Pau", 19, "Hollywood, Rua California, 777", "123.456.789-24", "CAT"),
]

Cadastro = {}

print("PROFESSORES:")
for nome, idade, endereco, cpf, titulacao in Professores:
    try:
        if cpf in Cadastro:
            raise cpfDuplicado()
        if idade < 30:
            raise idadeMenorQuePermitida()
        if titulacao != 'Doutor':
            raise titulacaoNaoEDoutor()
    except cpfDuplicado:
        print('O(A) CPF {} DO(A) PROFESSOR(A) {} JÁ ESTÁ SENDO USADO! - PODE TER OCORRIDO UM ENGANO, TENTE NOVAMENTE.'.format(cpf, nome))
    except idadeMenorQuePermitida:
        print('O(A) PROFESSOR(A) {} POSSUI IDADE {}, SENDO INFERIOR DO QUE A PERMITADA.'. format(nome, idade))
    except titulacaoNaoEDoutor:
        print('O(A) PROFESSOR(A) {} NÃO POSSUI DOUTORADO, ELE(A) É {}.'.format(nome, titulacao))
    else:
        pessoa = Professor(nome, idade, endereco, cpf, titulacao)
        Cadastro[cpf] = pessoa
        print("{} FOI CADASTRADO,".format(nome))
        pessoa.printDescricao()
print()
print("ALUNOS:")
for nome, idade, endereco, cpf, curso in Alunos:
    try:
        if cpf in Cadastro:
            raise cpfDuplicado()
        if idade < 18:
            raise idadeMenorQuePermitida()
        if curso != 'CCO' and curso != 'SIN':
            raise cursoInvalido()
    except cpfDuplicado:
        print('O CPF {} DO(A) ALUNO(A) {} JÁ ESTÁ SENDO USADO! - PODE TER OCORRIDO UM ENGANO, TENTE NOVAMENTE.'.format(cpf, nome))
    except idadeMenorQuePermitida:
        print('O(A) ALUNO(A) {} POSSUI IDADE {}, SENDO INFERIOR DO QUE A PERMITADA.'. format(nome, idade))
    except cursoInvalido:
        print('O(A) ALUNO(A) {} NÃO CURSA SISTEMAS OU CIÊNCIA, ELE(A) É DO CURSO {}'.format(nome, curso))
    else:
        pessoa = Aluno(nome, idade, endereco, cpf, curso)
        Cadastro[cpf] = pessoa
        print("{} FOI CADASTRADO".format(nome))
        pessoa.printDescricao()