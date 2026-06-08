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
1 - Adicionar animal
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

Data de Chegada: a data de chegada só pode ser colocada deste modo: DD/MM/AAAA. Se for colocado de qualquer outro modo não irá funcionar e irá cancelar cadastramento mostrando esse erro:

----------------------------------------
Erro: Data inválida ou formato incorreto!
----------------------------------------

ou seja apenas a data neste formato: 30/03/2026 irá funcionar.

----------------------------------------
Animal cadastrado com sucesso!
----------------------------------------

após essa mensagem o menu de gerenciamento de animais retorna e ao digitar 2 e apertar enter:

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

outro exemplo de aparece no sistema, após isso novamente aparece o menu de gerenciamento de sistema e ao digitar 3 e apertar enter

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

aparece a lista dos animais cadastrados 





