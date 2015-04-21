# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:12:56 2015

@author: Rachel
"""
import primeira_semana as ps
import ep3 as ep


import plotly.plotly as py
from plotly.graph_objs import *

def grafico_consumo_comparado(a1,a2,a3,a4,a5,a6,a7):
    data = Data([
        Bar(
            x=['Dia 1', 'Dia 2', 'Dia 3', 'Dia 4', 'Dia 5', 'Dia 6', 'Dia 7'],
            y=[a1, a2, a3, a4, a5, a6, a7]
        )
    ])
    py.plot(data, filename = 'Gráfico das calorias ingeridas nessa semana')
    
        
grafico_consumo_comprado(a1,a2,a3,a4,a5,a6,a7)  #chama a função gráfico consumo  
