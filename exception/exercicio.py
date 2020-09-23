#Definir nossas exceptions

class UsernameDuplicado(Exception):
    pass

class IdadeInvalida(Exception):
    pass

class IdadeMenorQuePermitida(Exception):
    pass

class EmailInvalido(Exception):
    pass

#Classe para conter os dados dos usuários

class User:

    def __init__(self, username, email):
        self.__username = username
        self.__email = email

    def getUsername(self):
        return self.__username

    def getEmail(self):
        return self.__email

listaExemplo = [
    ("paulo", "paulo@gmail.com", 21),
    ("maria", "maria@gmail.com", 19),
    ("antonio", "antonio@gmail.com", 25),
    ("pedro", "pedro@gmail.com", 15),
    ("marisa", "marisa", 23),
    ("ana", "ana@gmail.com", -3),
    ("maria", "maria2@gmail.com", 27)
]        

cadastro = {}

for username, email, idade in listaExemplo:
    try:
        if username in cadastro:
            raise UsernameDuplicado()
        if idade < 0:
            raise IdadeInvalida()
        if idade < 18:
            raise IdadeMenorQuePermitida()

        emailPartes = email.split('@')
        if len(emailPartes) != 2 or not emailPartes[0] or not emailPartes[1]:
            raise EmailInvalido()

    except UsernameDuplicado:
        print("Username '%s' já está em uso" % username)
    except IdadeInvalida:
        print("Idade inválida: %d" % idade)
    except IdadeMenorQuePermitida:
        print("Usuário %s tem idade inferior a permitida" % username)
    except EmailInvalido:
        print("'%s' não é um endereço de email válido" % email)
    
    else:
        cadastro[username] = User(username, email)