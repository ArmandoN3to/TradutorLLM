
# Tradutor de Texto com OpenAI e LangChain

## Descrição
Este projeto utiliza a API da OpenAI para traduzir textos de forma automática, integrando diversas bibliotecas do LangChain para facilitar o fluxo de mensagens e manipulação de prompts. O sistema é configurado para usar variáveis de ambiente com `dotenv`, garantindo segurança no gerenciamento da chave de API.

## Técnicas Interessantes
- **Integração com OpenAI**: Através da biblioteca `langchain_openai`, o projeto utiliza o modelo `gpt-3.5-turbo-0125` para realizar traduções automáticas.
- **Pipeline de Processos**: Usando o conceito de *chain* (corrente), o projeto encadeia processos como geração de mensagens e interpretação dos resultados, facilitando o fluxo de trabalho sem a necessidade de invocar métodos manualmente.
- **Mensagens e Templates Dinâmicos**: A construção de mensagens dinâmicas com `ChatPromptTemplate` permite a inserção de variáveis como idioma e texto de forma simplificada.

## Tecnologias Utilizadas
- [LangChain](https://github.com/hwchase17/langchain): Framework para criar pipelines de processamento de linguagem natural.
- [OpenAI API](https://beta.openai.com/docs/): Utilizada para acesso aos modelos de linguagem GPT.
- [dotenv](https://pypi.org/project/python-dotenv/): Biblioteca para carregamento de variáveis de ambiente.

## Estrutura do Projeto

```bash
/
├── .env               # Arquivo contendo a chave da API (não incluído no repositório)
├── src/
│   ├── debug.py        # Arquivo principal do script
```

- **`src/`**: Contém os arquivos principais, incluindo o script Python e os templates de mensagens.
- **`.env`**: Contém as variáveis de ambiente, como a chave da API OpenAI, que são carregadas com `dotenv`.

## Como Funciona
O código utiliza a biblioteca `dotenv` para carregar a chave da API OpenAI do arquivo `.env`. As mensagens são construídas usando as classes `SystemMessage` e `HumanMessage`, e processadas com um modelo GPT da OpenAI, configurado para traduzir textos. Através do `ChatPromptTemplate`, o projeto cria templates dinâmicos que podem ser reutilizados para diferentes idiomas.
