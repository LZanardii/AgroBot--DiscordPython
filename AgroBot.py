### AgroBot - Projeto para o Desenvolve Tech - Sicredi/Puc 
# Bot para o aplicativo discord que retorna o valor das comodities   

import discord
from discord import message #importando a lib discord.py 
from discord.ext import commands #importando comandos da lib
import asyncio #importando a lib asyncio
import csv # importando lib csv

#importando limpa terminal
import os 
os.system('cls') or None

# CONFIGURAÇÕES DO BOT
# O usuário deve utilizar o prefixo '!' antes de inserir qualquer comando;
# O AgroBot é case insensitive, portanto, não importa o formato case após o prefixo;
client = commands.Bot(command_prefix = '!' , case_insensitive = True)  

#Inicializando o AgroBotot no server  
@client.event
async def on_ready():
    print(f'Inicalizando seu @{client.user}\n')
    @client.command()
    async def AgroBot(parametro):
        await parametro.send('''Ola!
Para mais interações use os códigos a seguir...

!meuID       : para autenticar seu cadastro
!agroTech  : para acessar o menu (após autenticar o cadastro)
!menu '1'    : para navegar no menu (ex: !menu 1)

Lembre-se de não esquecer de colocar o '!' antes de inserir os códigos de interação.
Verifique seu cadastro com "!meuID" para desbloquear as outras funções.''')


@client.command() # verifica o chat para achar comandos

async def meuID(parametro): # "!meuID" é o comando que vai inicializar/liberar as funções do AgroBot
                         
    if parametro.author.id == 'id do usuario que vai interagir com o bot': #if que verifica/autoriza o usuário a interagir com o AgroBot pelo id so usuário
        print('Usuário autenticado no prompt')
        await parametro.send(f'''Buenas e me espalho  @{parametro.author}. 
Seu usuário foi autenticado com sucesso.''')
        
        @client.command() # iniciando outra verificação de comando no chat
        
        async def agrotech(parametro): # '!agrotech' explode o menu no chat
            await parametro.send(f''' Qual commodity do AGRO você quer obter informações?
1 - Milho
2 - Soja
3 - Trigo
4 - Café ''')
        
        @client.command()  # iniciando outra verificação de comando no chat
        
        async def menu(parametro, varMenu): # "menu + nome da commodity" vai selecionar a informação que o usuário quer (varMenu)
            
            if varMenu == '1' : # if responsável por explodir informações caso o cliente deseje saber sobre milho
                arq = open('commodities.csv', 'r') # arquivo que contem as informações fantasia de valor/tendência do gráfico 
                linha = arq.readlines()[1]  # variavel que instancia a linha do arquivo csv
                frase = (f'''Valor da saca US {linha[6:11]}
Tendência de {linha[13:18].upper()} na bolsa de valores.''') # variável frase é a que sera printada na tela, já formatada               
                await parametro.send(frase)

            elif varMenu ==  '2' : # if responsável por explodir informações caso o cliente deseje saber sobre soja
                arq = open('commodities.csv', 'r') # arquivo que contem as informações fantasia de valor/tendência do gráfico 
                linha = arq.readlines()[2]  # variavel que instancia a linha do arquivo csv
                frase = (f'''Valor da saca US {linha[5:11]}
Tendência de {linha[13:18].upper()} na bolsa de valores.''') # variável frase é a que sera printada na tela, já formatada              
                await parametro.send(frase)

            elif varMenu ==  '3' : # if responsável por explodir informações caso o cliente deseje saber sobre 
                arq = open('commodities.csv', 'r') # arquivo que contem as informações fantasia de valor/tendência do gráfico 
                linha = arq.readlines()[2]  # variavel que instancia a linha do arquivo csv
                frase = (f'''Valor da saca US {linha[6:11]}
Tendência de {linha[13:18].upper()} na bolsa de valores.''') # variável frase é a que sera printada na tela, já formatada             
                await parametro.send(frase)

            elif varMenu ==  '4' : # if responsável por explodir informações caso o cliente deseje saber sobre cafe
                arq = open('commodities.csv', 'r') # arquivo que contem as informações fantasia de valor/tendência do gráfico 
                linha = arq.readlines()[3]  # variavel que instancia a linha do arquivo csv
                frase = (f'''Valor da saca US {linha[6:11]}
Tendência de {linha[13:18].upper()} na bolsa de valores.''') # variável frase é a que sera printada na tela, já formatada         
                await parametro.send(frase)

    else: # else que retorna a verificação de usuário
        await parametro.send('''Você não possui em seu cadastro o ID necessário para falar comigo.
Desculpe \U0001F615''' )


#metodo que faz o bot rodar
client.run('toke do bot encontrado na platadorma do discord')




