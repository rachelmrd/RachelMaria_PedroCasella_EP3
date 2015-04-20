# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 08:43:50 2015

@author: Insper
"""

import primeira_semana as ps


#------------------------------------------------------------------------------
'''
importando a biblioteca de alimentos como lista
'''

def lista_alimentos(nome_do_arquivo="alimentos.csv"):
    text = open(nome_do_arquivo, 'r+', encoding = 'utf-8' )
    read = text.readlines() #lista suja
    lista_alimentos =[] #lista limpa
    for linha in read:   #joga todas as palavras na lista limpa
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
 alimentos[chave] = valores
 


alimentos_dia_1 = []


    
while True:
   alimento_usuario = input("Informe os alimentos consumidos no primeiro dia:  ")
   
   if alimento_usuario == "fim":
       break
   
   quantidade = float(input("Quantas gramas de cada alimento?:  "))
   
   
   
   quantidade_nominal = float(alimentos[str(alimento_usuario)][1])
   
   x = (quantidade_nominal*quantidade)/100

   print(x)
   
   alimentos_dia_1.append(x)
   
print(alimentos_dia_1)

print(sum(alimentos_dia_1))
    
