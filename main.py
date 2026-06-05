import os

os.system('cls')

from datetime import datetime

from entidade.animal import User

from menu import Menu

from arquivo import salvar_animais_arquivo

from arquivo import carregar_animais_arquivo

from cuidados import Cuidado

from arquivo import salvar_cuidados_arquivo

from arquivo import carregar_cuidados_arquivo

lista_animais = []

carregar_animais_arquivo(lista_animais)

lista_cuidados = []

carregar_cuidados_arquivo(lista_cuidados)

def observe_opcao(opcao):     

    if opcao.isnumeric():

        if int(opcao) < 1 or int(opcao) > 5:

            return True
    
    elif opcao.isalpha():

        return True

def observe_valor_menu_animais():

    observe_valor = Menu.menu_animais()
    
    while observe_opcao(observe_valor):
        
        print("-" * 40)

        print("Erro: Valor inválido, tente novamente")

        observe_valor = Menu.menu_animais()
    
    return int(observe_valor)

def observar_base_de_dados(lista_valores):
    maior_id = 0

    for animal in lista_valores:
        if animal.pegar_id() > maior_id:
            maior_id = animal.pegar_id()

    return maior_id + 1

def observar_base_de_cuidados(lista_cuidados):
    maior_id = 0

    for cuidado in lista_cuidados:
        if cuidado.pegar_id() > maior_id:
            maior_id = cuidado.pegar_id()

    return maior_id + 1

def adicionar_animal(lista_animais):

    print("-" * 40)
    
    nome = input("Digite o nome do animal: ")
    
    especie = input("Digite a espécie do animal: ")
    
    raca = input("Digite a raça do animal: ")
    
    idade = input("Digite a idade do animal: ")
    
    estado_de_saude = input("Digite o estado de saúde do animal: ") 
    
    data_de_chegada = input("Digite a data de chegada do animal: ")
    
    comportamento = input("Digite o comportamento do animal: ")

    id = observar_base_de_dados(lista_animais)

    print("-" * 40)

    print("Animal cadastrado com sucesso!")

    return User(nome, especie, raca, idade, estado_de_saude, data_de_chegada, comportamento, id)

def salvar_animal(animal):

    lista_animais.append(animal)

    salvar_animais_arquivo(lista_animais)

def visualizar_animais():

    if len(lista_animais) > 0:

        print("-" * 40)

        print("Animais Cadastrados:")

        print("-" * 40)

        for animal in lista_animais:
            
            print(f"{animal.para_string()}")

    else:
        
        Menu.animal_nao_encontrado()
        
        print()
        
def procurar_animal(id):
    
    for animal in lista_animais:
    
        if animal.pegar_id() == id:

            return animal

def deletar_animal(id):

    visualizar_animais()

    print("-" * 40)
    
    id = int(input("Digite o Id do animal que você irá deletar: "))

    print("-" * 40)

    if len(lista_animais) > 0:

        animal = procurar_animal(id)
        
        if animal not in lista_animais or animal is None:
            
            print("-" * 40)

            print("Erro: Id inválido. Digite um Id cadastrado")

            return

        print(animal.para_string())

        print(f"animal na lista?: {animal in lista_animais}")

        lista_animais.remove(animal)

        salvar_animais_arquivo(lista_animais)

        print("-" * 40)

        print("Animal removido do sistema.")

    else:
        
       Menu.animal_nao_encontrado()

       print()

def atualizar_animal():

    visualizar_animais()

    print("-" * 40)

    id = int(input("Digite o Id do animal que deseja atualizar: "))
    
    animal = procurar_animal(id)

    if animal not in lista_animais or animal is None:

        print("-" * 40)

        print("Erro: Id inválido. Digite um Id cadastrado")

        return
    
    Menu.menu_atualizar()
    
    print("-" * 40)
    
    opcao = int(input("Digite o número de uma opção: "))

    while opcao != 8:
        
        if opcao == 1:

            estado_de_saude = input("Digite o estado de saúde atual do animal: ")

            animal.definir_estado_de_saude(estado_de_saude if len(estado_de_saude) != 0 else animal.pegar_estado_de_saude())

        elif opcao == 2:

            idade = input("Digite a idade atual do animal: ")
            
            animal.definir_idade(idade if len(idade) != 0 else animal.pegar_idade())

        elif opcao == 3:
            
            comportamento = input("Digite o comportamento atual do animal: ")

            animal.definir_comportamento(comportamento if len(comportamento) != 0 else animal.pegar_comportamento())

        elif opcao == 4:

            data_de_chegada = input("Digite a data de chegada do animal: ")

            animal.definir_data_de_chegada(data_de_chegada if len(data_de_chegada) != 0 else animal.pegar_data_de_chegada())

        elif opcao == 5:

            raca = input("Digite a raça do animal: ")

            animal.definir_raca(raca if len(raca) != 0 else animal.pegar_raca())

        elif opcao == 6:

            especie = input("Digite a espécie do animal: ")

            animal.definir_especie(especie if len(especie) != 0 else animal.pegar_especie())

        elif opcao == 7:

            nome = input("Digite o nome do animal: ")
            animal.definir_nome(nome if len(nome) != 0 else animal.pegar_nome())

        else:
            
            print("Valor inválido")
        
        Menu.menu_atualizar()        
        
        opcao = int(input("Digite o número de uma opção: "))
    
    salvar_animais_arquivo(lista_animais)

