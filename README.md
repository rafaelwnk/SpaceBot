# SpaceBot

O SpaceBot é um chatbot desenvolvido com Django que permite aos usuários obter informações detalhadas sobre satélites. Ele utiliza um modelo de inteligência artificial da Groq e um banco de dados SQLite como RAG (Retrieval-Augmented Generation) para aumentar o contexto das respostas da IA.

Os dados utilizados para o RAG são coletados por meio de web scraping do site [Heavens Above](https://www.heavens-above.com/Satellites.aspx), garantindo informações atualizadas e detalhadas sobre os satélites em órbita.

## Instalação
Siga os passos abaixo para configurar e executar o projeto localmente.

### 1. Clonar o repositório
```bash
$ git clone https://github.com/rafaelwnk/SpaceBot.git
$ cd SpaceBot
```

### 2. Criar e ativar um ambiente virtual
#### Linux/macOS:
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

#### Windows:
```bash
$ python -m venv venv
$ venv\Scripts\activate
```

### 3. Instalar as dependências
As dependências estão listadas no arquivo `requirements.txt`. Para instalá-las, execute:
```bash
$ pip install -r requirements.txt
```

## Considerações Finais
O SpaceBot foi desenvolvido com fins de estudo e aprendizado, buscando aprimorar conhecimentos em desenvolvimento web, inteligência artificial e web scraping. Qualquer feedback ou sugestão será muito bem-vindo!










