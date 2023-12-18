
## Sumário

[1. Introdução](#c1)

[2. Pré-requisitos](#c2)

[3. Instalação e Configuração do Apache Airflow](#c3)

[4. Conectar com o Amazon S3](#c4)

[5. Configuração do Pipeline e Processamento de Dados com PySpark](#c5)

[6. Agendamento e Execução de Tarefas no Apache Airflow (execução do vídeo)](#c6)

<br>

# <a name="c1"></a>1. Introdução

Este tutorial em vídeo demonstra o processo de instalação e configuração do Apache Airflow em um ambiente de desenvolvimento, com ênfase no uso do PySpark para processamento de dados em Big Data. O objetivo é mostrar, passo a passo, como configurar um pipeline desde a ingestão de dados até a montagem de um cubo de dados.

# <a name="c2"></a>2. Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- Docker e Docker Compose
- Python
- [Dotenv](https://pypi.org/project/python-dotenv/)
- Boto3
- Pandas

# <a name="c3"></a>3. Instalação e configuração do Apache Airflow

Para instalar e configurar o Apache Airflow, siga os passos abaixo:

### Passo 1: Clonar o repositório

Clone este repositório em seu ambiente de desenvolvimento.

bash
git clone https://seu-repositorio.git
cd seu-repositorio


### Passo 2: Configuração do Docker Compose

Edite o arquivo docker-compose.yaml conforme necessário, ajustando as variáveis de ambiente e os volumes.
yaml
docker-compose.yaml


### Passo 3: Inicialização do Apache Airflow

Execute o seguinte comando para iniciar o Apache Airflow:

bash
docker-compose up


Acesse o Airflow em http://localhost:8080 para verificar se está funcionando corretamente.

# <a name="c4"></a>4. Conexão com o Amazon S3

Para conectar-se ao Amazon S3, siga os passos abaixo:

### Passo 1: Configuração das credenciais da AWS

Certifique-se de ter as credenciais da AWS configuradas corretamente no arquivo .env:

bash
AWS_REGION_NAME=sua-regiao
AWS_ACCESS_KEY_ID=sua-chave-de-acesso
AWS_SECRET_ACCESS_KEY=sua-chave-secreta
AWS_SESSION_TOKEN=seu-token-de-sessao


### Passo 2: Execução da DAG de Conexão com o S3

Execute a DAG de conexão com o S3 para listar os buckets:

bash
docker-compose exec airflow-cli bash -c "airflow dags trigger conexao_com_aws"


# <a name="c5"></a>5. Configuração do pipeline e processamento de dados com PySpark

A configuração do pipeline e o processamento de dados com PySpark estão integrados na DAG `conexao_com_aws`. O processo inclui:

- Listagem de arquivos em um bucket S3
- Pré-processamento dos dados, removendo caracteres especiais e lidando com valores nulos
- Upload do arquivo pré-processado de volta ao S3

# <a name="c6"></a>6. Agendamento e Execução de Tarefas no Apache Airflow

O agendamento e a execução de tarefas no Apache Airflow são gerenciados pela DAG. A DAG está configurada para ser executada diariamente. Para agendar outras tarefas, consulte a documentação oficial do Airflow.

### Execução do Tutorial - Vídeo
Para uma demonstração visual de todo o processo, assista ao <a href="https://clipchamp.com/watch/Cbn523dv9P4">'VÍDEO TUTORIAL'</a> que acompanha este README.
