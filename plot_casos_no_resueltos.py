#BASADO EN: https://stackoverflow.com/questions/41400136/how-to-do-waffle-charts-in-python-square-piechart

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("https://raw.githubusercontent.com/alexandersolis/poligran_mineria_de_datos_2/main/Datos_PQRS.csv")

labels = []
values = []
for label, value in df.groupby('ESTADO').size().iteritems():
    labels.append(label)
    values.append(value)

print(labels)
print(values)

barlist = plt.bar(labels, values)

barlist[0].set_color('r')
barlist[1].set_color('g')
barlist[2].set_color('b')

#plt.xlabel('ESTADO')
plt.ylabel("CASOS")

for i in range(len(labels)):
    plt.annotate(str(values[i]), xy=(labels[i], values[i]), ha='center', va='bottom')

plt.show()
