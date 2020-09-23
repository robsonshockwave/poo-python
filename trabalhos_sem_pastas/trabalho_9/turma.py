import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import estudante as est 
import disciplina as disc

class CampoVazio(Exception):
    pass

class FaltouCodigo(Exception):
    pass

class FaltouAluno(Exception):
    pass

class turmaDuplicada(Exception):
    pass

class Turma:

    def __init__(self, codigo, disciplina, estudantes):
        self.__codigo = codigo
        self.__disciplina = disciplina
        self.__estudantes = estudantes

    def getCodigo(self):
        return self.__codigo
    
    def getDisciplina(self):
        return self.__disciplina

    def getEstudantes(self):
        return self.__estudantes

class LimiteInsereTurma(tk.Toplevel):
    def __init__(self, controle, listaCodDiscip, listaNroMatric):

        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Disciplina")
        self.controle = controle

        self.frameCodTurma = tk.Frame(self)
        self.frameDiscip = tk.Frame(self)
        self.frameEstudante = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodTurma.pack()
        self.frameDiscip.pack()
        self.frameEstudante.pack()
        self.frameButton.pack()        

        self.labelCodTurma = tk.Label(self.frameCodTurma,text="INFORME O CODIGO DA TURMA: ")
        self.labelCodTurma.pack(side="left")
        self.inputCodTurma = tk.Entry(self.frameCodTurma, width=20)
        self.inputCodTurma.pack(side="left")

        self.labelDiscip = tk.Label(self.frameDiscip,text="QUAL A DISCIPLINA? : ")
        self.labelDiscip.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameDiscip, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCodDiscip

        self.labelEst = tk.Label(self.frameEstudante,text="QUAL O ESTUDANTE? : \n")
        self.labelEst.pack(side="left") 
        self.listbox = tk.Listbox(self.frameEstudante)
        self.listbox.pack(side="left")
        for nro in listaNroMatric:
            self.listbox.insert(tk.END, nro)

        self.buttonInsere = tk.Button(self.frameButton ,text="INSERIR ALUNO", font = ('Negrito', 9))           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereAluno)

        self.buttonCria = tk.Button(self.frameButton ,text="CRIAR TURMA", font = ('Negrito', 9))           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaTurma)   

        self.buttonConcluido = tk.Button(self.frameButton, text = 'CONCLUIDO', font = ('Negrito', 9))
        self.buttonConcluido.pack(side = 'left')
        self.buttonConcluido.bind("<Button>", controle.concluidoHandler) 

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)            

class LimiteMostraTurmas():
    def __init__(self, str):
        messagebox.showinfo('LISTA DE TURMAS', str)

