from abc import ABC, abstractclassmethod

class Person(ABC):
    def __init__(self, name, address, age):
        self.__name = name
        self.__address = address
        self.__age = age

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getAge(self):
        return self.__age

    @abstractclassmethod
    def printDescription(self):
        pass


class Professor(Person):
    def __init__(self, name, address, age, titulation):
        super().__init__(name, address, age)
        self.__titulation = titulation

    def getTitulation(self):
        return self.__titulation

    def printDescription(self):
        print('Name: {}'.format(self.getName()))
        print('Address: {}'.format(self.getAddress()))
        print('Age: {}'.format(self.getAge()))
        print('Titulation: {}'.format(self.getTitulation()))


class Student(Person):
    def __init__(self, name, address, age, major):
        super().__init__(name, address, age)
        self.__major = major

    def getMajor(self):
        return self.__major

    def printDescription(self):
        print('Nome: {}'.format(self.getName()))
        print('Endereço: {}'.format(self.getAddress()))
        print('Idade: {}'.format(self.getAge()))
        print('Grau: {}'.format(self.getMajor()))


prof = Professor('Olabama', 'Av.BPS, 1133', 58, 'Doutorado')

prof.printDescription()

print()

student = Professor('Robson', 'Rua dos Operários', 22, 'Mestrado')

student.printDescription()
