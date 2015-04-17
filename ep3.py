# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:52:19 2015

@author: Rachel Maria e Pedro Casella - Sala C
"""

#EP3: Programa de Dieta Semanal 

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










#CHECANDO SE FUNCIONA - Rachel
for entrada_usuario in alimentos:
    print (entradas_usuario)



#FÓRMULAS
#CALORIAS NECESSÁRIAS - Rachel
def calorias_necessarias():
    peso = keys.entrada_usuario(ALTURA)
    altura = keys.entrada_usuario(PESO (kg))
    idade = keys.entrada_usuario(IDADE)
    sexo = keys.entrada_usuario(SEXO)
    
    if sexo == H:
        return (88,36+(13,4*peso)+(4,8*altura)-(5,7*idade))
    else:
        return (447,6+(9,2*peso)+(3,1*altura)-(4,3*idade))
        

#GRAU DE ATIVIDADE FISICA - Rachel
def fator_atividade():
    fator = keys,entrada_usuario(Fator)
    
    if fator == minimo:
        energia = (calorias_necessarias*1,2)
        
    elif fator == baixo:
        energia = (calorias_necessarias*1,375)
        
    elif fator == medio:
        energia = (calorias_necessarias*1,55)
        
    elif fator == alto:
        energia = (calorias_necessarias*1,725)
        
    else:  #fator == muito alto
        energia = (calorias_necessarias*1,9)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
