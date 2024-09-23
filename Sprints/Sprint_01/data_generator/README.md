
# Data Generator - Halo World
Este projeto é um gerador de dados para o Sprint 01 do projeto Halo World. Ele utiliza o Google Cloud BigQuery para gerar e processar dados.

Pré-requisitos
- Python 3.10 ou superior
- Google Cloud CLI
- Conta Google com acesso ao Google Cloud BigQuery
- Acesso à internet para baixar dependências e autenticar no Google Cloud
# Instruções para rodar o projeto
### 1. Clonar o repositório
Clone o repositório para sua máquina local:

```
git clone https://github.com/2RP-Squad404/Halo-World.git
```
Entre na pasta do projeto:

```
cd Halo-World/Sprints/Sprint_01/data_generator
``` 
## 2. Configurar o ambiente virtual
No Ubuntu:

1. Criar e ativar o ambiente virtual:

```
python3 -m venv .venv
source .venv/bin/activate
```

Caso você não tenha o pacote venv instalado, faça isso com:

```
sudo apt update
sudo apt install -y python3-venv
```

2. Instalar dependências:

Caso o projeto tenha um arquivo requirements.txt, instale as dependências com:

```
pip install -r requirements.txt
```

No Windows:
1. Criar e ativar o ambiente virtual:

No terminal, execute o seguinte comando para criar o ambiente virtual:

```
python -m venv .venv
```

Ative o ambiente virtual com:

```
.venv\Scripts\activate
```
2. Instalar dependências:

Caso o projeto tenha um arquivo requirements.txt, instale as dependências com:

```
pip install -r requirements.txt
```

## 3. Instalar a CLI do Google Cloud
No Ubuntu:
Instale a CLI do Google Cloud com o seguinte comando:

```
sudo snap install google-cloud-cli --classic
```

No Windows:
Baixe e instale a Google Cloud CLI [aqui](https://cloud.google.com/sdk/docs/install?hl=pt_br&_gl=1*hqmbvj*_up*MQ..&gclid=Cj0KCQjwo8S3BhDeARIsAFRmkOOgrCgnl9O-8Xvb8r41OvcYyrZeWzpr-tLnO8mhQMm0cx8lWGYHrwkaAhmnEALw_wcB&gclsrc=aw.ds).

1. abrir o terminal do google cloud sdk

2. Navegar até a pasta onde você clonou o projeto 
- exemplo: cd /home/seu-usuário/Halo-World/Sprints/Sprint_01/data_generator.py 

3. abrir em um editor de código 

4. criar ambiente virtual com o comando:
```
python -m venv .venv
```
5. Ativar o ambiente virtual com o comando:
```
.venv/Scripts/activate
```

6. Dentro do ambiente virtual instalar as dependências do projeto:
```
python install -r requirements.txt
```

## 4. Autenticar no Google Cloud
Após instalar a Google Cloud CLI, você precisa fazer login na sua conta Google:

```
gcloud auth login
```

Siga as instruções exibidas no navegador para completar o login.

## 6. Autenticar as credenciais padrão do aplicativo
Se for necessário configurar as credenciais padrão do Google Cloud para sua aplicação, execute o comando abaixo:

```
gcloud auth application-default login
```

Siga as instruções para completar o login.

## 7. Executar o script
Finalmente, execute o script data_generator.py:

```
python3 data_generator.py
```

No Windows, o comando seria:

```
python data_generator.py
```

## Contribuição
Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias e correções.

Com esse README.md, você tem um guia claro para rodar o projeto tanto no Ubuntu quanto no Windows. Certifique-se de ajustar as dependências específicas no arquivo requirements.txt, se necessário.









