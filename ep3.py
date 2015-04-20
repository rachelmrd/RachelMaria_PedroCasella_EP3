# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:52:19 2015

@author: Rachel Maria e Pedro Casella - Sala C

Esse programa calculará sua dieta semanal.
Dê suas informações e entre com os alimentos consumidos (quantidade em gramas).
O programa gerará um gráfico diário e um gráfico de IMC ideal.



"""


#EP3: Programa de Dieta Semanal 
import matplotlib as plt #para plotar os gráficos ideais do usuário
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
 


#TESTES:
#print(alimentos)       
#print(alimentos['banana da terra'][1]) 


#------------------------------------------------------------------------------
'''
input dos alimentos diários do usuário - para uma semana apenas
'''

ps.alimentos_consumidos_primeira_semana()


#------------------------------------------------------------------------------
'''
cálculo do que foi ingerido - parte foda
'''


for ps.alimentos_dia_1 in alimentos:
    print(alimentos[ps.alimentos_dia_1[1]])
    
'''
ps.alimentos_dia_2

ps.alimentos_dia_3

ps.alimentos_dia_4

ps.alimentos_dia_5

ps.alimentos_dia_6

ps.alimentos_dia_7
'''


#------------------------------------------------------------------------------  
'''
plota o gráfico do que foi consumido 
'''
   
   
#------------------------------------------------------------------------------
'''
fórmulas: calorias ideias a serem consumidas
input do usuário de suas características
'''

def calorias_ideais():
    altura = float(input("Dê suas seguintes informações. Altura:  "))
    peso = float(input("Peso:  "))
    idade = float(input("Idade:  "))
    sexo = input("Sexo:  ")

    if sexo == "m" or "masculino":
        return (88.36+(13.4*peso)+(4.8*altura*100)-(5.7*idade))
    else:
        return (447.6+(9.2*peso)+(3.1*altura)-(4.3*idade))
 
      
print(calorias_ideais())
relaçao_calorica = calorias_ideais()


#------------------------------------------------------------------------------
'''
fórmulas: grau de atividade física
'''
relaçao_calorica = calorias_ideais()
def fator_atividade(relacao_calorica):    
    fator = input("Informe seu fator de atividade\n (mínimo, baixo, médio, alto ou muito alto):  ")    
    
    if fator == "minimo" or "mínimo":
        return (relaçao_calorica*1.2)
        
    elif fator == "baixo":
        return (relaçao_calorica*1.375)
        
    elif fator == "medio" or "médio":
        return (relaçao_calorica*1.55)
        
    elif fator == "alto":
        return (relaçao_calorica*1.725)
        
    else:  #fator == muito alto
        return (relaçao_calorica*1.9)

fator_atividade() 
ativ_fisica = fator_atividade()

#------------------------------------------------------------------------------
'''
plota o gráfico ideal 
'''






#------------------------------------------------------------------------------
'''
distribuições de necessidades por Heloísa Guarita (veja em README)

Calórica
- Proteínas = 20% das calorias
- Carboidratros = 60%
- Gorduras = 20%
'''

def proteinas_ideais(fator_atividade):
    return ativ_fisica*0.2
  
  
def carboidratos_ideias(fator_atividade):
    return ativ_fisica*0.6

  
def gorduras_ideias(fator_atividade):
    return ativ_fisica*0.2
 
 
'''
Refeições
- Café da manhã: 20% das calorias diárias
- Lanche da manhã: 5%
- Almoço: 30%
- Lanche da tarde: 15%
- Jantar: 20%
- Ceia: 10%
'''

def dieta(calorias_ideais):
    cafe = relaçao_calorica*0.2
    lanche_manha = relaçao_calorica*0.05
    almoco = relaçao_calorica*0.3
    lanche_tarde = relaçao_calorica*0.15
    jantar = relaçao_calorica*0.2
    ceia = relaçao_calorica*0.1

    return (cafe+lanche_manha+almoco+lanche_tarde+jantar+ceia)


#------------------------------------------------------------------------------








