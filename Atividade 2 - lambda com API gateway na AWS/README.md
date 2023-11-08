# Criação de um lambda com API gateway na AWS em python.
A tarefa em questão envolve a criação de um serviço na Amazon Web Services (AWS) utilizando o ambiente AWS Labs, que combina duas ferramentas: o AWS Lambda e o API Gateway, utilizando a linguagem de programação Python como base. Essa atividade é conduzida com o objetivo de estabelecer uma infraestrutura escalável e altamente disponível para gerenciar requisições e fornecer respostas eficazes a partir de endpoints de API criados no AWS API Gateway.
## Pré-requisitos
Para configurar e executar o projeto de Lambda com API Gateway na AWS em Python, você deve atender aos seguintes pré-requisitos:

- **Conta da Amazon Web Services (AWS)**: É necessário ter uma conta ativa na AWS para criar e configurar os serviços necessários.

- **Ambiente de Desenvolvimento Python**: Certifique-se de ter um ambiente de desenvolvimento Python configurado em sua máquina.

- **Conhecimento em AWS Lambda**: É recomendado ter um entendimento básico sobre como o AWS Lambda funciona, como criar funções Lambda e como configurá-las.

- **Conhecimento em AWS API Gateway**: É útil ter conhecimento sobre o AWS API Gateway e como configurar endpoints de API.

- **Credenciais AWS**: Certifique-se de ter credenciais de acesso à AWS configuradas, seja por meio do AWS CLI ou por meio de variáveis de ambiente.

- **Código da Função Lambda**: Tenha o código da função Lambda pronta para implantação. Isso inclui o código Python que será executado pela função.

- **Configuração do AWS API Gateway**: Tenha uma compreensão clara dos endpoints de API que você deseja criar e configurar no AWS API Gateway.

Depois de atender a esses pré-requisitos, você estará pronto para configurar e implantar seu projeto de Lambda com API Gateway na AWS em Python. Certifique-se de que suas credenciais e configurações estejam corretas antes de prosseguir com a implantação do projeto.

## Explicações 
O AWS Lambda, uma parte fundamental desse projeto, é um serviço de computação serverless que executa código em resposta a eventos. Neste contexto, o Lambda é configurado para processar solicitações vindas do API Gateway e executar a lógica de autenticação, validando as credenciais do usuário com base em autenticação Basic Auth.

O API Gateway, por sua vez, funciona como um proxy para o Lambda, permitindo a exposição segura e gerenciamento de endpoints de API para o público ou sistemas externos. Ele atua como uma camada de abstração que cuida do roteamento de solicitações HTTP e, no nosso caso, encaminha solicitações para o Lambda para autenticação.

