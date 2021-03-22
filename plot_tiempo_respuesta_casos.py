import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("https://raw.githubusercontent.com/alexandersolis/poligran_mineria_de_datos_2/main/Datos_PQRS.csv")

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)


    
    
df['PLAZO'] = 0
for index, row in df.iterrows():
    if row['DIAS'] <= 15:
        df.at[index, 'PLAZO'] = 15
    elif row['DIAS'] <= 20:
        df.at[index, 'PLAZO'] = 20
    elif row['DIAS'] <= 30:
        df.at[index, 'PLAZO'] = 30
    else:
        df.at[index, 'PLAZO'] = 60



df_plazo = df.loc[df['ESTADO'] == 'CERRADO']
#print(' ')
#print(df_plazo)

df_estado_caso = pd.DataFrame(columns=['PLAZO', 'CASOS'])
i=0
for label, value in df_plazo.groupby('PLAZO').size().iteritems():
    df_estado_caso.loc[i] = str(label) + ' DIAS' , value
    #print(label, value)
    i += 1
print(' ')
print(df_estado_caso)
print(' ')

#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
#ax1.pie(df_estado_caso['CASOS'], explode=explode, labels=df_estado_caso['PLAZO'], shadow=True, startangle=90)
#wedges, autotexts = ax1.pie(df_estado_caso['CASOS'], explode=explode, labels=df_estado_caso['PLAZO'])
#wedges, autotexts = ax1.pie(df_estado_caso['CASOS'], autopct=lambda pct: func(pct, df_estado_caso['PLAZO']), labels=df_estado_caso['PLAZO'])
wedges, autotexts = ax1.pie(df_estado_caso['CASOS'], labels=df_estado_caso['PLAZO'])
ax1.axis('equal')

ax1.legend(wedges, df_estado_caso['PLAZO'],
          title="PLAZO",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

#ax1.set_title("Matplotlib bakery: A pie")

plt.show()