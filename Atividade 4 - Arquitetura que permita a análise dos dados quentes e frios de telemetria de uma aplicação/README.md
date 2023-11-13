# Arquitetura de Análise de Dados de Telemetria

A análise de dados de telemetria em tempo real desempenha um papel crucial na monitorização do desempenho de sistemas e aplicações, identificando problemas e oportunidades de otimização imediatamente. Isso é particularmente crítico em cenários onde a latência e a ação imediata são essenciais, como em sistemas de IoT, sistemas de segurança e monitorização de servidores.

## Ferramentas na AWS para Dados Quentes

Para lidar com dados quentes (alta taxa de geração), a AWS oferece diversas ferramentas. Serviços como o Amazon Kinesis são ideais para ingestão, processamento e análise em tempo real de dados. Para armazenamento temporário, o Amazon DynamoDB, Elasticsearch ou Amazon CloudWatch podem ser usados.

## Diferença de Coleta entre Dados Quentes e Dados Frios

Dados quentes são gerados em alta frequência, exigindo sistemas de coleta e processamento de baixa latência, enquanto dados frios são armazenados para análises a longo prazo, com menor prioridade de tempo. Dados quentes geralmente são enviados diretamente para análise em tempo real, enquanto dados frios são armazenados em bancos de dados de longa duração.

## Arquitetura com Diagrama

Abaixo está a representação da arquitetura que combina dados quentes e frios:

<img width="1936" alt="Arquitetura" src="https://github.com/1zabella/Modulo-8/assets/99206817/b4f0bf7b-263f-40c1-9113-c8f7cb59cdb1">

Fonte: Autoria do grupo 2 - [Link para visualização](https://www.figma.com/file/cXHYv2fVL2kA38uof8qabj/Arquitetura?type=whiteboard&node-id=0%3A1&t=QAaJpBvgY1KjeiPK-1)

Os dados quentes são aqueles que são acessados com frequência, geralmente em tempo real ou próximo do tempo real. É crucial garantir que os dados possam ser acessados rapidamente, o que é essencial para aplicações que exigem processamento de dados em tempo real.

### Processo dos Dados Quentes na Arquitetura

**Evento no Datalake:**
O processo começa com um evento que ocorre no Datalake. Um Datalake é geralmente um repositório de dados que armazena grandes volumes de dados brutos em seu formato nativo até que seja necessário processá-los.

**AWS Lambda:**
Quando um evento ocorre no Datalake, o AWS Lambda é acionado. O AWS Lambda é um serviço de computação serverless que permite a execução de código em resposta a eventos sem a necessidade de provisionar ou gerenciar servidores.

**Kinesis Firehose:**
O AWS Lambda está conectado a um Kinesis Firehose. O Kinesis Firehose é um serviço da AWS que facilita a ingestão, transformação e carregamento (ETL) contínuo de grandes volumes de dados em serviços de armazenamento e análise.

**MongoDB:**
O Kinesis Firehose está conectado a um banco de dados MongoDB. MongoDB é um banco de dados NoSQL orientado a documentos, o que significa que armazena dados em documentos JSON BSON.

**PostgreSQL:**
O MongoDB se conecta com o banco de dados PostgreSQL. PostgreSQL é um sistema de gerenciamento de banco de dados relacional (RDBMS) que utiliza o modelo de dados relacional.

**Amazon Elasticsearch:**
O PostgreSQL está conectado a um serviço Amazon Elasticsearch. O Amazon Elasticsearch é um serviço gerenciado que facilita a busca, análise e visualização de dados em grande escala. Ele é baseado no Elasticsearch, que é uma engine de busca e análise distribuída.

**Grafana:**
O Amazon Elasticsearch está conectado a um serviço de visualização chamado Grafana. Grafana é uma plataforma de código aberto para análise e monitoramento interativo. Ele se conecta a uma variedade de fontes de dados, incluindo bancos de dados e sistemas de monitoramento, para visualizar dados e métricas.

### Resumindo a Interconexão

- Um evento no Datalake aciona o AWS Lambda.
- O AWS Lambda processa o evento e envia os dados para o Kinesis Firehose.
- O Kinesis Firehose faz a ingestão de dados no MongoDB e PostgreSQL.
- O PostgreSQL está conectado ao Amazon Elasticsearch para busca e análise.
- O Amazon Elasticsearch está conectado ao Grafana para a visualização interativa e análise dos dados.

## Serviços AWS e Azure Equivalentes

Apresenta-se o mapeamento dos serviços da AWS mencionados para equivalentes na Azure:

**AWS Lambda (Compute):**
`Azure Function:` Azure Functions é o equivalente ao AWS Lambda na Azure. Ele permite a execução de código sem a necessidade de provisionar servidores explicitamente.

**Kinesis Firehose (Data Streaming):**
`Azure Stream Analytics:` Para processamento de streaming de dados, Azure Stream Analytics pode ser uma escolha equivalente. Ele permite a análise em tempo real de dados de streaming usando consultas SQL.

**Amazon Elasticsearch (Search and Analytics):**
`Azure Elasticsearch Service:` Para funcionalidades semelhantes ao Amazon Elasticsearch, você pode usar o Azure Elasticsearch Service. Ele fornece uma implementação gerenciada do Elasticsearch.

Ao planejar a migração para a Azure, é importante considerar as características específicas dos serviços e ajustar a configuração conforme necessário, pois pode haver diferenças nas funcionalidades e na forma como os serviços são configurados entre as nuvens.
