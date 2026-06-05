class Cuidado:

    def __init__(self, id, id_animal, tipo, data, data_diferenca, responsavel):

        self.__id = id
        
        self.__id_animal = id_animal
        
        self.__tipo = tipo
        
        self.__data = data
        
        self.__data_diferenca = data_diferenca
        
        self.__responsavel = responsavel

    def definir_tipo(self, tipo):
        self.__tipo = tipo

    def definir_data(self, data):
        self.__data = data

    def definir_data_diferenca(self, data_diferenca):
        self.__data_diferenca = data_diferenca
    
    def definir_responsavel(self, responsavel):
        self.__responsavel = responsavel

    def pegar_id(self):
        return self.__id

    def pegar_id_animal(self):
        return self.__id_animal

    def pegar_tipo(self):
        return self.__tipo

    def pegar_data(self):
        return self.__data

    def pegar_data_diferenca(self):
        return self.__data_diferenca
    
    def pegar_responsavel(self):
        return self.__responsavel

    def para_string(self):
        return f"{self.pegar_tipo()} - {self.pegar_data()} - {self.pegar_data_diferenca()} dias para o cuidado - {self.pegar_responsavel()}"
    
    def para_string_arquivo(self):
        return f"{self.pegar_id()};{self.pegar_id_animal()};{self.pegar_tipo()};{self.pegar_data()};{self.pegar_data_diferenca()} dias para o cuidado;{self.pegar_responsavel()}"