class LimiteConsultaTurmas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('280x60')
        self.title("CONSULTAR TURMAS")
        self.controle = controle

        self.frameCode = tk.Frame(self)
        self.frameButtons = tk.Frame(self)
        self.frameCode.pack()
        self.frameButtons.pack()

        self.labelCode = tk.Label(self.frameCode, text = 'CODIGO DA DISCIPLINA:  ')
        self.labelCode.pack(side = 'left')

        self.inputCode = tk.Entry(self.frameCode, width = 20)
        self.inputCode.pack(side = 'left')

        self.buttonConsulta = tk.Button(self.frameButtons, text = 'CONSULTAR', font = ('Negrito', 9))
        self.buttonConsulta.pack(side = 'left')
        self.buttonConsulta.bind("<Button>", controle.consultaHandler)

        self.buttonConcluido = tk.Button(self.frameButtons, text = 'CONCLUIDO', font = ('Negrito', 9))
        self.buttonConcluido.pack(side = 'left')
        self.buttonConcluido.bind("<Button>", controle.concluiHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlTurma():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaTurmas = []
        self.listaAlunosTurma = []

        self.listaNroMatric = []

    def insereTurmas(self):        
        self.listaAlunosTurma = []
        listaCodDisc = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        self.listaNroMatric = self.ctrlPrincipal.ctrlEstudante.getListaNroMatric()
        self.limiteIns = LimiteInsereTurma(self, listaCodDisc, self.listaNroMatric)

    def criaTurma(self, event):
        try:
            if len(self.limiteIns.inputCodTurma.get()) == 0 and len(self.limiteIns.escolhaCombo.get()) == 0:
                raise CampoVazio()
            if len(self.limiteIns.inputCodTurma.get()) == 0:
                raise FaltouCodigo()
            if len(self.limiteIns.escolhaCombo.get()) == 0:
                raise FaltouAluno()
        except CampoVazio:
            self.limiteIns.mostraJanela('ERROR', 'PREENCHA TODOS CAMPOS')
        except FaltouCodigo:
            self.limiteIns.mostraJanela('ERROR', 'INFORME O CODIGO')
        except FaltouAluno:
            self.limiteIns.mostraJanela('ERROR', 'ESCOLHA A DISCIPLINA')
        
        else:
            codTurma = self.limiteIns.inputCodTurma.get()
            discSel = self.limiteIns.escolhaCombo.get()
            disc = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(discSel)
            turma = Turma(codTurma, disc, self.listaAlunosTurma)
            try:
                for turmas in self.listaTurmas:
                    if turma.getCodigo() == turmas.getCodigo():
                        raise turmaDuplicada()
            except turmaDuplicada:
                str = ("UMA TURMA COM O CODIGO '{}'' JA ESTA CADASTRADA".format(codTurma))
                self.limiteIns.mostraJanela('ERROR', str)
            
            else:
                self.listaTurmas.append(turma)
                self.limiteIns.mostraJanela('INSERCAO REALIZADA COM SUCESSO', 'TURMA CRIADA')
                self.limiteIns.inputCodTurma.delete(0, len(self.limiteIns.inputCodTurma.get()))
            
    def insereAluno(self, event):
        try:
            if len(self.limiteIns.listbox.get(tk.ACTIVE)) == None:
                raise CampoVazio()
        except CampoVazio:
            self.limiteIns.mostraJanela('FALHA NA MATRICULA DO ALUNO', 'NENHUM ALUNO ALUNO FOI SELECIONADO')

        else:
            alunoSel = self.limiteIns.listbox.get(tk.ACTIVE)
            aluno = self.ctrlPrincipal.ctrlEstudante.getEstudante(alunoSel)
            self.listaAlunosTurma.append(aluno)
            self.limiteIns.mostraJanela('CONGRULATIONS', 'ALUNO MATRICULADO')
            self.limiteIns.listbox.delete(tk.ACTIVE)
        
    def mostraTurmas(self):
        str = ''
        if len(self.listaTurmas) == 0:
            str += 'NENHUMA TURMA FOI CADASTRADA'
            self.limiteLista = LimiteMostraTurmas(str)
        for turma in self.listaTurmas:
            str += 'CODIGO: ' + turma.getCodigo() + '\n'
            str += 'DISCIPLINA: ' + turma.getDisciplina().getCodigo() + '\n'
            str += 'ESTUDANTES:\n'
            for estud in turma.getEstudantes():
                str += estud.getNroMatric() + ' - ' + estud.getNome() + '\n'
            str += '------\n'

        self.limiteLista = LimiteMostraTurmas(str)
    
    def consultaTurmas(self):
        self.limiteCon = LimiteConsultaTurmas(self)

    def consultaHandler(self, event):
        try:
            if len(self.limiteCon.inputCode.get()) == 0:
                raise CampoVazio()
        except CampoVazio:
            str = 'DIGITE UM CODIGO DE DISCIPLINA PRIMEIRO'
            self.limiteCon.mostraJanela('FALHA', str)

        else:
            Code = self.limiteCon.inputCode.get()
            listaTurmaPorCodigo = []
            for trm in self.listaTurmas:
                if trm.getDisciplina().getCodigo() == Code:
                    listaTurmaPorCodigo.append(trm)
            if len(listaTurmaPorCodigo) == 0:
                str = ('NENHUMA TURMA POSSUI A DISCIPLINA COM O CODIGO {}'.format(Code))
                self.limiteCon.mostraJanela('Turma não encontrada', str)
                self.limiteCon.inputCode.delete(0, len(self.limiteCon.inputCode.get()))
            else:
                str = 'INFORMACOES DAS TURMAS COM A DISCIPLINA CONSULTADA:\n'
                for trm in listaTurmaPorCodigo:
                    str += 'CODIGO: ' + trm.getCodigo() + '\n'
                    str += 'DISCIPLINA: ' + trm.getDisciplina().getCodigo() +  ' - ' + trm.getDisciplina().getNome() + '\n'
                    str += 'ESTUDANTES:\n'
                    for estud in trm.getEstudantes():
                        str += estud.getNroMatric() + ' - ' + estud.getNome() + '\n'
                    str += '-----------------\n'
                self.limiteCon.mostraJanela('TURMA ENCONTRADA', str)
                self.limiteCon.inputCode.delete(0, len(self.limiteCon.inputCode.get()))
    
    def concluiHandler(self, event):
        self.limiteCon.destroy()
    
    def concluidoHandler(self, event):
        self.limiteIns.destroy()
    
