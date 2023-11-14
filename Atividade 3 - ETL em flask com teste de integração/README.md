# OpenWeather ETL em Flask
Este projeto consiste em uma aplicação Flask que realiza uma ETL (Extração, Transformação e Carga) de dados climáticos da API OpenWeather para uma tabela no banco de dados SQLite. Além disso, inclui testes de integração para garantir o correto funcionamento das funcionalidades.

## Sumário
- [Descrição Geral](#descrição-geral)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Configuração do Flask](#configuração-do-flask)
- [ETL (Extração, Transformação e Carga)](#etl-extração-transformação-e-carga)
- [Testes](#testes)
- [Créditos](#créditos)


## Descrição Geral
A aplicação busca informações climáticas de mais de 10 cidades do Brasil, consulta a API OpenWeather para obter esses dados, e armazena as informações em uma tabela no banco de dados SQLite. A tabela possui as seguintes colunas: Data da Ingestão, Tipo, Valores e Uso.

## Estrutura do Projeto
**app.py**: Arquivo principal da aplicação Flask, contendo as rotas, as funções ETL e a configuração do servidor.
**requirements.txt**: Lista de dependências do projeto.
**test_app.py**: Arquivo contendo testes de integração para as funções principais.
**README.md**: Documentação detalhada do projeto.

## Configuração do Flask
Certifique-se de ter o Python instalado. Em seguida, instale as dependências necessárias usando o comando:

```
pip install -r requirements.txt
```
Para executar a aplicação, utilize o seguinte comando:
```
python app.py
```

A aplicação estará disponível em http://127.0.0.1:5000/.

## ETL (Extração, Transformação e Carga)

Função **coletar_dados()**
Esta função realiza a extração de dados climáticos da API OpenWeather para mais de 10 cidades brasileiras. Em caso de erro na requisição, um log é exibido indicando a cidade com problema.

Função **limpar_tabela()**
Esta função realiza a limpeza da tabela no banco de dados SQLite (dados_tempo), removendo todos os registros.

Função **criar_tabela()**
Esta função realiza a transformação dos dados obtidos pela função coletar_dados e os armazena na tabela dados_tempo. A tabela é composta por quatro colunas: Data de Ingestão, Tipo, Valores e Uso.

## Testes
Os testes de integração são implementados utilizando a biblioteca pytest. Eles abrangem cenários de sucesso e cenários de erro para as funções coletar_dados, limpar_tabela e criar_tabela. Certifique-se de instalar as dependências de teste antes de executar os testes:
```
pip install -r requirements.txt
```
Execute os testes com o comando:

```
pytest test_app.py
```

## Créditos
O desenvolvimento desse projeto ocorreu em parceria com o aluno Pedro Rezende que, por sua vez, o fez com base no auxílio dos alunos Dayllan Alho e Patrick Miranda. 

