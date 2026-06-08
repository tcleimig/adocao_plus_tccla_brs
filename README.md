# Adoção+

Adoção+ é um sistema com função controlar e gerenciar informações sobre adoções, cuidados, vacinas e etc. criado por Tiago Leimig e Bruno Ramos para a matéria de Fundamentos de Programação da Faculdade C.E.S.A.R School.

ao iniciar o sistema essa tela irá aparecer:

----------------------------------------
Adoção+ - MENU PRINCIPAL
----------------------------------------
1 - Gerenciar animais
2 - Gerenciar adotantes
3 - Gerenciar cuidados e atividades
4 - Sugestões personalizadas
5 - Sair do sistema

cada tela possui uma variação desse sistema para escolher uma opção você precisa digitar um dos números para ir a outro menu.

ao digitar 1 o menu de gerenciamento de animais é aberto:

----------------------------------------
Adoção+ - GERENCIAMENTO DE ANIMAIS
----------------------------------------
1 - Adicionar animal <----
2 - Visualizar animais no sistema
3 - Editar informações de um animal
4 - Deletar um animal do sistema
5 - Voltar ao menu principal

mesma coisa do primeiro digite um número para selecionar uma opção, precisa ser o número na frente da opção, outros números ou letras irão falhar.

ao digitar 1 e apertar enter aparecem estas opções para adicionar as informações do animal, aqui vou usar o exemplo de Kiki:

----------------------------------------
Digite o nome do animal: Kiki
Digite a espécie do animal: Cachorro
Digite a raça do animal: Settler Irlandês
Digite a idade do animal: 4
Digite o estado de saúde do animal: Saudável
Digite a data de chegada do animal: 30/03/2026
Digite o comportamento do animal: Dócil
----------------------------------------

é preciso ter cuidado apenas em 2 das opções: Idade e Data de Chegada.

Idade: quando for escrever a idade coloque APENAS o número que representa a idade do cachorro como está citado acima, Kiki possui 4 anos de idade mas para o sistema só precisa ser colocado o número 4 neste exemplo, caso contrário o sistema irá quebrar

Data: a data de chegada só pode ser colocada deste modo - DD/MM/AAAA. Se for colocado de qualquer outro modo não irá funcionar e irá cancelar cadastramento mostrando esse erro:

----------------------------------------
Erro: Data inválida ou formato incorreto!
----------------------------------------

ou seja apenas a data neste formato: 30/03/2026 irá funcionar.

as outras opções de escrita não possuem nenhuma forma de quebra ou falha

----------------------------------------
Animal cadastrado com sucesso!
----------------------------------------

após essa mensagem o menu de gerenciamento de animais retorna e ao digitar 2 e apertar enter:

----------------------------------------
Adoção+ - GERENCIAMENTO DE ANIMAIS
----------------------------------------
1 - Adicionar animal
2 - Visualizar animais no sistema <----
3 - Editar informações de um animal
4 - Deletar um animal do sistema
5 - Voltar ao menu principal

----------------------------------------
Animais Cadastrados:
----------------------------------------
1: Kiki - Cachorro - Settler Irlandês - 4 anos - Saudável - 30/03/2022 - Dócil
----------------------------------------

independente da quantidade de animais cadastrados todos irão aparecer com base na ordem que eles foram colcados no sistema, e sim mesmo que um animal seja retirado do sistema os números não mudam, mas vamos chegar lá

----------------------------------------
Animais Cadastrados:
----------------------------------------
1: Luke - Cachorro - Fox Paulistinha - 8 anos - Saudável - 07/04/2018 - Alegre
2: Kiki - Cachorro - Settler Irlandês - 4 anos - Saudável - 30/03/2022 - Dócil
3: Tobby - Cachorro - Lhasa Apso - 12 anos - Saudável - 10/10/2014 - Medroso
4: Sissi - Cachorro - Maltês - 9 anos - Saudável - 07/08/2017 - Tímido
5: Kiki - Cachorro - Settler Irlandês - 4 anos - Saudável - 30/03/2026 - Dócil
----------------------------------------

