# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 08:43:50 2015

@author: Insper
"""

#------------------------------------------------------------------------------

'''
importando a biblioteca de alimentos
'''

def lista_alimentos(nome_do_arquivo="alimentos.csv"):
    text = open(nome_do_arquivo, 'r+', encoding = 'utf-8' )
    read = text.readlines() # lista suja
    lista_alimentos =[] # lista limpa
    for linha in read:                  #joga todas as palavras na lista limpa
        y = linha.strip().lower()
        if len(y) > 0:  
            lista_alimentos.append(y)        #adiciona as palavras a nova lista
    return lista_alimentos
    
lista_alimentos('alimentos.csv')

#------------------------------------------------------------------------------
'''
importanto a lista fornecida pelo execel
'''

def lista_usuário(nome_do_arquivo="usuario.csv"):
    text = open(nome_do_arquivo, 'r+', encoding = 'utf-8' )
    read = text.readlines() # lista suja
    lista_usuario =[] # lista limpa
    for linha in read:                  #joga todas as palavras na lista limpa
        y = linha.strip().lower()
        if len(y) > 0:  
            lista_usuario.append(y)         #adiciona as palavras a nova lista
    return lista_usuario
    
    
lista_usuário()

#------------------------------------------------------------------------------
    
    
    
    
    
    
    