def adicionar_cuidado(lista_cuidados):

    visualizar_animais()

    print("-" * 40)

    if len(lista_animais) == 0:
        return

    
    id_animal = int(input("Digite o ID do animal relacionado ao cuidado: "))
    
    print("-" * 40)

    animal = procurar_animal(id_animal)

    if animal is None:
        
        ("-" * 40)

        print("Animal não encontrado.")
        return None

    tipo = input("Digite o cuidado/atividade previsto para o animal: ")
    data = input("Digite a data prevista do cuidado: ")

    hoje = datetime.now()

    data_brasil = datetime.strptime(data, "%d/%m/%Y")

    data_delta = data_brasil - hoje

    if data_delta.days < 0:
        
        print("-" * 40)

        print("Erro: a data do cuidado não pode ser anterior a hoje. Tente novamente")

        return None

    data_diferenca = str(data_delta.days)

    responsavel = input("Digite o responsável pelo cuidado: ")

    id = observar_base_de_cuidados(lista_cuidados)

    cuidado = Cuidado(id, id_animal, tipo, data, data_diferenca, responsavel)

    print("-" * 40)
    
    print("Cuidado cadastrado com sucesso!")

    return cuidado

def salvar_cuidado(cuidado):

    if cuidado is not None:

        lista_cuidados.append(cuidado)

        salvar_cuidados_arquivo(lista_cuidados)

def visualizar_cuidados():

    if len(lista_cuidados) > 0:

        print("-" * 40)
        print("Cuidados cadastrados:")

        for cuidado in lista_cuidados:

            animal = procurar_animal(cuidado.pegar_id_animal())

            if animal is not None:
                nome_animal = animal.pegar_nome()
            else:
                nome_animal = "Animal não encontrado"

            print(
                f"{cuidado.pegar_id()}: "
                f"{nome_animal} - "
                f"{cuidado.para_string()}"
            )

    else:
        print("-" * 40)
        print("Nenhum cuidado cadastrado.")
        

def procurar_cuidado(id):

    for cuidado in lista_cuidados:

        if cuidado.pegar_id() == id:

            return cuidado

def atualizar_cuidado():

    visualizar_cuidados()

    if len(lista_cuidados) == 0:
        return

    print("-" * 40)

    id = int(input("Digite o ID do cuidado que deseja atualizar: "))

    cuidado = procurar_cuidado(id)

    if cuidado is None:

        print("ID inválido.")
        return

    print("-" * 40)
    print("1 - Editar tipo")
    print("2 - Editar data")
    print("3 - Editar responsável")
    print("4 - Voltar")
    print("-" * 40)

    opcao = int(input("Digite uma opção: "))

    while opcao != 4:

        if opcao == 1:

            tipo = input("Digite o novo tipo: ")

            cuidado.definir_tipo(
                tipo if len(tipo) != 0 else cuidado.pegar_tipo()
            )

        elif opcao == 2:

            data = input("Digite a nova data: ")

            cuidado.definir_data(
                data if len(data) != 0 else cuidado.pegar_data()
            )

        elif opcao == 3:

            responsavel = input("Digite o novo responsável: ")

            cuidado.definir_responsavel(
                responsavel if len(responsavel) != 0 else cuidado.pegar_responsavel()
            )

        else:

            print("Valor inválido.")

        print("-" * 40)
        print(cuidado.para_string())
        print("-" * 40)

        print("-" * 40)
        print("1 - Editar tipo")
        print("2 - Editar data")
        print("3 - Editar responsável")
        print("4 - Voltar")
        print("-" * 40)

        opcao = int(input("Digite uma opção: "))

    salvar_cuidados_arquivo(lista_cuidados)

def deletar_cuidado():

    visualizar_cuidados()

    if len(lista_cuidados) == 0:
        return

    id = int(input("Digite o ID do cuidado que deseja deletar: "))

    cuidado = procurar_cuidado(id)

    if cuidado is None:

        print("ID inválido. Digite um ID cadastrado.")
        return

    lista_cuidados.remove(cuidado)

    salvar_cuidados_arquivo(lista_cuidados)

    print("-" * 40)
    print("Cuidado removido do sistema.")

def menu_animais_sistema():

    valor = observe_valor_menu_animais()

    while valor != 5:

        if valor == 1:
            salvar_animal(adicionar_animal(lista_animais))

        elif valor == 2:
            visualizar_animais()

        elif valor == 3:
            atualizar_animal()

        elif valor == 4:
            deletar_animal(id)

        valor = observe_valor_menu_animais()

def menu_cuidados_sistema():

    opcao = Menu.menu_cuidados()

    while opcao != "5":

        if opcao == "1":
            salvar_cuidado(adicionar_cuidado(lista_cuidados))

        elif opcao == "2":
            visualizar_cuidados()

        elif opcao == "3":
            atualizar_cuidado()

        elif opcao == "4":
            deletar_cuidado()

        else:
            print("Valor inválido.")

        opcao = Menu.menu_cuidados()

def main():

    opcao = Menu.menu_inicio()

    while opcao != "3":

        if opcao == "1":
            menu_animais_sistema()

        elif opcao == "2":
            menu_cuidados_sistema()

        else:
            print("-" * 40)
            
            print("Valor inválido.")

        opcao = Menu.menu_inicio()

if __name__ == "__main__":
    
    main()


