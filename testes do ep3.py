# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 08:43:50 2015

@author: Insper
"""

#------------------------------------------------------------------------------

'''
importando a biblioteca de alimentos
'''

def biblioteca_alimentos(nome_do_arquivo="alimentos.csv"):
    text = open(nome_do_arquivo, 'r+', encoding = 'utf-8' )
    read = text.readlines() # lista suja
    lista_alimentos =[] # lista limpa
    for linha in read:                  #joga todas as palavras na lista limpa
        y = linha.strip().lower()
        if len(y) > 0:  
            lista_alimentos.append(y)        #adiciona as palavras a nova lista
    print(lista_alimentos)
    return lista_alimentos
   
lista_alimentos=biblioteca_alimentos('alimentos.csv')

#------------------------------------------------------------------------------
'''
criação do dicionario dos alimetos da biblioteca
'''

alimentos={} #criando um dicionario vazio

for i in lista_alimentos: #atribuindo as minhas comidas valores
 alimento_caracteristica=i.split(',')
 chave = alimento_caracteristica[0]
 valores = alimento_caracteristica[1:]
 alimentos[chave] = valores
 
print(alimentos)
print(alimentos['banana da terra'][1]) 
'''

#------------------------------------------------------------------------------
#importanto a lista fornecida pelo execel
'''

def lista_usuário(nome_do_arquivo="usuario.csv"):
    text = open(nome_do_arquivo, 'r+', encoding = 'utf-8' )
    read = text.readlines() # lista suja
    lista_usuario =[] # lista limpa
    for linha in read:                  #joga todas as palavras na lista limpa
        y = linha.strip().lower()
        if len(y) > 0:  
            lista_usuario.append(y)         #adiciona as palavras a nova lista
    print(lista_usuario)
    return lista_usuario
    
    
lista_usuário()

#------------------------------------------------------------------------------
'''
criação do dicionario do usuario
-data 
-quantidade calorica
'''


alimentos_ingeridos = {} #dicionario de alimentos comidos
    
text = open('usuario.csv', 'r+', encoding = 'utf-8' )
   
read = text.readlines() # lista suja
for line in read:
    print(line.strip().split(','))
    
    

    
    
    
    