from datetime import datetime

class Cuidado:

    def __init__(self, id, id_animal, tipo, data_brasil2, data_diferenca, responsavel):

        self.__id = id
        
        self.__id_animal = id_animal
        
        self.__tipo = tipo
        
        self.__data_brasil2 = data_brasil2
        
        self.__data_diferenca = data_diferenca
        
        self.__responsavel = responsavel

    def definir_tipo(self, tipo):
        self.__tipo = tipo

    def definir_data_brasil2(self, data_brasil2):
        self.__data_brasil2 = data_brasil2

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

    def pegar_data_brasil2(self):
        return self.__data_brasil2

    def pegar_data_diferenca(self):
        return self.__data_diferenca
    
    def pegar_responsavel(self):
        return self.__responsavel
    
    def __limpar_data(self):
        
        data_errada = self.pegar_data_brasil2()

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
        
        return f"{self.pegar_tipo()} - {data_correta} - {self.pegar_data_diferenca()} dias para o cuidado - {self.pegar_responsavel()}"
    
    def para_string_arquivo(self):
        
        data_correta = self.__limpar_data()
        
        return f"{self.pegar_id()};{self.pegar_id_animal()};{self.pegar_tipo()};{data_correta};{self.pegar_data_diferenca()} dias para o cuidado;{self.pegar_responsavel()}"