outro exemplo de aparece no sistema, após isso novamente aparece o menu de gerenciamento de sistema e ao digitar 3 e apertar Enter

----------------------------------------
Adoção+ - GERENCIAMENTO DE ANIMAIS
----------------------------------------
1 - Adicionar animal
2 - Visualizar animais no sistema 
3 - Editar informações de um animal <----
4 - Deletar um animal do sistema
5 - Voltar ao menu principal

----------------------------------------
Animais Cadastrados:
----------------------------------------
1: Luke - Cachorro - Fox Paulistinha - 8 anos - Saudável - 07/04/2018 - Alegre
2: Kiki - Cachorro - Settler Irlandês - 4 anos - Saudável - 30/03/2022 - Dócil
3: Tobby - Cachorro - Lhasa Apso - 12 anos - Saudável - 10/10/2014 - Medroso
4: Sissi - Cachorro - Maltês - 9 anos - Saudável - 07/08/2017 - Tímido
5: Kiki - Cachorro - Settler Irlandês - 4 anos - Saudável - 30/03/2026 - Dócil
----------------------------------------
Digite o Id do animal que deseja atualizar:

aparece a lista dos animais cadastrados e todas as informações podem ser alteradas, para escolher o animal é o mesmo estilo dos menus, digita o ID que no caso é o número na frente da lista e aperta Enter

----------------------------------------
Digite o Id do animal que deseja atualizar: 1
----------------------------------------
1 - Editar estado de saúde
2 - Editar idade do animal
3 - Editar comportamento do animal 
4 - Editar data de chegada do animal
5 - Editar raça do animal
6 - Editar espécie do animal
7 - Editar nome do animal
8 - Parar de atualizar
----------------------------------------
Digite o número de uma opção: 

para escolher o que alterar é o mesmo estilo dos menus, digita a opção que no caso é o número na frente da lista e aperta Enter

as mesmas regras da opção de adicionar seguem nessa área:

Idade: quando for escrever a idade coloque APENAS números que representam a idade do cachorro como está citado acima, Kiki possui 4 anos de idade mas para o sistema só precisa ser colocado o número 4 neste exemplo, caso contrário o sistema irá quebrar

Data de Chegada: a data de chegada só pode ser colocada deste modo: DD/MM/AAAA. Se for colocado de qualquer outro modo não irá funcionar e irá cancelar cadastramento mostrando esse erro:

as outras opções de escrita não possuem nenhuma forma de quebra ou falha

a tela ficará sempre nesta lista até você digitar 8 e apertar Enter que retorna ao menu de gerenciamento de animais 

e ao digitar 4 e Enter

----------------------------------------
Adoção+ - GERENCIAMENTO DE ANIMAIS
----------------------------------------
1 - Adicionar animal
2 - Visualizar animais no sistema 
3 - Editar informações de um animal 
4 - Deletar um animal do sistema <----
5 - Voltar ao menu principal

----------------------------------------
Animais Cadastrados:
----------------------------------------
1: Luke - Cachorro - Fox Paulistinha - 8 anos - Saudável - 06/04/2026 - Alegre
2: Kiki - Cachorro - Settler Irlandês - 4 anos - Saudável - 30/03/2022 - Dócil
3: Tobby - Cachorro - Lhasa Apso - 12 anos - Saudável - 10/10/2014 - Medroso
4: Sissi - Cachorro - Maltês - 9 anos - Saudável - 07/08/2017 - Tímido
5: Kiki - Cachorro - Settler Irlandês - 4 anos - Saudável - 30/03/2026 - Dócil <----
----------------------------------------
Digite o Id do animal que você irá deletar: 

aqui é simples quando você digitar o número na frente da lista ele apaga o animal correspondente é deletado, se eu digitar 5 nesse exemplo ele apaga a cópia de kiki que está aqui

----------------------------------------
Animal removido do sistema.
----------------------------------------

e automaticamente ele retorna ao menu principal e se digitar 2 e Enter

