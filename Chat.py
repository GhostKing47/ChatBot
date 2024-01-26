import nltk
from nltk.chat.util import Chat, reflections
import subprocess
import os

# Baixar o pacote de dados do nltk
nltk.download('punkt')

os.system('clear')
os.system('neofetch')

pares = [
    ["Meu nome é (.*)", ["Oi, como posso ajudar?"]],
    ["Qual é o seu nome?", ["Meu nome é Assistente ChatGPT."]],
    ["(.*) ajuda (.*)", ["Eu posso ajudar em muitas coisas. O que você precisa?"]],
    ["(.*) sua IA favorita?", ["Claro, eu sou a melhor!"]],
    # Padrões de respostas para dúvidas no Termux
    ["Como instalo um pacote no Termux?", ["Para instalar um pacote, use 'pkg install <nome_do_pacote>'."]],
    ["Como atualizo os pacotes no Termux?", ["Você pode atualizar os pacotes com 'pkg upgrade'."]],
    ["Onde encontro meus arquivos no Termux?", ["Os arquivos geralmente estão em '/data/data/com.termux/files/home/'."]],
    ["Como saio do Termux?", ["Para sair, use 'exit' ou pressione 'CTRL + D'."]],
    # Adicione mais padrões de respostas conforme necessário
    # ...
]

# Configurar e iniciar o chat
chatbot = Chat(pares, reflections)

print("Olá!, como posso ajudar?")

# Loop para interação contínua
while True:
    pergunta_usuario = input("Você: ")

    if pergunta_usuario.lower() == "executar comando":
        comando = input("Digite o comando a ser executado no Termux: ")
        print(f"Executando o comando: {comando}")
        print("Porfavor aguarde...")
        try:
            resultado = subprocess.check_output(comando, shell=True, stderr=subprocess.STDOUT, text=True)
            print("Resultado do comando:")
            print(resultado)
        except subprocess.CalledProcessError as e:
            print("Erro ao executar o comando:")
            print(e.output)
    else:
        resposta = chatbot.respond(pergunta_usuario)
        print("Assistente:", resposta)
