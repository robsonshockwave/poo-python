class Disciplina:

    def __init__(self, codigo, nome, cargaHoraria):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome
    
    def getCargaHoraria(self):
        return self.__cargaHoraria
    
class Grade: 

    def __init__(self, ano):
        self.__ano = ano
        self.__disciplinas = []

    def getAno(self):
        return self.__ano
    
    def getDisciplina(self):
        return self.__disciplinas
    
    def addDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)
    
class Curso:

    def __init__(self, nome, grade):
        self.__nome = nome 
        self.__grade = []

    def getNome(self):
        return self.__nome
    
    def getGrade(self):
        return self.__grade
    
    def addGrade(self, grade):
        self.__grade.append(grade)
    
class Aluno:

    def __init__(self, nome, nroMatric, curso):
        self.__nome = nome
        self.__nroMatric = nroMatric
        self.__curso = curso
        self.__disciplinasObrigatorias = []
        self.__disciplinasEletivas = []
        self.__historico = []

    def getNome(self):
        return self.__nome

    def getNroMatric(self):
        return self.__nroMatric
    
    def getCurso(self):
        return self.__curso
    
    def getDisciplinasObrigatorias(self):
        return self.__disciplinasObrigatorias
    
    def getDisciplinasEletivas(self):
        return self.__disciplinasEletivas
    
    def getHistorico(self):
        return self.__historico
    
    def addDisciplinaObrigatoria(self, disciplina):
        self.__disciplinasObrigatorias.append(disciplina)
    
    def addDisciplinaEletiva(self, disciplina):
        self.__disciplinasEletivas.append(disciplina)
    
    def addHistorico(self, historico):
        self.__historico.append(historico)
        
class Historico:

    def __init__(self, aluno):
        self.__aluno = aluno
        self.__disciplinasObrigatorias = []
        self.__disciplinasEletivas = []
        self.__horasObrigatorias = 0
        self.__horasEletivas = 0

        aluno.addHistorico(self)

    def getAluno(self):
        return self.__aluno
    
    def getDisciplinasObrigatorias(self):
        if len(self.__disciplinasObrigatorias) == 0:
            print('\n{} AINDA NAO CURSOU DISCIPLINAS OBRIGATORIAS '.format(self.getAluno().getNome()))
        else:
            print('\nDISCIPLINAS OBRIGATORIAS CURSADAS POR: {}'.format(self.getAluno().getNome()))
            for disciplina in self.__disciplinasObrigatorias:
                print('{} - CARGA HORARIA: {}'.format(disciplina.getNome(), disciplina.getCargaHoraria()))
    
    def getHorasObgt(self):
        if len(self.__disciplinasObrigatorias) == 0:
            print('{} NAO POSSUI CARGA HORARIA CADASTRADA PARA DISCIPLINAS OBRIGATORIAS '.format(self.getAluno().getNome()))
        else:
            print('TOTAL DE CARGA HORARIA: {}'.format(self.__horasObrigatorias))
            
    def getDisciplinasEletivas(self):
        if len(self.__disciplinasEletivas) == 0:
            print('\n{} AINDA NAO CURSOU DISCIPLINAS ELETIVAS '.format(self.getAluno().getNome()))
        else:
            print('\nDISCIPLINAS ELETIVAS CURSADAS POR: {}'.format(self.getAluno().getNome()))
            for disciplina in self.__disciplinasEletivas:
                print('{} - CARGA HORARIA: {}'.format(disciplina.getNome(), disciplina.getCargaHoraria()))
    
    def getHorasEltv(self):
        if len(self.__disciplinasEletivas) == 0:
            print('{} NAO POSSUI CARGA HORARIA CADASTRADA PARA DISCIPLINAS ELETIVAS '.format(self.getAluno().getNome()))
        else:
            print('CARGA HORARIA TORAL: {}'.format(self.__horasEletivas))
    
    def addDisciplinaObrigatoria(self, disciplina):
        self.__horasObrigatorias += disciplina.getCargaHoraria()
        self.__disciplinasObrigatorias.append(disciplina)
    
    def addDisciplinaEletiva(self, disciplina):
        self.__horasEletivas += disciplina.getCargaHoraria()
        self.__disciplinasEletivas.append(disciplina)
    
