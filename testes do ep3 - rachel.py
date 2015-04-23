# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:12:56 2015

@author: Rachel
"""

imc = 22

def grau(imc):
    if imc < 16:
        return "Magreza grave"
    elif 16<=imc<17:
        return "Magreza moderada"
    elif 17<=imc<18.5:
        return "Magreza leve"
    elif 18.5<=imc<25:
        return "Saudável"
    elif 25<=imc<30:
        return "Sobrepeso"
    elif 30<=imc<35:
        return "Obesidade Grau I"
    elif 35<=imc<40:
        return "Obesidade Grau II"
    elif 40<=imc:
        return "Obesidade Grau III: mórbida"

grau(imc)
print("Assim, analisamos seu grau de obesidade, que é %s" %grau(imc)) 