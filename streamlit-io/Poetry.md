
# Passo a Passo: Criando um Projeto Virtualizado com Poetry no Python 3.12

Este guia irá te ajudar a configurar um projeto Python virtualizado usando o `Poetry` no Windows 10 com Python 3.12. O nome do projeto será `streamlit-io`.

## Passo 1: Instalar Python 3.12

### 1.1 Baixar Python 3.12

- Acesse o site oficial do Python: [https://www.python.org/downloads/release/python-3120/](https://www.python.org/downloads/release/python-3120/)
- Baixe o instalador adequado para o Windows 10 (recomenda-se "Windows installer (64-bit)").

### 1.2 Instalar Python

- Execute o instalador e marque a opção para **Adicionar o Python ao PATH**.
- Siga as instruções da instalação.

### 1.3 Verificar a Instalação

Abra o terminal (cmd ou PowerShell) e execute:

```bash
python --version
```

A saída deve ser algo como:

```
Python 3.12.x
```

## Passo 2: Instalar o Poetry

### 2.1 Instalar o Poetry

No PowerShell ou cmd, execute o comando:

```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### 2.2 Configurar o PATH

Adicione a pasta do Poetry ao PATH. A pasta do Poetry geralmente está localizada em:

```bash
%USERPROFILE%\.local\bin
```

Você pode adicionar essa pasta ao PATH através das configurações de "Variáveis de Ambiente" do Windows.

### 2.3 Verificar a Instalação

Verifique se o Poetry foi instalado corretamente executando:

```bash
poetry --version
```

## Passo 3: Criar o Projeto com Poetry

### 3.1 Criar a Pasta do Projeto

No terminal, crie uma nova pasta e entre nela:

```bash
mkdir streamlit-io
cd streamlit-io
```

### 3.2 Inicializar o Projeto

Inicialize o projeto com o comando:

```bash
poetry init
```

Durante a configuração interativa, você pode preencher as seguintes opções:

- **Nome do pacote**: `streamlit-io`
- **Versão**: `0.1.0`
- **Descrição**: Exemplo de um projeto usando Streamlit
- **Autor**: Seu nome ou equipe
- **Licença**: `MIT` (ou outra de sua escolha)
- Pule a adição de dependências por enquanto.

Isso criará o arquivo `pyproject.toml` com as configurações básicas do projeto.

## Passo 4: Configurar o Ambiente Virtual

### 4.1 Criar o Ambiente Virtual

Para criar o ambiente virtual e instalar as dependências, execute:

```bash
poetry install
```

### 4.2 Ativar o Ambiente Virtual

Ative o ambiente virtual com o comando:

```bash
poetry shell
```

Agora, você está no ambiente virtual configurado pelo Poetry.

## Passo 5: Adicionar Dependências (Streamlit)

### 5.1 Adicionar o Streamlit

Adicione a dependência `Streamlit` ao projeto com:

```bash
poetry add streamlit
```

O Poetry instalará o Streamlit e atualizará o arquivo `pyproject.toml`.

## Passo 6: Testar o Streamlit

### 6.1 Criar um Arquivo de Exemplo

Dentro da pasta do projeto, crie um arquivo chamado `app.py` com o seguinte conteúdo:

```python
import streamlit as st

st.title("Hello, Streamlit!")
st.write("Este é um exemplo de aplicação usando Streamlit.")
```

### 6.2 Executar o Aplicativo Streamlit

Execute o aplicativo com o comando:

```bash
streamlit run app.py
```

Isso abrirá o navegador com a aplicação `Streamlit`.

## Passo 7: Finalizar o Projeto

Agora que o ambiente virtual foi configurado com sucesso, você pode continuar desenvolvendo sua aplicação `Streamlit`.

Para sair do ambiente virtual, use:

```bash
exit
```

## Passo 8: Dicas Adicionais

### 8.1 Verificar o Ambiente Virtual

Para verificar informações sobre o ambiente virtual, use:

```bash
poetry env info
```

### 8.2 Adicionar Dependências de Desenvolvimento

Para adicionar dependências que serão usadas apenas durante o desenvolvimento, como ferramentas de linting ou testes, use o argumento `--dev`:

```bash
poetry add --dev flake8
```

### 8.3 Remover o Ambiente Virtual

Se precisar remover o ambiente virtual e recriá-lo, execute:

```bash
poetry env remove python
```

Com isso, você finalizou a configuração do projeto `streamlit-io` utilizando o `Poetry` e Python 3.12 no Windows 10.
