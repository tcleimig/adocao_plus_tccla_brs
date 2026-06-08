class Menu:
    def __init__(self):
        pass

    def menu_inicio():

        print("-" * 40)
        print("Adoção+ - MENU PRINCIPAL")
        print("-" * 40)

        return input(
            "1 - Gerenciar animais\n"
            "2 - Gerenciar adotantes\n"
            "3 - Gerenciar cuidados e atividades\n"
            "4 - Sugestões personalizadas\n"
            "5 - Sair do sistema\n")
     
    def menu_animais():
       
        print("-" * 40)

        print("Adoção+ - GERENCIAMENTO DE ANIMAIS")

        print("-" * 40) 
        
        return input("1 - Adicionar animal\n2 - Visualizar animais no sistema\n3 - Editar informações de um animal\n4 - Deletar um animal do sistema\n5 - Voltar ao menu principal\n")
    
    def menu_atualizar():

        print("-" * 40)

        print("1 - Editar estado de saúde\n2 - Editar idade do animal\n3 - Editar comportamento do animal \n4 - Editar data de chegada do animal\n5 - Editar raça do animal\n6 - Editar espécie do animal\n7 - Editar nome do animal\n8 - Parar de atualizar")
        
        print("-" * 40)

    def animal_nao_encontrado():
        
        print("-" * 40)

        print("Erro: Nenhum animal cadastrado")

        print("-" * 40)

    def adotante_nao_encontrado():
        
        print("-" * 40)

        print("Erro: Nenhum cadastro foi feito ainda!")

        print("-" * 40)

    def menu_adotantes():
       
        print("-" * 40)

        print("Adoção+ - GERENCIAMENTO DE ADOTANTES")

        print("-" * 40) 
        
        return input("1 - Fazer seu cadastro\n2 - Visualizar adotantes cadastrados no sistema\n3 - Editar informações de um adotante\n4 - Deletar um adotante do sistema\n5 - Voltar ao menu principal\n")

    def menu_cuidados():

        print("-" * 40)
        print("Adoção+ - GERENCIAMENTO DE CUIDADOS")
        print("-" * 40)

        return input(
            "1 - Adicionar cuidado\n"
            "2 - Visualizar cuidados\n"
            "3 - Editar cuidado\n"
            "4 - Deletar cuidado\n"
            "5 - Voltar ao menu principal\n"
        )
    
    def menu_atualizar_adotante():

        print("-" * 40)

        print("1 - Editar nome\n2 - Editar CPF\n3 - Editar idade\n4 - Editar endereço\n5 - Editar telefone\n6 - Editar email\n7 - Parar de atualizar")

        