# Daily Schedule 

## Descrição da API - CDU Cronogramas 

### Histórico da Revisão

| Data | Versão | Descrição | Autor |
| :-----: | :-----: | :-----: | :-----: |
| 16/01/2023 | 1.2 | Versão Continuada | Christian |

### 1. Resumo
Esse documento visa descrever como funcionará a API do caso de uso principal do sistema.
<br>

### 2. Funcionamento
  - No endpoint dentro do diretório do projeto teremos um recurso chamado cronogramas.
  - O recurso cronogramas terá obrigatorioamente que receber um ou mais parâmetros.
  - Este recurso (cronogramas) terá 4 métodos, que são os mais comuns (POST, GET, PUT ou PATCH, e DELETE).
  - Os cronogramas criados pelos usuários são semanais, tendo como base o dia/semana atual. 
  - O conteúdo dos cronogramas são tarefas. As tarefas são classificadas em mais de um tipo, e estão descritas no CDU Tarefas.

### 3. Exemplificação dos Parâmetros e do Endpoint
- O recurso cronogramas terá 5 parâmetros, sendo 1 passado como obrigatório, 3 obrigatórios que podem ser omitidos, e 1 opcional.
- Quando os parâmetros obrigatórios forem omitidos, o sistema irá passar sa referências atuais. Ex: Semana atual, Mês Atual, Ano Atual e Último ID Cadastrado.

#### 3.1 - Parâmetros
- O primeiro parâmetro é passado como obrigatório, e indicará a qual usuário aquele cronograma pertence.
- O segundo parâmetro é passado como obrigatório e pode ser omitido, ele informa a qual semana o cronograma pertence.
- O terceiro parâmetro é passado como obrigatório e pode ser omitido, ele indica o mês ao qual as semanas pertencem.
- O quarto parâmetro é passado como obrigatório e pode ser omitido, ele referencia o ano ao qual os meses e semanas fazem parte.
- O quinto parâmetro é passado como opcional, ele irá indicar um dos vários cronogramas cadastrados na semana.

#### 3.2 - Endpoint
- *PADRÃO UTILIZADO*
  - recurso/parametro-1/parametro-2/paramatro-3/parametro-4/parametro-5
  - cronogramas/usuário/semana/mes/ano/id

### 4. Exemplos dos Métodos e do Endpoint
  - ***POST***
    - cronogramas/ (Não funcionará, pois o primeiro parâmetro que informa o usuário é obrigatório e deve ser passado)
    - cronogramas/1 (Criará o cronograma para o usuario 1 omitindo os outros parâmetros obrigatórios, o sistema pegará a semana, mês e ano atuais, assim como irá incrementar o ID do cronograma)
    - cronogramas/1/semana3 (Criará o cronograma para o usuario 1 omitindo os outros parâmetros obrigatórios, o sistema pegará o mês e ano atuais, assim como irá incrementar o ID do cronograma)
    - cronogramas/1/semana3/mes2 (Criará o cronograma para o usuario 1 omitindo os outros parâmetros obrigatórios, o sistema pegará o ano atual, assim como irá incrementar o ID do cronograma)
    - **OBS: Caso esteja em uma semana/mes/ano e tente criar um cronograma para a semana/mes/ano anterior, não permitir.**

  - ***GET***
     - cronogramas/ (inválido por não informar a quem pertence o cronograma)
     - cronogramas/1 (Retorna todos os cronogramas da semana atual do usuario 1)
     - cronogramas/1/2 (inválido pois o segundo parametro é uma semana definida de 1 a 4)
     - cronogramas/1/semana3 (Retorna todos os cronogramas do usuario 1 da semana 3)
     - cronogramas/0 (Retorna um erro pois não informa o usuario nem o cronograma)
     
  - ***PUT ou PATCH***
     - cronogramas/1 (Atualizará o cronograma atual do usuario 1)
     - cronogramas/1/3 (Atualizará o cronograma do usuario 1 da semana 3)
     - cronogramas/0 (Retorna um erro pois não informa o usuario nem o cronograma)
     - cronogramas/0/3 (Retorna um erro pois pede o cronograma da semana 3 mas não informa qual o usuario)
        
  - ***DELETE***
     - cronogramas/1 (Apagará o cronograma atual do usuario 1)
     - cronogramas/1/3 (Apagará o cronograma do usuario 1 da semana 3)
     - cronogramas/0 (Retorna um erro pois não informa o usuario nem o cronograma)
     - cronogramas/0/3 (Retorna um erro pois pede o cronograma da semana 3 mas não informa qual o usuario)

### 5. Descrevendo os Métodos
  - **Método POST:** Criará um cronograma para um usuário, no qual o identificador do usuário e a semana são passados como parâmetros, o identificador do cronograma dentro de uma determinada semana será gerido pelo sistema.
      - Caso seja informado apenas o primeiro parâmetro (id do usuário), o método deverá criar um cronograma para a semana atual.
      - Caso haja passagem de um segundo parâmetro, ele criará um cronograma informando a qual semana deseja que o cronograma pertença.
      
  - **Método GET:** Recuperará o cronograma completo da semana atual de um usuário no qual seu identificador é passado como parâmetro.
      - Caso haja passagem de mais de um parâmetro, ele retornará um dos vários cronogramas daquele usuário.
      - Caso não haja passagem de nenhum parâmetro, o método deverá retornar um erro.
         
  - **Método PUT ou PATCH:** Atualizará um cronograma existente de um usuário.
      - Caso receba apenas o primeiro parâmetro que é o identificador do usuário, atualizará o cronograma da semana atual.
      - Caso receba mais de um parâmetro, deverá atualizar o cronograma da semana informada.
      - Caso não receba nenhum parâmetro, o método deverá retornar um erro.
         
  - **Método DELETE:** Apagará um cronograma existente de um usuário.
      - Caso receba apenas o primeiro parâmetro que é o identificador do usuário, deletará o cronograma da semana atual.
      - Caso receba mais de um parâmetro, deverá deletar o cronograma da semana informada.
      - Caso não receba nenhum parâmetro, o método deverá retornar um erro.
<br>

**OBS: Alguns desses métodos devem verificar se o cronograma está público ou privado para não executar algumas das operações CRUD.**
<br><br>

<!--
Observações:
Criar issues para fazer alterações que melhorem esse documento.
O parâmetro "identificador" citado no tópico 3 servirá para identificar o usuário do cronograma, em alguns métodos os parâmetros podem ser opcionais.

Sugestões:
Tópico 2 / Item 5 - Alterar o trecho "e serão descritas em um outro CDU" para o link referenciando o CDU "Tarefas" que ainda não foi criado.
Tópico 3 / Item 1 / Sub-item 1 - Especificar o erro gerado que ainda não foi discutido/pensado.
Tópico 3 / Item 1 / Sub-item 3 - Especificar o erro gerado que ainda não foi discutido/pensado.
Tópico 3 / Item 2 / Sub-item 2 - Especificar o erro gerado que ainda não foi discutido/pensado.
Tópico 3 / Item 3 / Sub-item 3 - Especificar o erro gerado que ainda não foi discutido/pensado.
Tópico 3 / Item 4 / Sub-item 3 - Especificar o erro gerado que ainda não foi discutido/pensado.
-->