### Configuração do ambiente aws 
![image](https://github.com/1zabella/Modulo-8/assets/99206817/e8fff528-428b-4a9c-a6be-73dc87f27b28)

### Inserção do método post na API Gateway
A imagem a seguir representa a habilitação do método post no end-point da API Gateway:

![image](https://github.com/1zabella/Modulo-8/assets/99206817/6404b1cf-be8c-459a-a74f-b99748b482e6)


![image](https://github.com/1zabella/Modulo-8/assets/99206817/96d24057-ed9e-4a27-8974-eab396e1ac93)

### Função lambda
```
# Código utilizado na criação da função lambda
import base64
import json

class Authenticator:
    def __init__(self, users):
        self.users = users

    def authentication(self, event):
        headers = event.get('headers', {})
        authorization_header = headers.get('Authorization', '')

        if not authorization_header:
            return {
                'statusCode': 401,
                'body': 'Acesso não autorizado'
            }

        if authorization_header.startswith('Basic '):
            encoded_credentials = authorization_header[len('Basic '):]
            credentials = base64.b64decode(encoded_credentials).decode('utf-8')

            user, password = credentials.split(':')

            if user in self.users and self.users[user] == password:
                return {
                    'statusCode': 200,
                    'body': json.dumps(event['body'])
                }

        return {
            'statusCode': 401,
            'body': 'Acesso não autorizado'
        }

def lambda_handler(event, context):
    users = {
        "izabella": "faria",
    }
    
    authentication = Authenticator(users)
    return authentication.authentication(event)
```

O código Python acima implementa uma função Lambda na AWS que fornece autenticação usando o método Basic Auth. O código recebe solicitações HTTP, verifica a presença do cabeçalho de autorização e autentica os usuários com base nas credenciais fornecidas.

A classe Authenticator recebe um dicionário de usuários e senhas como entrada. Ela verifica o cabeçalho de autorização na solicitação e autentica os usuários com base nas credenciais fornecidas.

A função lambda_handler define um conjunto de usuários válidos e chama a classe Authenticator para autenticar a solicitação. Se as credenciais estiverem corretas, a solicitação é autorizada e o código de status 200 é retornado com o corpo da solicitação. Caso contrário, a solicitação recebe o código de status 401, indicando acesso não autorizado.

### Retorno do json após autenticação
A imagem a seguir representa a função post criada a partir do end-point gerado pela API Gateway, que permitiu, após o processo de autenticação, a visualização do json escolhido.
![image](https://github.com/1zabella/Modulo-8/assets/99206817/b6cdee6a-ddeb-42cb-a6fe-badb6f0dddb8)
**Json utilizado:**
```
{
  "autores": [
    {
      "nome": "Jane Austen",
      "nacionalidade": "Inglesa",
      "nascimento": "1775",
      "falecimento": "1817",
      "livros": [
        {
          "título": "Orgulho e Preconceito",
          "ano": 1813
        },
        {
          "título": "Razão e Sensibilidade",
          "ano": 1811
        },
        {
          "título": "Emma",
          "ano": 1815
        }
      ]
    },
    {
      "nome": "Fyodor Dostoevsky",
      "nacionalidade": "Russa",
      "nascimento": "1821",
      "falecimento": "1881",
      "livros": [
        {
          "título": "Crime e Castigo",
          "ano": 1866
        },
        {
          "título": "Os Irmãos Karamazov",
          "ano": 1880
        },
        {
          "título": "O Idiota",
          "ano": 1869
        }
      ]
    },
    {
      "nome": "Leo Tolstoy",
      "nacionalidade": "Russa",
      "nascimento": "1828",
      "falecimento": "1910",
      "livros": [
        {
          "título": "Guerra e Paz",
          "ano": 1869
        },
        {
          "título": "Anna Karenina",
          "ano": 1877
        }
      ]
    },
    {
      "nome": "Victor Hugo",
      "nacionalidade": "Francês",
      "nascimento": "1802",
      "falecimento": "1885",
      "livros": [
        {
          "título": "Os Miseráveis",
          "ano": 1862
        },
        {
          "título": "O Corcunda de Notre-Dame",
          "ano": 1831
        }
      ]
    }
  ]
}

```
Após essa etapa, foram realizados testes unitários para a verificação do funcionamento da autenticação.
### Teste de Autenticação com Credenciais Incorretas:
```
{
    "queryStringParameters": {
        "auth": "usuario_inexistente:senha_incorreta"
    },
    "body": "{\"key\": \"value\"}"
}

```
Neste teste, simulamos uma solicitação de autenticação com credenciais incorretas. Os principais elementos da solicitação são:

**queryStringParameters:** Este objeto contém os parâmetros de consulta, com o parâmetro "auth" representando um exemplo de tentativa de autenticação. A string "usuario_inexistente:senha_incorreta" indica que o usuário está tentando se autenticar com um usuário inexistente e senha incorreta.

**body:** O corpo da solicitação contém informações adicionais, representadas aqui por {"key": "value"}. O conteúdo real do corpo pode variar de acordo com a implementação do sistema.

Este teste ilustra a tentativa de autenticação com credenciais incorretas, e seu código de função Lambda deve ser capaz de identificar e rejeitar essa tentativa.

![Teste 1](https://github.com/1zabella/Modulo-8/assets/99206817/cc2222b5-4a12-4db2-a5fb-86b583a179d1)

### Teste de Solicitação Não Autenticada:
```
{
    "queryStringParameters": {},
    "body": "{\"key\": \"value\"}"
}

```
Neste teste, simulamos uma solicitação que não inclui parâmetros de autenticação na consulta, o que pode indicar uma solicitação de usuário não autenticado. Os principais elementos são:

**queryStringParameters:** Neste caso, o objeto está vazio, indicando que não há tentativa de autenticação na consulta.

**body:** Novamente, o corpo da solicitação contém informações adicionais, representadas por {"key": "value"}. O conteúdo do corpo pode variar de acordo com a necessidade.

Este teste representa uma solicitação de um usuário que não está tentando se autenticar.

![Teste 2](https://github.com/1zabella/Modulo-8/assets/99206817/e14f4eed-3a66-4c71-b401-fc1ba79630d8)

## Agradecimentos
 O projeto aqui estabelecido foi feito em conjunto com os seguintes estudantes do Instituto de Tecnologia e Liderança:
- [Dayllan Alho](https://www.linkedin.com/in/dayllan-alho/) 
- [Giovanna Furlan](https://www.linkedin.com/in/giovanna-furlan-torres/)
- [Lucas Brito](https://www.linkedin.com/in/lucas-britto-376665208/)
- [Pedro Rezende](https://www.linkedin.com/in/pedrocrezende/)

## Referências
- [Tutorial: Uso do Lambda com API Gateway](https://docs.aws.amazon.com/pt_br/lambda/latest/dg/services-apigateway-tutorial.html)
- [OpenAI ChatGPT](https://chat.openai.com/)
