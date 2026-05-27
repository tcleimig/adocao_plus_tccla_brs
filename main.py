import os

os.system('cls')

from entidade.usuário import User

from menu import Menu

lista_animais = []

def observe_opcao(opcao):     

    if opcao.isnumeric():

        if int(opcao) < 1 or int(opcao) > 5:

            return True
    
    elif opcao.isalpha():

        return True

def observe_valor_menu():

    observe_valor = Menu.menu_principal()
    
    while observe_opcao(observe_valor):
        
        print("-" * 40)

        print("Valor inválido, tente novamente")

        print("-" * 40)

        observe_valor = Menu.menu_principal()
    
    return int(observe_valor)

def observar_base_de_dados(lista_valores):
    
    return len(lista_valores) + 1

def adicionar_animal(lista_animais):

    print("-" * 40)
    
    nome = input("Digite o nome do animal: ")
    
    especie = input("Digite a espécie do animal: ")
    
    raca = input("Digite a raça do animal: ")
    
    idade = input("Digite a idade do animal: ")
    
    estado_de_saude = input("Digite o estado de saúde do animal: ") 
    
    data_de_chegada = input("Digite a data em que o animal chegou no centro: ")
    
    comportamento = input("Digite o comportamento do animal: ")

    id = observar_base_de_dados(lista_animais)

    print("-" * 40)

    print("Animal cadastrado com sucesso!")

    print("-" * 40)

    return User(nome, especie, raca, idade, estado_de_saude, data_de_chegada, comportamento, id)

def salvar_animal(animal):

    lista_animais.append(animal)

def visualizar_animais():

    if len(lista_animais) > 0:
        
        print("-" * 40)

        print("Animais Cadastrados:")

        for animal in lista_animais:
            
            print(f"{animal.para_string()}")

        print("-" * 40)

    else:
        
        Menu.animal_nao_encontrado()
        
        print()
        
def procurar_animal(id):
    
    for animal in lista_animais:
    
        if animal.pegar_id() == id:

            return animal

def deletar_animal(id):

    visualizar_animais()

    id = int(input("Digite o Id do animal que você irá deletar: "))

    if len(lista_animais) > 0:

        animal = procurar_animal(id)

        print("-" * 40)
        
        if animal not in lista_animais or animal is None:
            
            print("Id inválido. Digite um Id cadastrado")

            print("-" * 40)

            return

        print(animal.para_string())

        print(f"animal na lista?: {animal in lista_animais}")

        lista_animais.remove(animal)

        print("-" * 40)

        print("Animal removido do sistema.")

        print("-" * 40)

    else:
        
       Menu.animal_nao_encontrado()

       print()

def atualizar_animal():

    visualizar_animais()

    id = int(input("Digite o Id do animal que deseja atualizar: "))
    
    animal = procurar_animal(id)

    if animal not in lista_animais or animal is None:
            
        print("Id inválido. Digite um Id cadastrado")

        print("-" * 40)

        return
    
    Menu.menu_atualizar()
    
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
    
    print(animal.para_string())

    print("-" * 40)

def main():

    valor = observe_valor_menu()

    while valor != 5:

        if (valor == 1):

            salvar_animal(adicionar_animal(lista_animais))

        if (valor == 2):
            
            visualizar_animais()

        if (valor == 3):
            
            atualizar_animal()

        if (valor == 4):
            
            deletar_animal(id)

        valor = observe_valor_menu()

if __name__ == "__main__":
    
    main()

