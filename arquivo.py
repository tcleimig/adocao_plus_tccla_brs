from entidade.animal import User

from entidade.cuidados import Cuidado

from entidade.adotante import Adotante

def salvar_cuidados_arquivo(lista_cuidados):

    arquivo = open("cuidados.csv", "w", encoding="utf-8")

    for cuidado in lista_cuidados:

        arquivo.write(cuidado.para_string_arquivo() + "\n")

    arquivo.close()

def carregar_cuidados_arquivo(lista_cuidados):

    try:

        arquivo = open("cuidados.csv", "r", encoding="utf-8")

        for linha in arquivo:

            dados = linha.strip().split(";")

            if len(dados) == 6:

                cuidado = Cuidado(
                    int(dados[0]),
                    int(dados[1]),
                    dados[2],
                    dados[3],
                    dados[4],
                    dados[5]
                )

                lista_cuidados.append(cuidado)

        arquivo.close()

    except FileNotFoundError:

        arquivo = open("cuidados.csv", "w", encoding="utf-8")
        arquivo.close()

def carregar_animais_arquivo(lista_animais):

    try:

        arquivo = open("animais.csv", "r", encoding="utf-8")

        for linha in arquivo:

            dados = linha.strip().split(";")

            if len (dados) == 8:

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

def salvar_adotantes_arquivo(lista_adotantes):

    arquivo = open("adotante.csv", "w", encoding="utf-8")

    for adotante in lista_adotantes:

        arquivo.write(adotante.para_string_arquivo() + "\n")

    arquivo.close()

def carregar_adotantes_arquivo(lista_adotantes):

    try:

        arquivo = open("adotante.csv", "r", encoding="utf-8")

        for linha in arquivo:

            dados = linha.strip().split(";")

            if len(dados) == 7:

                adotante = Adotante(
                    int(dados[0]),
                    dados[1],
                    int(dados[2]),
                    dados[3],
                    dados[4],
                    int(dados[5]),
                    dados[6]
                )

                lista_adotantes.append(adotante)

        arquivo.close()

    except FileNotFoundError:

        arquivo = open("adotante.csv", "w", encoding="utf-8")
        arquivo.close()






