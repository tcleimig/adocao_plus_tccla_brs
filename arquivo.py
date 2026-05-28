import os

os.system('cls')

from entidade.usuário import User

def carregar_animais_arquivo(lista_animais):

    try:

        arquivo = open("animais.csv", "r", encoding="utf-8")

        for linha in arquivo:

            dados = linha.strip().split(";")

            animal = User(
                dados[1],
                dados[2],
                dados[3],
                dados[4],
                dados[5],
                dados[6],
                dados[7],
                int(dados[0])
            )

            lista_animais.append(animal)

        arquivo.close()

    except FileNotFoundError:

        arquivo = open("animais.csv", "w", encoding="utf-8")
        arquivo.close()

def salvar_animais_arquivo(lista_animais):

    arquivo = open("animais.csv", "w", encoding="utf-8")

    for animal in lista_animais:

        arquivo.write(animal.para_string_arquivo() + "\n")

    arquivo.close()
