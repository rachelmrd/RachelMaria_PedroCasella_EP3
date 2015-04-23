# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 08:43:50 2015

@author: Insper
"""

import primeira_semana as ps


import primeira_semana as ps
import numpy as np
from matplotlib import pyplot as plt
from pylab import *


#------------------------------------------------------------------------------
'''
importando a biblioteca de alimentos como lista
'''

def lista_alimentos(nome_do_arquivo="alimentos.csv"):
    text = open(nome_do_arquivo, 'r+')
    read = text.readlines() #lista suja
    lista_alimentos =[] #lista limpa
    for linha in read:  #joga todas as palavras na lista limpa
        y = linha.strip().lower()
        if len(y) > 0:  
            lista_alimentos.append(y)  #adiciona as palavras a nova lista
    return lista_alimentos
    
    
lista_alimentos('alimentos.csv')


#------------------------------------------------------------------------------
'''
criação do dicionario dos alimentos com suas caracteristicas 
'''

alimentos={} #criando um dicionario vazio

for i in lista_alimentos('alimentos.csv'): #atribuindo valores às comidas
    alimento_caracteristica = i.split(',')
    chave = alimento_caracteristica[0]
    valores = alimento_caracteristica[1:]
    alimentos[chave] = valores               #dicionário
 

#------------------------------------------------------------------------------


alimentos_proteinas = []
alimentos_lipidios = []
alimentos_carboidratos = []

def funcao_grafico_proteina():
    
    
    
        #armazenando informações de quantidade de proteinas
        quantidade_nominal_proteina = float(alimentos[str(alimento_usuario)][2])
        y = (quantidade_nominal_proteina*quantidade)/100
        alimentos_proteinas.append(y)
        #armazenando informações de quantidade de lipidios 
        quantidade_nominal_lipidios = float(alimentos[str(alimento_usuario)][4])
        z = (quantidade_nominal_lipidios*quantidade)/100
        alimentos_lipidios.append(z)
        #armazenamento informações de quantidade de carboidratos 
        quantidade_nominal_carboidratos = float(alimentos[str(alimento_usuario)][3])
        j = (quantidade_nominal_carboidratos*quantidade)/100
        alimentos_carboidratos.append(j)
        
        
        
        
        
        
        