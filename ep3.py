# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:52:19 2015

@author: Rachel Maria e Pedro Casella - Sala C

Esse programa calculará uma dieta semanal.
Dê suas informações e entre com os alimentos consumidos (quantidade em gramas).
O programa gerará um gráfico diário e um gráfico de IMC ideal.


"""
#EP3: Programa de Dieta Semanal 

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


alimentos_dia_1 = []     #elementos da lista são
alimentos_dia_2 = []     #números (calorias) que
alimentos_dia_3 = []     #serão somados no código
alimentos_dia_4 = []     #principal EP3.
alimentos_dia_5 = []
alimentos_dia_6 = []
alimentos_dia_7 = []

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

#ps.alimentos_consumidos_primeira_semana()#importa do arquivo o input do usuário

alimentos_consumidos_primeira_semana()

a1 = sum(alimentos_dia_1)
a2 = sum(alimentos_dia_2)
a3 = sum(alimentos_dia_3)           #faz a soma dos alimentos
a4 = sum(alimentos_dia_4)            #consumidos a cada dia e
a5 = sum(alimentos_dia_5)            #transforma nas variaveis 
a6 = sum(alimentos_dia_6)            #utilizadas no gráfico(consumo)
a7 = sum(alimentos_dia_7)


#------------------------------------------------------------------------------ 
'''
plota o gráfico do que foi consumido a cada dia da semana
'''

fig = plt.figure()

x = ('Dia 1', 'Dia 2', 'Dia 3', 'Dia 4', 'Dia 5', 'Dia 6', 'Dia 7')
y = (a1, a2, a3, a4, a5, a6, a7)
width = .35
ind = np.arange(len(y))    #divisão do espaço pelo número de dias(variaveis)
plt.bar(ind, y, color='lightpink',edgecolor='black',linewidth=1, width = 0.7)
plt.xticks(ind + width, x)
fig.autofmt_xdate()    #deixa a escrita na diagonal -->questão de estilo

plt.show()


#------------------------------------------------------------------------------
'''
fórmulas: calorias de acordo com características
input do usuário
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
 
      
relacao_calorica = calorias_ideais()


#------------------------------------------------------------------------------

'''
cálculo do IMC (Índice de Massa Corporal) - utilizando a nova fórmula
'''

imc = 1.3*peso/(altura**2.5)


#------------------------------------------------------------------------------
'''
fórmulas: calorias de acordo com grau de atividade física
'''

def fator_atividade(relacao_calorica):    
    fator = input("Informe seu fator de atividade\nMínimo, baixo, médio, alto ou muito alto:  ")    
    
    if fator == "minimo" or "mínimo":
        return (relacao_calorica*1.2)
        
    elif fator == "baixo":
        return (relacao_calorica*1.375)
        
    elif fator == "medio" or "médio":
        return (relacao_calorica*1.55)
        
    elif fator == "alto":
        return (relacao_calorica*1.725)
        
    else:  #fator == muito alto
        return (relacao_calorica*1.9)


ideal = fator_atividade(relacao_calorica)   #para uso no gráfico (comparação)

#------------------------------------------------------------------------------  
'''
plota o gráfico do que foi consumido na semana comparando com o ideal
'''

semana = (a1+a2+a3+a4+a5+a6+a7)/7

dias = ('Ideal', 'Semana', 'Dia 7', 'Dia 6', 'Dia 5', 'Dia 4', 'Dia 3', 'Dia 2', 'Dia 1')
y_pos = np.arange(len(dias))
calorias = ideal, semana, a7, a6, a5, a4, a3, a2, a1


plt.barh(y_pos, calorias, align='center', alpha=0.4, color='lightpink')
plt.yticks(y_pos, dias)
plt.xlabel('Calorias')
plt.title('Grafico Semanal - Compare o ideal, a media da semana e cada dia')

plt.show()


#------------------------------------------------------------------------------
'''
distribuições de necessidades por Heloísa Guarita

Calórica
- Proteínas = 20% das calorias
- Carboidratros = 60%
- Gorduras = 20%
'''

proteinas_ideais = ideal*0.2
carboidratos_ideias = ideal*0.6
gorduras_ideias = ideal*0.2
 
 
'''
Refeições
- Café da manhã: 20% das calorias diárias
- Lanche da manhã: 5%
- Almoço: 30%
- Lanche da tarde: 15%
- Jantar: 20%
- Ceia: 10%
'''


cafe = relacao_calorica*0.2
lanche_manha = relacao_calorica*0.05
almoco = relacao_calorica*0.3
lanche_tarde = relacao_calorica*0.15
jantar = relacao_calorica*0.2
ceia = relacao_calorica*0.1


#------------------------------------------------------------------------------
'''
plota um gráfico-pizza-demonstração de distribuição de refeições
'''

fig = plt.gcf()
fig.set_size_inches(4,4)

title('Distribuição Recomendada de Calorias por Refeição\n\n')
labels = 'Cafe', 'Lanche1', 'Almoco', 'Lanche2', 'Janta', 'Ceia'
sizes = [20, 5, 30, 15, 20, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'blue', 'pink']
explode = (0.05, 0.1, 0.05, 0.1, 0.05, 0.1) #serapação das rfeições
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal') #transforma em círculo

plt.show()
#------------------------------------------------------------------------------
'''
resultado do IMC
'''

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

#------------------------------------------------------------------------------
'''
soma de quantos kg o usuario engordou ou emagreceu
'''
e1 = ideal-a1
e2 = ideal-a2
e3 = ideal-a3
e4 = ideal-a4
e5 = ideal-a5
e6 = ideal-a6
e7 = ideal-a7

kg = e1+e2+e3+e4+e5+e6+e7/7000  #KG GANHO OU PERDA


#------------------------------------------------------------------------------
'''
gerando arquivo texto com as informações do usuário / IMC
'''

arquivo_texto = open('Informando-o-usuario', 'a')  #A para um append (o que já estava no arquivo vai para o final)
read = arquivo_texto.readlines()

arquivo_texto.write("Seu Índice de Massa Corporal, conhecido por IMC, é %f" % imc)
arquivo_texto.write("Assim, analisamos seu grau de obesidade, que é %s" %grau(imc))


if a1 > ideal:
    arquivo_texto.write("Você consumiu %d calorias a mais no Dia 1 do que foi indicado." %ideal-a1)
if a2 > ideal:
    arquivo_texto.write("Você consumiu %d calorias a mais no Dia 2 do que foi indicado." %ideal-a2)
if a3 > ideal:
    arquivo_texto.write("Você consumiu %d calorias a mais no Dia 3 do que foi indicado." %ideal-a3)
if a4 > ideal:
    arquivo_texto.write("Você consumiu %d calorias a mais no Dia 4 do que foi indicado." %ideal-a4)
if a5 > ideal:
    arquivo_texto.write("Você consumiu %d calorias a mais no Dia 5 do que foi indicado." %ideal-a5)
if a6 > ideal:
    arquivo_texto.write("Você consumiu %d calorias a mais no Dia 6 do que foi indicado." %ideal-a6)
if a7 > ideal:
    arquivo_texto.write("Você consumiu %d calorias a mais no Dia 7 do que foi indicado." %ideal-a7)    
if kg > 0:
    arquivo_texto.write("Você engordou %d kg até agora." %kg)
if kg < 0:
    arquivo_texto.write("Você engordou %d kg até agora." %kg)
    

arquivo_texto.write("Veja abaixo o significado dessas informações.")
#presente no arquivo já


arquivo_texto.close()
#------------------------------------------------------------------------------