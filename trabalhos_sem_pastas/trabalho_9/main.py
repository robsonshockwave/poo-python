import tkinter as tk
from tkinter import messagebox
import estudante as est
import disciplina as disc
import turma as trm

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.estudanteMenu = tk.Menu(self.menubar)
        self.discipMenu = tk.Menu(self.menubar)
        self.turmaMenu = tk.Menu(self.menubar)     

        self.estudanteMenu.add_command(label="INSERE", \
                    command=self.controle.insereEstudantes)
        self.estudanteMenu.add_command(label="MOSTRA", \
                    command=self.controle.mostraEstudantes)
        self.estudanteMenu.add_command(label="CONSULTA", \
                    command=self.controle.consultaEstudantes)
        self.menubar.add_cascade(label="ESTUDANTE", \
                    menu=self.estudanteMenu)

        self.discipMenu.add_command(label="INSERE", \
                    command=self.controle.insereDisciplinas)
        self.discipMenu.add_command(label="MOSTRA", \
                    command=self.controle.mostraDisciplinas)
        self.discipMenu.add_command(label="CONSULTA", \
                    command=self.controle.consultaDisciplinas)        
        self.menubar.add_cascade(label="DISCIPLINA", \
                    menu=self.discipMenu)

        self.turmaMenu.add_command(label="INSERE", \
                    command=self.controle.insereTurmas)
        self.turmaMenu.add_command(label="MOSTRA", \
                    command=self.controle.mostraTurmas)
        self.turmaMenu.add_command(label="CONSULTA", \
                    command=self.controle.consultaTurmas)                     
        self.menubar.add_cascade(label="TURMA", \
                    menu=self.turmaMenu)        

        self.root.config(menu=self.menubar)

class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlEstudante = est.CtrlEstudante()
        self.ctrlDisciplina = disc.CtrlDisciplina()
        self.ctrlTurma = trm.CtrlTurma(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("EXEMPLO MVC")

        self.root.mainloop()
    
    def insereEstudantes(self):
        self.ctrlEstudante.insereEstudantes()

    def mostraEstudantes(self):
        self.ctrlEstudante.mostraEstudantes()
    
    def consultaEstudantes(self):
        self.ctrlEstudante.consultaEstudantes()

    def insereDisciplinas(self):
        self.ctrlDisciplina.insereDisciplinas()

    def mostraDisciplinas(self):
        self.ctrlDisciplina.mostraDisciplinas()
    
    def consultaDisciplinas(self):
        self.ctrlDisciplina.consultaDisciplinas()

    def insereTurmas(self):
        self.ctrlTurma.insereTurmas()

    def mostraTurmas(self):
        self.ctrlTurma.mostraTurmas()
    
    def consultaTurmas(self):
        self.ctrlTurma.consultaTurmas()

if __name__ == '__main__':
    c = ControlePrincipal()