----------------------------------------
Animais Cadastrados:
----------------------------------------
1: Luke - Cachorro - Fox Paulistinha - 8 anos - Saudável - 06/04/2026 - Alegre
2: Kiki - Cachorro - Settler Irlandês - 4 anos - Saudável - 30/03/2022 - Dócil
3: Tobby - Cachorro - Lhasa Apso - 12 anos - Saudável - 10/10/2014 - Medroso
4: Sissi - Cachorro - Maltês - 9 anos - Saudável - 07/08/2017 - Tímido
----------------------------------------

aparece que foi deletado a cópia de kiki

caso você delete o primeiro animal os outros vão manter seus números de índice dessa forma:

----------------------------------------
Animais Cadastrados:
----------------------------------------
2: Kiki - Cachorro - Settler Irlandês - 4 anos - Saudável - 30/03/2022 - Dócil
3: Tobby - Cachorro - Lhasa Apso - 12 anos - Saudável - 10/10/2014 - Medroso
4: Sissi - Cachorro - Maltês - 9 anos - Saudável - 07/08/2017 - Tímido
----------------------------------------

e é aqui que termina a parte de gerenciar animais

O Gerenciamento de Adotantes é exatamente o mesmo sistema do de animais com algumas poucas mudanças digite 2 e Enter

----------------------------------------
Adoção+ - MENU PRINCIPAL
----------------------------------------
1 - Gerenciar animais 
2 - Gerenciar adotantes <----
3 - Gerenciar cuidados e atividades
4 - Sugestões personalizadas
5 - Sair do sistema

----------------------------------------
Adoção+ - GERENCIAMENTO DE ADOTANTES
----------------------------------------
1 - Fazer seu cadastro <----
2 - Visualizar adotantes cadastrados no sistema
3 - Editar informações de um adotante
4 - Deletar um adotante do sistema
5 - Voltar ao menu principal

a principal diferença dessa parte para a anterior é fazendo o cadastro digitando 1 e Enter

----------------------------------------
Digite seu nome: Tiago
Digite o seu CPF: 0909990
Digite sua idade: 19
Digite o seu endereço: Rua Sucrilhenta 90
digite o seu telefone: 7321708231780
digite o seu email: trico@gmail.com
----------------------------------------

aqui são mantidas a regra de Idade mas outras são adicionadas

Idade: quando for escrever a idade coloque APENAS números que representam a idade do cachorro como está citado acima, Kiki possui 4 anos de idade mas para o sistema só precisa ser colocado o número 4 neste exemplo, caso contrário o sistema irá quebrar

CPF e Telefone são obrigatórios o uso apenas de números, não precisa de pontinho no CPF nem linhas no telefone

as outras opções de escrita não possuem nenhuma forma de quebra ou falha

essas regras são mantidas quando for editar as informações 

----------------------------------------
Adoção+ - GERENCIAMENTO DE ADOTANTES
----------------------------------------
1 - Fazer seu cadastro
2 - Visualizar adotantes cadastrados no sistema
3 - Editar informações de um adotante <----
4 - Deletar um adotante do sistema
5 - Voltar ao menu principal

além disso não há diferenças significantes dessa área para a de animais, o que você pode fazer naquele pode nesse também

agora indo para a opção 3 de cuidados e atividades

----------------------------------------
Adoção+ - MENU PRINCIPAL
----------------------------------------
1 - Gerenciar animais 
2 - Gerenciar adotantes 
3 - Gerenciar cuidados e atividades <----
4 - Sugestões personalizadas
5 - Sair do sistema

o Gerenciamento de cuidados segue os exemplos de navegação das outras digitando 1 e Enter

----------------------------------------
Adoção+ - GERENCIAMENTO DE CUIDADOS
----------------------------------------
1 - Adicionar cuidado <----
2 - Visualizar cuidados
3 - Editar cuidado
4 - Deletar cuidado
5 - Voltar ao menu principal

leva você a esse menu

