from abc import ABC, abstractclassmethod

class Person(ABC):
    def __init__(self, name, address, age, disciplineList):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__disciplineList = disciplineList

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getAge(self):
        return self.__age

    def getDisciplineList(self):
        return self.__disciplineList

    def insertDiscipline(self, disc):
        self.__disciplineList.append(disc)

    @abstractclassmethod
    def printDescription(self):
        pass


class Professor(Person):
    def __init__(self, name, address, age, titulation, disciplineList):
        super().__init__(name, address, age, disciplineList)
        self.__titulation = titulation

    def getTitulation(self):
        return self.__titulation

    def printDescription(self):
        print('Nome: {}'.format(self.getName()))
        print('Endereço: {}'.format(self.getAddress()))
        print('Idade: {}'.format(self.getAge()))
        print('Titulação: {}'.format(self.getTitulation()))
        print('Disciplines ministradas')
        disciplineList = self.getDisciplineList()
        for disc in disciplineList:
            print('Nome: {} - total de horas: {}'.format(disc.getDisciplineName(),
                                                          disc.getScheduleHourly()))


class Student(Person):
    def __init__(self, name, address, age, major, disciplineList):
        super().__init__(name, address, age, disciplineList)
        self.__major = major

    def getMajor(self):
        return self.__major

    def printDescription(self):
        print('Nome: {}'.format(self.getName()))
        print('Endereço: {}'.format(self.getAddress()))
        print('Idade: {}'.format(self.getAge()))
        print('Grau: {}'.format(self.getMajor()))
        print('Disciplines tomadas')
        disciplineList = self.getDisciplineList()
        for disc in disciplineList:
            print('Nome: {} - total de horas: {}'.format(disc.getDisciplineName(),
                                                          disc.getScheduleHourly()))


class Discipline():
    def __init__(self, disciplineName, scheduleHourly):
        self.__disciplineName = disciplineName
        self.__scheduleHourly = scheduleHourly

    def getDisciplineName(self):
        return self.__disciplineName

    def getScheduleHourly(self):
        return self.__scheduleHourly


subject1 = Discipline('Engenharia de Software', 64)
subject2 = Discipline('Estrutura de Dados 2', 64)
subject3 = Discipline('Banco de Dados', 64)

prof = Professor('Olabama', 'Av.BPS, 1133', 58, 'Doutorado', [])
prof.insertDiscipline(subject1)
prof.insertDiscipline(subject2)

prof.printDescription()

print()

student = Professor('Robson', 'Rua dos Operários', 22, 'Mestrado', [])
student.insertDiscipline(subject2)
student.insertDiscipline(subject3)

student.printDescription()

student.insertDiscipline(subject1)

print()

student.printDescription()
