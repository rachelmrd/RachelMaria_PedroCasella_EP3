# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:12:56 2015

@author: Rachel
"""

'''
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import ep3 as ep

# Example data
dias = ('Dia 7', 'Dia 6', 'Dia 5', 'Dia 4', 'Dia 3', 'Dia 2', 'Dia 1')
y_pos = np.arange(len(dias))
y = ep.a1, ep.a2, ep.a3, ep.a4, ep.a5, ep.a6, ep.a7
#error = np.random.rand(len(dias))

plt.barh(y_pos, y, align='center', alpha=0.4, color = 'lightpink')
plt.yticks(y_pos, dias)
plt.xlabel('Calorias Consumidas')
plt.title('Gráfico Semanal')

plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt


a1 = 1523
a2 = 2156
a3 = 1658
a4 = 1793
a5 = 1500
a6 = 1632
a7 = 2001
ideal = 1500


'''
N = 7
menMeans   = (a1, a2, a3, a4, a5, a6, a7)
#womenMeans = (25, 32, 34, 20, 25)
#menStd     = (2, 3, 4, 1, 2)
#womenStd   = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans,   width, color='r')

plt.ylabel('Calorias')
plt.title('Grafico Semanal')
plt.xticks(ind+width/2., ('Dia 1', 'Dia 2', 'Dia 3', 'Dia 4', 'Dia 5', 'Dia 6', 'Dia 7'))
plt.yticks(np.arange(0,10000,10))
plt.legend( (p1[0]), ('Men', 'Women') )

plt.show()
'''
from pylab import title

title('Distribuicao recomendada de calorias por refeicao', bbox={'facecolor':'0.8', 'pad':3})
labels = 'Cafe', 'Lanche1', 'Almoco', 'Lanche2', 'Janta', 'Ceia'
sizes = [20, 5, 30, 15, 20, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'blue', 'pink']
explode = (0.05, 0.1, 0.05, 0.1, 0.05, 0.1) #serapação das rfeições
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal') #transforma em círculo

plt.show()






