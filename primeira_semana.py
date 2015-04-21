# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:58:00 2015

@author: Rachel
"""

import ep3 as ep

alimentos_dia_1 = []     #elementos da lista são
alimentos_dia_2 = []     #números (calorias) que
alimentos_dia_3 = []     #serão somados no código
alimentos_dia_4 = []     #principal EP3.
alimentos_dia_5 = []
alimentos_dia_6 = []
alimentos_dia_7 = []

alimentos = ep.alimentos

def alimentos_consumidos_primeira_semana():
    
    while True:
        alimento_usuario = input("Informe os alimentos consumidos no primeiro dia:  ")
        if alimento_usuario == "fim":
            break
        quantidade = float(input("Quantas gramas?:  "))
        quantidade_nominal = float(alimentos[str(alimento_usuario)][1])
        x = (quantidade_nominal*quantidade)/100
        alimentos_dia_1.append(x)
            
    
    while True:
        alimento_usuario = input("Informe os alimentos consumidos no segundo dia:  ")
        if alimento_usuario == "fim":
            break
            
        quantidade = float(input("Quantas gramas?:  "))
        quantidade_nominal = float(alimentos[str(alimento_usuario)][1])
        x = (quantidade_nominal*quantidade)/100
        alimentos_dia_2.append(x)
    
    
    while True:
        alimento_usuario = input("Informe os alimentos consumidos no terceiro dia:  ")
        if alimento_usuario == "fim":
            break
            
        quantidade = float(input("Quantas gramas?:  "))
        quantidade_nominal = float(alimentos[str(alimento_usuario)][1])
        x = (quantidade_nominal*quantidade)/100
        alimentos_dia_3.append(x)
        
    
    
    while True:
        alimento_usuario = input("Informe os alimentos consumidos no quarto dia:  ")
        if alimento_usuario == "fim":
            break
            
        quantidade = float(input("Quantas gramas?:  "))
        quantidade_nominal = float(alimentos[str(alimento_usuario)][1])
        x = (quantidade_nominal*quantidade)/100
        alimentos_dia_4.append(x)
    
    while True:
        alimento_usuario = input("Informe os alimentos consumidos no quinto dia:  ")
        if alimento_usuario == "fim":
            break
            
        quantidade = float(input("Quantas gramas?:  "))
        quantidade_nominal = float(alimentos[str(alimento_usuario)][1])
        x = (quantidade_nominal*quantidade)/100
        alimentos_dia_5.append(x)
    
    
    while True:
        alimento_usuario = input("Informe os alimentos consumidos no sexto dia:  ")
        if alimento_usuario == "fim":
            break
            
        quantidade = float(input("Quantas gramas?:  "))
        quantidade_nominal = float(alimentos[str(alimento_usuario)][1])
        x = (quantidade_nominal*quantidade)/100
        alimentos_dia_6.append(x)
        
    
    while True:
        alimento_usuario = input("Informe os alimentos consumidos no sétimo dia:  ")
        if alimento_usuario == "fim":
            break
        quantidade = float(input("Quantas gramas?  "))
        quantidade_nominal = float(alimentos[str(alimento_usuario)][1])
        x = (quantidade_nominal*quantidade)/100
        alimentos_dia_6.append(x)