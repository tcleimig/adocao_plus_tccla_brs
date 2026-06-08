class Adotante:

    def __init__(self, id, nome_adotante, CPF, idade_adotante, endereco, telefone, email):

        self.__id = id
        
        self.__nome_adotante = nome_adotante
        
        self.__CPF = CPF
        
        self.__idade_adotante = idade_adotante
        
        self.__endereco = endereco

        self.__telefone = telefone

        self.__email = email

    def definir_nome_adotante(self, nome_adotante):
        self.__nome_adotante = nome_adotante

    def definir_CPF(self, CPF):
        self.__CPF = CPF

    def definir_idade_adotante(self, idade_adotante):
        self.__idade_adotante = idade_adotante
    
    def definir_endereco(self, endereco):
        self.__endereco = endereco

    def definir_telefone(self, telefone):
        self.__telefone = telefone

    def definir_email(self, email):
        self.__email = email
    
    def pegar_id(self):
        return self.__id
    
    def pegar_nome_adotante(self):
        return self.__nome_adotante
    
    def pegar_CPF(self):
        return self.__CPF
    
    def pegar_idade_adotante(self):
        return self.__idade_adotante
    
    def pegar_endereco(self):
        return self.__endereco
    
    def pegar_telefone(self):
        return self.__telefone

    def pegar_email(self):
        return self.__email
    
    def pegar_animais_para_conhecer(self):
        return self.__animais_para_conhecer

    def para_string(self):
        return f"{self.pegar_id()}: {self.pegar_nome_adotante()} - {self.pegar_CPF()} - {self.pegar_idade_adotante()} anos - {self.pegar_endereco()} - {self.pegar_telefone} - {self.pegar_email}"
    
    def para_string_arquivo(self):
        return f"{self.pegar_id()};{self.pegar_nome_adotante()};{self.pegar_CPF()};{self.pegar_idade_adotante()} anos;{self.pegar_endereco()};{self.pegar_telefone};{self.pegar_email}"