Disc1 = Disciplina('COM001', 'MATEMATICA INICIAL PARA PROGRAMACAO', 80)
Disc2 = Disciplina('COM002', 'PROGRAMACAO EM ASSEMBLY', 64)
Disc3 = Disciplina('COM003', 'EMPREENDEDORISMO E SOCIEDADE', 48)
Disc4 = Disciplina('COM004', 'PROGRAMACAO ORIENTADA A OBJETOS', 64)
Disc5 = Disciplina('COM005', 'ENGENHARIA DE SOFTWARE E GESTAO', 80)
Disc6 = Disciplina('COM006', 'PORTUGUES INSTRUMENTAL PARA INFORMATICA', 48)
Disc7 = Disciplina('ADS001', 'PROGRAMACAO EM LUA', 64)
Disc8 = Disciplina('ADS002', 'CONCERTO DE IMPRESSORAS E COMPUTADORES', 80)
Disc9 = Disciplina('ADS003', 'INGLES INSTRUMENTAL PARA INFORMATICA', 48)
Disc10 = Disciplina('ADS004', 'PROGRAMACAO WEB I', 64)
Disc11 = Disciplina('ADS005', 'BANCO DE DADOS I', 64)
Disc12 = Disciplina('ADS006', 'DESENVOLVIMENTO COM ANDROID STUDIO', 80)
grade1 = Grade(2020.1)
grade2 = Grade(2020.1)
grade1.addDisciplina(Disc1)
grade1.addDisciplina(Disc2)
grade1.addDisciplina(Disc3)
grade1.addDisciplina(Disc4)
grade1.addDisciplina(Disc5)
grade1.addDisciplina(Disc6)
grade2.addDisciplina(Disc7)
grade2.addDisciplina(Disc8)
grade2.addDisciplina(Disc9)
grade2.addDisciplina(Disc10)
grade2.addDisciplina(Disc11)
grade2.addDisciplina(Disc12)
curso1 = Curso('CIENCIA DA COMPUTACAO', grade1)
curso2 = Curso('ANALISE E DESENVOLVIMENTO DE SISTEMAS', grade2)


aluno1 = Aluno('Jailson Mendes', 2019123456, curso2)

for disciplina in grade1.getDisciplina():
    aluno1.addDisciplinaObrigatoria(disciplina)

aluno1.addDisciplinaEletiva(Disc8)
aluno1.addDisciplinaEletiva(Disc10)
histAluno1 = Historico(aluno1)

for disciplina in aluno1.getDisciplinasObrigatorias():
    histAluno1.addDisciplinaObrigatoria(disciplina)

for disciplina in aluno1.getDisciplinasEletivas():
    histAluno1.addDisciplinaEletiva(disciplina)


aluno2 = Aluno('Orivaldo da Silva', 2019876543, curso2)

for disciplina in grade2.getDisciplina():
    aluno2.addDisciplinaObrigatoria(disciplina)

aluno2.addDisciplinaEletiva(Disc5)
aluno2.addDisciplinaEletiva(Disc2)
histAluno2 = Historico(aluno2)

for disciplina in aluno2.getDisciplinasObrigatorias():
    histAluno2.addDisciplinaObrigatoria(disciplina)

for disciplina in aluno2.getDisciplinasEletivas():
    histAluno2.addDisciplinaEletiva(disciplina)


aluno3 = Aluno('Jamelao Santos', 2019999888, curso1)
histAluno3 = Historico(aluno3)


aluno4 = Aluno('Layne Staley', 2019272727, curso1)

for disciplina in grade2.getDisciplina():
    aluno4.addDisciplinaObrigatoria(disciplina)

histAluno4 = Historico(aluno4)
for disciplina in aluno4.getDisciplinasObrigatorias():
    histAluno4.addDisciplinaObrigatoria(disciplina)


aluno5 = Aluno('Kurt Cobain', 2019011111, curso2)

for disciplina in grade2.getDisciplina():
    aluno5.addDisciplinaObrigatoria(disciplina)

aluno5.addDisciplinaEletiva(Disc4)
aluno5.addDisciplinaEletiva(Disc3)
aluno5.addDisciplinaEletiva(Disc1)
histAluno5 = Historico(aluno5)

for disciplina in aluno5.getDisciplinasObrigatorias():
    histAluno5.addDisciplinaObrigatoria(disciplina)

for disciplina in aluno5.getDisciplinasEletivas():
    histAluno5.addDisciplinaEletiva(disciplina)

print("AGUARDE...\n")

print("""ALUNO: {}
MATRICULA: {} 
CURSO: {}""".format(aluno1.getNome(), aluno1.getNroMatric(), aluno1.getCurso().getNome()))
histAluno1.getDisciplinasObrigatorias()
histAluno1.getHorasObgt()
histAluno1.getDisciplinasEletivas()
histAluno1.getHorasEltv()
print()
print("""ALUNO: {}
MATRICULA: {} 
CURSO: {}""".format(aluno2.getNome(), aluno2.getNroMatric(), aluno2.getCurso().getNome()))
histAluno2.getDisciplinasObrigatorias()
histAluno2.getHorasObgt()
histAluno2.getDisciplinasEletivas()
histAluno2.getHorasEltv()
print()
print("""ALUNO: {}
MATRICULA: {} 
CURSO: {}""".format(aluno3.getNome(), aluno3.getNroMatric(), aluno3.getCurso().getNome()))
histAluno3.getDisciplinasObrigatorias()
histAluno3.getHorasObgt()
histAluno3.getDisciplinasEletivas()
histAluno3.getHorasEltv()
print()
print("""ALUNO: {}
MATRICULA: {} 
CURSO: {}""".format(aluno4.getNome(), aluno4.getNroMatric(), aluno4.getCurso().getNome()))
histAluno4.getDisciplinasObrigatorias()
histAluno4.getHorasObgt()
histAluno4.getDisciplinasEletivas()
histAluno4.getHorasEltv()
print()
print("""ALUNO: {}
MATRICULA: {} 
CURSO: {}""".format(aluno5.getNome(), aluno5.getNroMatric(), aluno5.getCurso().getNome()))
histAluno5.getDisciplinasObrigatorias()
histAluno5.getHorasObgt()
histAluno5.getDisciplinasEletivas()
histAluno5.getHorasEltv()