# AWS CDK for Professionals (Python)

Neste curso, aprendi como usar o AWS Cloud Development Kit (AWS CDK) que é uma estrutura de software de código aberto que permite a definicão de infraestutura de nuvem como código.

Com o AWS CDK, é possível modelar e provisionar infraestrutura na AWS, usando linguagens como Python, Java ou TypeScript. O AWS CDK integra-se com o AWS CloudFormation para implantar e provisionar a infraestrutura.

O AWS CDK é composto por um conjunto de ferramentas e bibliotecas de software, incluindo a AWS Construct Library. Com a AWS Construct Library, é possível resolver tarefas AWS, como implantar código em uma frota de hosts.

O AWS CDK não é um serviço da AWS, mas sim um cliente, uma abstração lateral sobre o CloudFormation.

## Ambiente, Ferramentas e Configuração

**Ambiente**

| SO | Python | AWS CLI | IDE | CDK |
|--- |--- |--- |--- |--- |
| Ubuntu 22.04 | 3.10.12 | 1.35.15 | VsCode | 2.166.0 |

**Requirements**

[![My Skills](https://skillicons.dev/icons?i=nodejs&perline=1)](https://skillicons.dev)  [Node.js](https://nodejs.org/en/download/package-manager)

[![My Skills](https://skillicons.dev/icons?i=aws&perline=1)](https://skillicons.dev)  [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

[![My Skills](https://skillicons.dev/icons?i=python&perline=1)](https://skillicons.dev)  [Python](https://www.python.org/downloads/)


**Instalação AWS CDK CLI**

```bash
npm install -g aws-cdk 
```

**Verificar a Instalação**

```bash 
cdk --version 
```

**Preparar o Ambiente AWS para utilização do CDK**

``` bash 
cdk bootstrap $AWS_ACCOUNT_ID/$AWS_DEFAULT_REGION 
```

**Exemplo de Inicialização (Python)**

```bash
 mkdir app && cd app 
```

```bash 
cdk init app --language python 
```




### Repositórios/Projetos

* `py-starter`  Criação de um bucket e uma função Lambda que retorna o ARN do Bucket
* `py_rest_api` Criação de uma API Gateway, tabela DynamoDB e uma função Lambda
* `py_cw_metrics`   Criação de alarmes no CloudWatch, tópico SNS e uma função Lambda que envia estes alarmes para um webhook (Usei o Slack)

Enjoy!