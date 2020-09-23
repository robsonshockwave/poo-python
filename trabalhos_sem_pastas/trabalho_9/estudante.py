import tkinter as tk
from tkinter import messagebox

class CampoVazio(Exception):
    pass

class PreenchaTudo(Exception):
    pass

class MatricRepetida(Exception):
    pass

class alunoJaCadastrado(Exception):
    pass

class Estudante:

    def __init__(self, nroMatric, nome):
        self.__nroMatric = nroMatric
        self.__nome = nome

    def getNroMatric(self):
        return self.__nroMatric
    
    def getNome(self):
        return self.__nome

class LimiteInsereEstudantes(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("ESTUDANTE")
        self.controle = controle

        self.frameNro = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelNro = tk.Label(self.frameNro,text="NUMERO MATRICULA: ")
        self.labelNome = tk.Label(self.frameNome,text="NOME:              ")
        self.labelNro.pack(side="left")
        self.labelNome.pack(side="left")  

        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="INSERIR", font = ('Negrito', 9))      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.insereHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="LIMPAR", font = ('Negrito', 9))      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="CONCLUIDO", font = ('Negrito', 9))      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraEstudantes():
    def __init__(self, str):
        messagebox.showinfo('LISTA DE ALUNOS', str)

class LimiteConsultaEstudantes(tk.Toplevel):

    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('280x60')
        self.title("CONSULTAR ESTUDANTE")
        self.controle = controle

        self.frameMatric = tk.Frame(self)
        self.frameButtons = tk.Frame(self)
        self.frameMatric.pack()
        self.frameButtons.pack()

        self.labelMatric = tk.Label(self.frameMatric, text = 'MATRICULA:  ')
        self.labelMatric.pack(side = 'left')

        self.inputMatric = tk.Entry(self.frameMatric, width = 20)
        self.inputMatric.pack(side = 'left')

        self.buttonConsulta = tk.Button(self.frameButtons, text = 'CONSULTAR', font = ('Negrito', 9))
        self.buttonConsulta.pack(side = 'left')
        self.buttonConsulta.bind("<Button>", controle.consultaHandler)

        self.buttonConcluido = tk.Button(self.frameButtons, text = 'CONCLUIDO', font = ('Negrito', 9))
        self.buttonConcluido.pack(side = 'left')
        self.buttonConcluido.bind("<Button>", controle.concluiHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
      
class CtrlEstudante():       
    def __init__(self):
        self.listaEstudantes = [
            Estudante('1001', 'Kurt Cobain'),
            Estudante('1002', 'Raul Seixas'),
            Estudante('1003', 'Elton John'),
            Estudante('1004', 'Raul Gil')
        ]

    def getEstudante(self, nroMatric):
        estRet = None
        for est in self.listaEstudantes:
            if est.getNroMatric() == nroMatric:
                estRet = est
        return estRet

    def getListaNroMatric(self):
        listaNro = []
        for est in self.listaEstudantes:
            listaNro.append(est.getNroMatric())
        return listaNro

    def insereEstudantes(self):
        self.limiteIns = LimiteInsereEstudantes(self) 

    def mostraEstudantes(self):
        if len(self.listaEstudantes) == 0:
            str = "NAO HA ALUNOS CADASTRADOS"
            self.limiteLista = LimiteMostraEstudantes(str)
        else:
            str = "NUM. MATRIC. -- NOME\n"
            for est in self.listaEstudantes:
                str += est.getNroMatric() + ' -- ' + est.getNome() + '\n'
            self.limiteLista = LimiteMostraEstudantes(str)
    
    def consultaEstudantes(self):
        self.limiteCon = LimiteConsultaEstudantes(self)

    def insereHandler(self, event):
        try:
            if len(self.limiteIns.inputNro.get()) == 0 or len(self.limiteIns.inputNome.get()) == 0:
                raise PreenchaTudo()
            for estud in self.listaEstudantes:
                if estud.getNroMatric() == self.limiteIns.inputNro.get() and estud.getNome() == self.limiteIns.inputNome.get():
                    raise alunoJaCadastrado()
                if estud.getNroMatric() == self.limiteIns.inputNro.get():
                    raise MatricRepetida()
        except alunoJaCadastrado:
            self.limiteIns.mostraJanela('CADASTRO NAO PERMITIDO', 'ESTE JA FOI CADASTRADO')
        except PreenchaTudo:
            self.limiteIns.mostraJanela('CADASTRO NAO PERMITIDO', 'PREENCHA TODOS OS CAMPOS')
        except MatricRepetida:
            self.limiteIns.mostraJanela('CADASTRO NAO PERMITIDO', 'ESTA MATRICULA JA ESTA EM USO')

        else:
            nroMatric = self.limiteIns.inputNro.get()
            nome = self.limiteIns.inputNome.get()
            estudante = Estudante(nroMatric, nome)
            self.listaEstudantes.append(estudante)
            self.limiteIns.mostraJanela('CONGRULATIONS', 'ESTUDANTE CADASTRADO COM SUCESSO')
            self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
    
    def consultaHandler(self, event):
        try:
            if len(self.limiteCon.inputMatric.get()) == 0:
                raise CampoVazio()
        except CampoVazio:
            str = 'DIGITE O NUMERO DE MATRICULA PRIMEIRO'
            self.limiteCon.mostraJanela('FALHA', str)
            
        else:
            Matric = self.limiteCon.inputMatric.get()
            est = self.getEstudante(Matric)
            if est == None:
                str = ('NENHUM ALUNO POSSUI A MATRICULA {}'.format(Matric))
                self.limiteCon.mostraJanela('ALUNO NAO ENCONTRADO', str)
                self.limiteCon.inputMatric.delete(0, len(self.limiteCon.inputMatric.get()))
            else:
                str = 'INFORMACOES DO ALUNO CONSULTADO:\n'
                str += 'NUM. MATRIC. -- NOME\n'
                str += est.getNroMatric() + ' -- ' + est.getNome()
                self.limiteCon.mostraJanela('ALUNO ENCONTRADO', str)
                self.limiteCon.inputMatric.delete(0, len(self.limiteCon.inputMatric.get()))

    def concluiHandler(self, event):
        self.limiteCon.destroy()