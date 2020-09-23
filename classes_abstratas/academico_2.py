from abc import ABC, abstractclassmethod

class Person(ABC):
    def __init__(self, name, address, age, subjectList):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__subjectList = subjectList

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getAge(self):
        return self.__age

    def getSubjectList(self):
        return self.__subjectList

    @abstractclassmethod
    def printDescription(self):
        pass


class Professor(Person):
    def __init__(self, name, address, age, titulation, subjectList):
        super().__init__(name, address, age, subjectList)
        self.__titulation = titulation

    def getTitulation(self):
        return self.__titulation

    def printDescription(self):
        print('Nome: {}'.format(self.getName()))
        print('Endereço: {}'.format(self.getAddress()))
        print('Idade: {}'.format(self.getAge()))
        print('Titulação: {}'.format(self.getTitulation()))
        print('Assuntos ministrados')
        subjectList = self.getSubjectList()
        for subj in subjectList:
            print('Name: {} - Schedule hourly: {}'.format(subj.getNameSubject(),
                                                          subj.getScheduleHourly()))


class Student(Person):
    def __init__(self, name, address, age, major, subjectList):
        super().__init__(name, address, age, subjectList)
        self.__major = major

    def getMajor(self):
        return self.__major

    def printDescription(self):
        print('Nome: {}'.format(self.getName()))
        print('Endereço: {}'.format(self.getAddress()))
        print('Idade: {}'.format(self.getAge()))
        print('Grau: {}'.format(self.getMajor()))
        print('Assuntos estudados')
        subjectList = self.getSubjectList()
        for subj in subjectList:
            print('Name: {} - Schedule hourly: {}'.format(subj.getNameSubject(),
                                                          subj.getScheduleHourly()))


class Subject():
    def __init__(self, subjectName, scheduleHourly):
        self.__subjectName = subjectName
        self.__scheduleHourly = scheduleHourly

    def getSubjectName(self):
        return self.__subjectName

    def getScheduleHourly(self):
        return self.__scheduleHourly


subject1 = Subject('Engenharia de Software', 64)
subject2 = Subject('Estrutura de Dados 2', 64)
subject3 = Subject('Banco de Dados', 64)
subjectList1 = [subject1, subject2]
subjectList2 = [subject2, subject3]

prof = Professor('Olabama', 'Av.BPS, 1133', 58, 'Doutorado', subjectList1)

prof.printDescription()

print()

student = Professor('Robson', 'Rua dos Operários', 22, 'Mestrado', subjectList2)

student.printDescription()
