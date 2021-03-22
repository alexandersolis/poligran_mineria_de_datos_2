import pandas as pd
import matplotlib.pyplot as plt

labels = ['SEM1', 'SEM2', 'SEM3', 'SEM4', 'SEM5']
peticiones = [0, 8, 5, 1, 1]
quejas = [3, 3, 2, 12, 8]
reclamos = [0, 1, 18, 13, 9]
soliciturdes = [0, 0, 8, 8, 0]

df_casos = pd.DataFrame(columns=labels)
df_casos.loc[0] = peticiones
df_casos.loc[1] = quejas
df_casos.loc[2] = reclamos
df_casos.loc[3] = soliciturdes

print(df_casos)

width = 0.35       

fig, ax = plt.subplots()

ax.bar(labels, peticiones, width, label='PETICIONES')
ax.bar(labels, quejas, width, label='QUEJAS', bottom=peticiones,)
ax.bar(labels, reclamos, width, label='RECLAMOS', bottom=quejas,)
ax.bar(labels, soliciturdes, width, label='SOLICITURDES', bottom=reclamos)

ax.set_ylabel('CASOS')
ax.set_title('CASOS POR TIPO')
ax.legend()

plt.show()
