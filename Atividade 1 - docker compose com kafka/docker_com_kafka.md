# Criação de um docker compose com kafka
A atividade aqui desenvolvida trata-se da elaboração de um arquivo docker-compose que inclui todos os parâmetros necessários para configurar um ambiente Kafka com seus respectivos gerenciadores, juntamente com um exemplo de como produzir e consumir mensagens localmente.
## Pré-requisitos
- **WSL (Windows Subsystem for Linux)**: Instale e configure o WSL em seu sistema Windows.

- **Docker para Windows**: Instale o Docker Desktop for Windows para executar contêineres Docker na WSL.

- **Configurar o Docker para WSL:** No Docker Desktop, vá para Configurações > Geral e marque a opção "Expose daemon on tcp://localhost:2375 without TLS" para permitir a comunicação entre a WSL e o Docker no Windows.

- **Instalar o Kafka na WSL:** Utilize sua distribuição Linux na WSL para instalar o Apache Kafka e configure-o de acordo com suas necessidades.

- **Configurar o Kafka:** Defina tópicos, configure produtores e consumidores, e ajuste as propriedades do Kafka conforme necessário.

- **Python:** Instale o Python em sua distribuição Linux na WSL.

- **Bibliotecas Kafka para Python:** Utilize pip ou conda para instalar bibliotecas Python como confluent-kafka para interagir com o Kafka a partir de seu projeto Python.

Depois de cumprir esses pré-requisitos, você estará pronto para executar seu projeto que envolve Kafka, Docker e Python na sua WSL. Certifique-se de iniciar o Kafka na WSL conforme necessário antes de executar seu projeto.

## Recomendações
É estritamente recomendado que seja iniciado, antes, o arquivo "listener.ipynb" antes do arquivo "producer.ipynb". Isso porque, durante os testes, somente foi possível visualizar os dados presentes na fila quando o "listener" já estava ativado e pronto para ouvir todos os dados enviados pelo tópico. 

Para conseguir rodar e visualizar o projeto, após ter verificado todos os pré-requisitos, é necessário, no terminal WSL, digitar o seguinte comando:
```
docker-compose up
```
Após essa etapa, é preciso rodar todas as células presentes no arquivo jupyter denominado "listener.ipynb" e deixar a última célula em funcionamento. Logo em seguida, é preciso rodar todas as células do arquivo "producer.py"

## Explicações 

**Código do Listener (Consumidor Kafka):**

Este código tem a função de receber informações sobre filmes da internet, filtrar os filmes desejados, formatar essas informações de maneira compreensível pelo computador e, em seguida, enviar esses dados ao Kafka. O Kafka é um sistema que ajuda a compartilhar informações entre aplicativos.

**Código do Producer (Produtor Kafka):**

O código do produtor se concentra em configurar a conexão com o Kafka e obter informações sobre filmes de um site chamado TMDb. Ele verifica se a obtenção de informações foi bem-sucedida, processa os dados dos filmes e, em seguida, envia essas informações ao Kafka.

Em resumo, esses códigos trabalham juntos para obter dados sobre filmes da internet, formatá-los e compartilhá-los entre aplicativos usando o Kafka. O Listener consome os dados e o Producer os fornece.


## Referências
- [Apache Kafka - Codificação na Prática](https://medium.com/trainingcenter/apache-kafka-codifica%C3%A7%C3%A3o-na-pratica-9c6a4142a08f)
- [OpenAI ChatGPT](https://chat.openai.com/)
- [GitHub - Big Data Cluster](https://github.com/mrugankray/Big-Data-Cluster/tree/main)
- [The Movie Database (TMDb)](https://www.themoviedb.org/)
