from datetime import datetime

class User:
    
    def __init__(self, nome, especie, raca, idade, estado_de_saude, data_brasil1, comportamento, id):

        self.__id = id
        
        self.__nome = nome
        
        self.__especie = especie
        
        self.__raca = raca
        
        self.__idade = idade
        
        self.__estado_de_saude = estado_de_saude
        
        self.__data_brasil1 = data_brasil1
        
        self.__comportamento = comportamento

        self.__adotante = None

    def pegar_id(self):

        return self.__id

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
    
    def pegar_data_brasil1(self):

        return self.__data_brasil1
    
    def pegar_comportamento(self):

        return self.__comportamento
    
    def pegar_adotante(self):

        return self.__adotante
    
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

    def definir_data_brasil1(self, data_brasil1):
        
        self.__data_brasil1 = data_brasil1
    
    def definir_comportamento(self, comportamento):
        
        self.__comportamento = comportamento

    def definir_adotante(self, adotante):

        self.__adotante = adotante

    def __limpar_data(self):
        
        data_errada = self.pegar_data_brasil1()

        data_formatada = str(data_errada)

        try:
            
            if "-" in data_formatada:

                data_limpa = data_formatada.split(" ")[0]
                
                objeto_data = datetime.strptime(data_limpa, "%Y-%m-%d")

                data_correta = objeto_data.strftime("%d/%m/%Y")

            else:

                data_correta = data_formatada

        except:

            data_correta = data_formatada

        return data_correta

    def para_string(self):
        
        data_correta = self.__limpar_data()     
        
        return f"{self.pegar_id()}: {self.pegar_nome()} - {self.pegar_especie()} - {self.pegar_raca()} - {self.pegar_idade()} anos - {self.pegar_estado_de_saude()} - {data_correta} - {self.pegar_comportamento()}"

    def para_string_arquivo(self):
        
        data_correta = self.__limpar_data()
        
        return f"{self.pegar_id()};{self.pegar_nome()};{self.pegar_especie()};{self.pegar_raca()};{self.pegar_idade()} anos;{self.pegar_estado_de_saude()};{data_correta};{self.pegar_comportamento()}"
    