----------------------------------------
Animais Cadastrados:
----------------------------------------
1: Luke - Cachorro - Fox Paulistinha - 8 anos - Saudável - 07/04/2018 - Alegre
2: Kiki - Cachorro - Settler Irlandês - 4 anos - Saudável - 30/03/2022 - Dócil
3: Tobby - Cachorro - Lhasa Apso - 12 anos - Saudável - 10/10/2014 - Medroso
4: Sissi - Cachorro - Maltês - 9 anos - Saudável - 07/08/2017 - Tímido
----------------------------------------
Digite o ID do animal relacionado ao cuidado: 

primeiro você deve escolher o animal que irá fazer o cuidado/atividade demarcado, vamos usar Tobby neste exemplo

depois de digitar você poderá descrever o cuidado, a data e o responsável pelo animal que estará presente neste cuidado/atividade.

----------------------------------------
Digite o ID do animal relacionado ao cuidado: 3
----------------------------------------
Digite o cuidado/atividade previsto para o animal: Vacina de Raiva
Digite a data prevista do cuidado: 08/07/2026
Digite o responsável pelo cuidado: Bruno 
----------------------------------------
Cuidado cadastrado com sucesso!
----------------------------------------

a há duas regras aqui a de data no gerenciamento de animais e de data antiga:

Data: a data de chegada só pode ser colocada deste modo - DD/MM/AAAA. Se for colocado de qualquer outro modo não irá funcionar e irá cancelar cadastramento mostrando esse erro:

----------------------------------------
Erro: Data inválida ou formato incorreto!
----------------------------------------

ou seja apenas a data neste formato: 30/03/2026 irá funcionar.

mesma coisa serve quando for editar o cuidado

Data antiga: o sistema calcula quanto tempo falta para os cuidados/atividades não faz sentido cadastrar uma atividade em uma data que já ocorreu:

Digite a data: 08/05/2026
----------------------------------------
Erro: a data do cuidado não pode ser anterior a hoje. Tente novamente
----------------------------------------

mesma coisa serve quando for editar o cuidado

----------------------------------------
Adoção+ - GERENCIAMENTO DE CUIDADOS
----------------------------------------
1 - Adicionar cuidado
2 - Visualizar cuidados
3 - Editar cuidado <----
4 - Deletar cuidado
5 - Voltar ao menu principal

----------------------------------------
Cuidados cadastrados:
1: Kiki - Tosa - 25/06/2026 - 16 dias para o cuidado - Tiago
2: Tobby - Vacina de Raiva - 08/07/2026 - 29 dias para o cuidado - Bruno 
----------------------------------------
Digite o ID do cuidado que deseja atualizar:

aqui já é possível ver a funcionalidade dele, marcando o nome do animal que foi selecionado e também quanto tempo falta para o cuidado

----------------------------------------
Digite uma opção: 2
Digite a nova data: 08/05/2026
----------------------------------------
Erro: a data do cuidado não pode ser anterior a hoje. Tente novamente
----------------------------------------

falha na alteração

----------------------------------------
Digite uma opção: 2
Digite a nova data: 16/06/2026
----------------------------------------
Cuidados cadastrados:
1: Kiki - Tosa - 25/06/2026 - 16 dias para o cuidado - Tiago
2: Tobby - Vacina de Raiva - 16/06/2026 - 7 dias para o cuidado - Bruno 
----------------------------------------

sucesso na alteração, neste sistema é melhor de ver pois aparece logo depois o que foi alterado

deletar é a mesma coisa dos outros

----------------------------------------
Adoção+ - GERENCIAMENTO DE CUIDADOS
----------------------------------------
1 - Adicionar cuidado
2 - Visualizar cuidados
3 - Editar cuidado 
4 - Deletar cuidado <----
5 - Voltar ao menu principal

----------------------------------------
Cuidados cadastrados:
1: Kiki - Tosa - 25/06/2026 - 16 dias para o cuidado - Tiago
2: Tobby - Vacina de Raiva - 16/06/2026 - 7 dias para o cuidado - Bruno <----
Digite o ID do cuidado que deseja deletar: 2
----------------------------------------
Cuidado removido do sistema.
----------------------------------------

e é isso este é o Adoção+ criado por Tiago Leimig e Bruno Ramos

# OBRIGADO!







