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
'''
import numpy as np
import matplotlib.pyplot as plt
'''

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


fig = plt.figure()

x = ('Dia 1', 'Dia 2', 'Dia 3', 'Dia 4', 'Dia 5', 'Dia 6', 'Dia 7')
y = (a1, a2, a3, a4, a5, a6, a7)
width = .35
ind = np.arange(len(y))    #divisão do espaço pelo número de dias(variaveis)
plt.bar(ind, y, color='lightpink',edgecolor='black',linewidth=1, width = 0.7)
plt.xticks(ind + width, x)
fig.autofmt_xdate()

plt.show()






