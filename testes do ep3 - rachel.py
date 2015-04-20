# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:12:56 2015

@author: Rachel
"""


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
        return (calorias_ideais*1.2)
        
    elif fator == "baixo":
        return (calorias_ideais*1.375)
        
    elif fator == "medio":
        return (calorias_ideais*1.55)
        
    elif fator == "alto":
        return (calorias_ideais*1.725)
        
    else:  #fator == muito alto
        return (calorias_ideais*1.9)

fator_atividade() 