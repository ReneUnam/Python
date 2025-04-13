import pandas as pd
import matplotlib.pyplot as plt

path_file = "./Data/Pen Sales Data.xlsx"
df_pen_ranking = pd.read_excel(path_file, sheet_name='Pen Sales')
print(df_pen_ranking.head())

#Cuente el número de compras por artículo.
#Ordenar en orden descendente.
df_pen_ranking_count = df_pen_ranking["Item"].value_counts().sort_values(ascending=False)
print(df_pen_ranking_count)

#Traza un gráfico de barras horizontales para mayor claridad.
plt.figure(figsize = (15,8))
df_pen_ranking_count.plot(kind = 'barh', color = 'g')
plt.title('Pen popularity ranking')
plt.xlabel('Number of sales')
plt.ylabel('Pen type')
plt.grid(axis ='x', linestyle = '--', alpha = 0.7)
plt.gca().invert_yaxis()
plt.show()