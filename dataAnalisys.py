import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('ITICB.csv',encoding='utf-8')
#col=[]
#[col.append(i) for i in range(len(df.columns))]
col={df.columns[i]:i for i in range(len(df.columns))}
#col={*col}
print(len(df.columns))
df.rename(columns = col, inplace = True)

print(df.columns)
print(df.shape)
#Read columns and save names in file
"""with open('ColName.txt','w',encoding="UTF-8") as f:
    for inde,i in enumerate (df.columns):
        f.write(str(inde)+','+ str(i)+'\n')
"""
#    print(i)
# index 
index=[6,7,10,11,13,14,15,16,17,21,22,23,25,26,27,28,29,30,31,32,33,34,35,37] 
dataAnalysis =[]
for i in index:
    dataAnalysis.append(df.iloc[:,i])


año=df.iloc[:,7]*1.0 - df.iloc[:,6]*1.0
egreso= np.unique(df.iloc[:,7])
uniqueVal, countYear = np.unique(año, return_counts=True)
print(uniqueVal)

print(egreso)

 
#librerias_python = ['Pandas','Numpy','Plotly','Reuests','matplotlib']
#valores = [37,48,21,35,43]
colores = ['silver','green', 'grey','coral']
#explode_vals = [0,0,0.15,0.15]
plt.pie(x=countYear, labels=uniqueVal, colors = colores, autopct='%1.2f%%', shadow=True)#,xplode = explode_vals)
 
plt.title('Años-Escuela de la Carrera de ITIC') 
plt.show()

#año=df.iloc[:,6:8].copy()

#año.plot(kind = 'bar')
año.plot(kind = 'bar',
             width=0.8,
             subplots=True,
             )
plt.show()
#print('Datas: ',año)
##print(np.shape(dataAnalysis))



