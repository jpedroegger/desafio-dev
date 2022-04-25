# Desafio programação - para vaga desenvolvedor

A proposta do desafio consiste na criação de uma aplicação que permita ao usuário fazer upload de um arquivo, neste caso CNAB.txt. Esse arquivo deve ser parseado e suas informações inseridas em um banco de dados. Além disso, será necessário exibir essas informações formatadas em tela. O desafio pede ainda, que seja exibida a soma dos valores contidos no arquivo. Esses valores correspondem à transações bancárias e devem ser agrupados por lojas, com a finalidade de obter o saldo em conta.

# Tecnologias

As tecnologias utilizadas neste desafio incluem a linguagem `Python 3` e seu framework `Django`. Por apresentar estabilidade e qualidade no armazenamento de dados, foi utilizado `PostgreSQL`. Além disso, foi utilizada a ferramenta `Django-Rest-Framework`, o qual facilita a criação de endpoints da API.

# Instruções de uso

Para utilizar este programa é preciso clonar este repositório em sua máquina local com o comando `git clone https://github.com/jpedroegger/desafio-dev.git`. 
Após a clonagem, acesse a pasta do projeto com o comando `cd desafio-dev`. Para os próximos passos, é preciso ter instalado python nas versões 3.6 ou superiores. Para instalar os pacotes utilizados nesse programa utilize o comando `pip install -r requirements.txt`. 
Após as intalações, já será possível iniciar o projeto com o comando `python manage.py runserver`. Esse comando irá iniciar o servidor através do seu localhost exibido no terminal: `http://127.0.0.1:8000/`. 

Pronto, agora o arquivo CNAB.txt pode ser enviado pelo site. Note que também será possível adicionar registros através de outros arquivos, que não o CNAB.txt. No entanto, os dados presentes no arquivo precisam seguir o padrão do arquivo proposto pelo desafio.

# Instruções da API

Este programa conta ainda com a serialização do dados e disponibiliza, através da ferramente Django Rest Framework, uma API REST. 
Para consumir os dados, entre na página inicial do projeto em seu navegador. Por padrão, `http://127.0.0.1:8000/`. 
Basta digitar `http://127.0.0.1:8000/api` para obter a lista completa das informações salvas na base de dados, agora em formato JSON.
Se quiser buscar por um registro específico, digite o ID logo após api. Como por exemplo, `http://127.0.0.1:8000/api/25`.
Neste exemplo, o programa irá buscar pelo registro de ID 25 e trazê-lo em formato JSON.

<br><br>
# Desafio

Por favor leiam este documento do começo ao fim, com muita atenção.
O intuito deste teste é avaliar seus conhecimentos técnicos em programação.
O teste consiste em parsear [este arquivo de texto(CNAB)](https://github.com/ByCodersTec/desafio-ruby-on-rails/blob/master/CNAB.txt) e salvar suas informações(transações financeiras) em uma base de dados a critério do candidato.
Este desafio deve ser feito por você em sua casa. Gaste o tempo que você quiser, porém normalmente você não deve precisar de mais do que algumas horas.

# Instruções de entrega do desafio

1. Primeiro, faça um fork deste projeto para sua conta no Github (crie uma se você não possuir).
2. Em seguida, implemente o projeto tal qual descrito abaixo, em seu clone local.
3. Por fim, envie via email o projeto ou o fork/link do projeto para seu contato Bycoders_ com cópia para rh@bycoders.com.br.

# Descrição do projeto

Você recebeu um arquivo CNAB com os dados das movimentações finanaceira de várias lojas.
Precisamos criar uma maneira para que estes dados sejam importados para um banco de dados.

Sua tarefa é criar uma interface web que aceite upload do [arquivo CNAB](https://github.com/ByCodersTec/desafio-ruby-on-rails/blob/master/CNAB.txt), normalize os dados e armazene-os em um banco de dados relacional e exiba essas informações em tela.

**Sua aplicação web DEVE:**

1. Ter uma tela (via um formulário) para fazer o upload do arquivo(pontos extras se não usar um popular CSS Framework )
2. Interpretar ("parsear") o arquivo recebido, normalizar os dados, e salvar corretamente a informação em um banco de dados relacional, **se atente as documentações** que estão logo abaixo.
3. Exibir uma lista das operações importadas por lojas, e nesta lista deve conter um totalizador do saldo em conta
4. Ser escrita na sua linguagem de programação de preferência
5. Ser simples de configurar e rodar, funcionando em ambiente compatível com Unix (Linux ou Mac OS X). Ela deve utilizar apenas linguagens e bibliotecas livres ou gratuitas.
6. Git com commits atomicos e bem descritos
7. PostgreSQL, MySQL ou SQL Server
8. Ter testes automatizados
9. Docker compose (Pontos extras se utilizar)
10. Readme file descrevendo bem o projeto e seu setup
11. Incluir informação descrevendo como consumir o endpoint da API

**Sua aplicação web não precisa:**

1. Lidar com autenticação ou autorização (pontos extras se ela fizer, mais pontos extras se a autenticação for feita via OAuth).
2. Ser escrita usando algum framework específico (mas não há nada errado em usá-los também, use o que achar melhor).
3. Documentação da api.(Será um diferencial e pontos extras se fizer)

# Documentação do CNAB

| Descrição do campo  | Inicio | Fim | Tamanho | Comentário
| ------------- | ------------- | -----| ---- | ------
| Tipo  | 1  | 1 | 1 | Tipo da transação
| Data  | 2  | 9 | 8 | Data da ocorrência
| Valor | 10 | 19 | 10 | Valor da movimentação. *Obs.* O valor encontrado no arquivo precisa ser divido por cem(valor / 100.00) para normalizá-lo.
| CPF | 20 | 30 | 11 | CPF do beneficiário
| Cartão | 31 | 42 | 12 | Cartão utilizado na transação 
| Hora  | 43 | 48 | 6 | Hora da ocorrência atendendo ao fuso de UTC-3
| Dono da loja | 49 | 62 | 14 | Nome do representante da loja
| Nome loja | 63 | 81 | 19 | Nome da loja

# Documentação sobre os tipos das transações

| Tipo | Descrição | Natureza | Sinal |
| ---- | -------- | --------- | ----- |
| 1 | Débito | Entrada | + |
| 2 | Boleto | Saída | - |
| 3 | Financiamento | Saída | - |
| 4 | Crédito | Entrada | + |
| 5 | Recebimento Empréstimo | Entrada | + |
| 6 | Vendas | Entrada | + |
| 7 | Recebimento TED | Entrada | + |
| 8 | Recebimento DOC | Entrada | + |
| 9 | Aluguel | Saída | - |

# Avaliação

Seu projeto será avaliado de acordo com os seguintes critérios.

1. Sua aplicação preenche os requerimentos básicos?
2. Você documentou a maneira de configurar o ambiente e rodar sua aplicação?
3. Você seguiu as instruções de envio do desafio?
4. Qualidade e cobertura dos testes unitários.

Adicionalmente, tentaremos verificar a sua familiarização com as bibliotecas padrões (standard libs), bem como sua experiência com programação orientada a objetos a partir da estrutura de seu projeto.

# Referência

Este desafio foi baseado neste outro desafio: https://github.com/lschallenges/data-engineering

---

Boa sorte!
