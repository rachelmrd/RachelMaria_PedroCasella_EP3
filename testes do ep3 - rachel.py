# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:12:56 2015

@author: Rachel
"""
import primeira_semana as ps
from ep3 import lista_alimentos


alimentos={} #criando um dicionario vazio

for i in lista_alimentos('alimentos.csv'): #atribuindo valores às comidas
 alimento_caracteristica = i.split(',')
 chave = alimento_caracteristica[0]
 valores = alimento_caracteristica[1:]
 alimentos[chave] = valores
 


for ps.alimentos_dia_1 in alimentos:
    print("alimentos[ps.alimentos_dia_1[1]]")
    
    
    
'''
ps.alimentos_dia_2

ps.alimentos_dia_3

ps.alimentos_dia_4

ps.alimentos_dia_5

ps.alimentos_dia_6

ps.alimentos_dia_7
'''