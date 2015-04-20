# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:52:19 2015

@author: Rachel Maria e Pedro Casella - Sala C
"""

#EP3: Programa de Dieta Semanal 
import matplotlib as plt #para plotar os gráficos ideais do usuário


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
importando a lista do usuário fornecida pelo excel
'''

def lista_usuário(nome_do_arquivo="usuario.csv"):
    text = open(nome_do_arquivo, 'r+', encoding = 'utf-8' )
    read = text.readlines()[3:] #lista suja, pula as linhas de instrução
    lista_usuario =[] #lista limpa
    
    for linha in read:   #joga todas as palavras na lista limpa
        y = linha.strip().lower()
        if len(y) > 0:  
            lista_usuario.append(y) #adiciona as palavras à nova lista
    return lista_usuario
    
    
#print(lista_usuário('usuario.csv'))


#------------------------------------------------------------------------------
'''
criação do dicionario dos alimentos (caracteristicas) da biblioteca
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
fórmulas: calorias necessárias


def calorias_ideais():
    text = open('usuario.csv', 'r+', encoding = 'utf-8' )
    carac = text.readlines()[1:2] #lista suja, pega as linhas de instrução
    carac_usuario =[]  #lista limpa
    
    for linha in carac:  #joga todas as palavras na lista limpa
        y = linha.strip().lower()
        if len(y) > 0:  
            carac_usuario.append(y)  #adiciona as palavras a nova lista
    
    
    #TRANSFORMANDO AS INFORMAÇÕES EM ELEMENTOS DE LISTA
    carac_usuario = carac_usuario[0].strip().split(",")
    

    #IDENTIFICAÇÃO DE CARACTERÍSTICAS DO USUÁRIO
    #chave = carac_usuario[0]
    altura = carac_usuario[4]
    list(altura)
    peso = carac_usuario[2]
    list(peso)
    idade = carac_usuario[1]
    list(idade)
    sexo = carac_usuario[3]
    
    #DEFINIÇÃO DAS CALORIAS DIÁRIAS DO USUÁRIO
    if sexo == "m":
        return (88,36+(13,4*peso)+(4,8*altura*100)-(5,7*idade))
    else:
        return (447,6+(9,2*peso)+(3,1*altura)-(4,3*idade))
        
print(calorias_ideais())
'''

def calorias_ideais():
    altura = float(input("Dê suas seguintes informações. Altura:  "))
    peso = float(input("Peso:  "))
    idade = float(input("Idade:  "))
    sexo = ("Sexo:  ")

    if sexo == "m":
        return (88,36+(13,4*peso)+(4,8*altura*100)-(5,7*idade))
    else:
        return (447,6+(9,2*peso)+(3,1*altura)-(4,3*idade))
 
calorias_ideais()       
print(calorias_ideais())


#------------------------------------------------------------------------------
'''
fórmulas: grau de atividade física
'''

def fator_atividade():
    text = open('usuario.csv', 'r+', encoding = 'utf-8' )
    carac = text.readlines()[1:2] #lista suja, pega as linhas de instrução
    carac_usuario =[]  #lista limpa
    
    for linha in carac:  #joga todas as palavras na lista limpa
        y = linha.strip().lower()
        if len(y) > 0:  
            carac_usuario.append(y)  #adiciona as palavras a nova lista
    
    
    #TRANSFORMANDO AS INFORMAÇÕES EM ELEMENTOS DE LISTA
    carac_usuario = carac_usuario[0].strip().split(",")
    fator = carac_usuario[5]
    
    if fator == "minimo":
        return (calorias_ideais*1,2)
        
    elif fator == "baixo":
        return (calorias_ideais*1,375)
        
    elif fator == "medio":
        return (calorias_ideais*1,55)
        
    elif fator == "alto":
        return (calorias_ideais*1,725)
        
    else:  #fator == muito alto
        return (calorias_ideais*1,9)

  
#------------------------------------------------------------------------------
'''
distribuições de necessidades por Heloísa Guarita (veja em README)

Calórica
- Proteínas = 20% das calorias
- Carboidratros = 60%
- Gorduras = 20%
'''

def proteinas_ideais(fator_atividade):
    return fator_atividade*0,2
  
  
def carboidratos_ideias(fator_atividade):
    return fator_atividade*0,6

  
def gorduras_ideias(fator_atividade):
    return fator_atividade*0,2
 
 
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
    cafe = calorias_ideais*0.2
    lanche_manha = calorias_ideais*0.05
    almoco = calorias_ideais*0.3
    lanche_tarde = calorias_ideais*0.15
    jantar = calorias_ideais*0.2
    ceia = calorias_ideais*0.1

    return (cafe+lanche_manha+almoco+lanche_tarde+jantar+ceia)


#------------------------------------------------------------------------------








