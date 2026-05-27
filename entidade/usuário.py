class User:
    def __init__(self, nome, especie, raca, idade, estado_de_saude, data_de_chegada, comportamento, id):

        self.__nome = nome
        
        self.__especie = especie
        
        self.__raca = raca
        
        self.__idade = idade
        
        self.__estado_de_saude = estado_de_saude
        
        self.__data_de_chegada = data_de_chegada
        
        self.__comportamento = comportamento

        self.__id = id

    def pegar_nome(self):

        return self.__nome
    
    def pegar_especie(self):

        return self.__especie
    
    def pegar_raca(self):

        return self.__raca
    
    def pegar_idade(self):

        return self.__idade
    
    def pegar_estado_de_saude(self):

        return self.__estado_de_saude
    
    def pegar_data_de_chegada(self):

        return self.__data_de_chegada
    
    def pegar_comportamento(self):

        return self.__comportamento
    
    def pegar_id(self):

        return self.__id
    
    def definir_nome(self, nome):
        
        self.__nome = nome

    def definir_especie(self, especie):
        
        self.__especie = especie

    def definir_raca(self, raca):
        
        self.__raca = raca

    def definir_idade(self, idade):
        
        self.__idade = idade

    def definir_estado_de_saude(self, estado_de_saude):
        
        self.__estado_de_saude = estado_de_saude

    def definir_data_de_chegada(self, data_de_chegada):
        
        self.__data_de_chegada = data_de_chegada
    
    def definir_comportamento(self, comportamento):
        
        self.__comportamento = comportamento

    def para_string(self):
        return f"{self.pegar_id()}: {self.pegar_nome()} - {self.pegar_especie()} - {self.pegar_raca()} - {self.pegar_idade()} - {self.pegar_estado_de_saude()} - {self.pegar_data_de_chegada()} - {self.pegar_comportamento()}"

    
    