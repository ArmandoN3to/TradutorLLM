from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

chave_api=os.getenv("OPENAI_API_KEY")

mensagens = [
    SystemMessage("Traduza o texto a seguir para ingles"),
    HumanMessage("oi!")
]
modelo= ChatOpenAI(model='gpt-3.5-turbo-0125')
parser = StrOutputParser()
chain = modelo | parser   #criar uma corrente para exetar cada processo em sequencia

# resposta = modelo.invoke(mensagens)       #Nós criamos uma corrente para nao ter que dar o INVOKE toda vez que for instanciar um novo objeto(etapa)
# texto = parser.invoke(resposta)       

template_mensagem = ChatPromptTemplate.from_messages([
    ("system","Traduza o texto a seguir para {idioma}"),
    ("user","{texto}"),
])

# print(template_mensagem.invoke({"idioma":"francês","texto": "oi!"}))
chain= template_mensagem| modelo| parser
texto = chain.invoke({"idioma":"francês","texto": "oi!"})

print(texto)

