# desafio_olx-pset1
Desafio D-OLX em Python

Objetivo:

Desenvolver um sistema de compra e venda de objetos novos e usados, chamado D-OLX, semelhante ao OLX. O sistema deve permitir que os usuários cadastrem produtos, pesquisem por produtos e filtrem por interesses, como região e tipo do produto (móvel, aluguel, carro, moto, eletrônico, etc). Ao escolher o produto, o usuário poderá ver todos os dados do anúncio, incluindo os comentários, caso ele esteja disponível.

Requisitos:

Modelagem de Dados:

    Crie modelos para representar usuários e produtos.
    Utilize conceitos de herança, encapsulamento e polimorfismo nos modelos.

Persistência:

    Implemente uma classe de persistência do tipo estoque para armazenar os produtos.
    Os produtos vendidos devem ser removidos da coleção de produtos disponíveis e direcionados para uma coleção de produtos vendidos.

Padrões de Design:

Utilize pelo menos um padrão de projeto em sua implementação. Dicas: factory, observer, singleton, builder...

Opções de Desenvolvimento:

Escolha uma das seguintes opções para aprimorar seu sistema:

1) Ao publicar um anúncio, notifique TODOS os usuários que permitiram o aviso por notificações sobre a publicação desse anúncio. Use o padrão Observer.

2) Crie um diagrama de classes para o projeto usando ferramentas como draw.io.

3) Crie um diagrama de casos de uso para o projeto usando ferramentas como draw.io.

Usuário:

Represente o usuário com nome, idade, identificador (CPF) e papel (vendedor, comprador, ambos). Diferencie o perfil de vendedor do perfil de comprador de maneira criativa. O comprador poderá realizar comentários em produtos.

Anúncio:

Um anúncio deve conter informações como nome, descrição, data de lançamento, nome e identificador do vendedor, tipo do produto, local de publicação (região), estado de uso (novo ou usado), identificador, quantidade disponível, comentários, etc.

Entrega:

Você deve entregar o projeto até o dia 06/02, contendo modelos, um pseudo-controller, e a persistência implementada. O código deve ser escrito em Python ou Java.

Opcional:

Faça um clone do projeto e faça um pull request no GitHub para contribuir com a evolução do código.

Instruções Adicionais:

Crie um arquivo README.md explicando o que seu código faz, suas escolhas para a solução, quais design patterns utilizou e o porquê, e o fluxo de execução.

Realização e avaliação:

A atividade deverá ser realizada em grupos de 4 pessoas, a serem escolhidos de maneira aleatória (vulgo minha decisão na hora de dividir). É importante ressaltar que a atividade é em grupo, por isso todos devem ajudar a contribuir com o projeto, inclusive uns com os outros. 

No dia da avaliação, irei verificar os projetos e perguntar sobre as decisões para alguém do grupo. Deixaremos o projeto aberto para corrigirmos em sala, com toda a turma, se não for um problema para todos.
