import pandas as pd
import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------------------------------------------------
file_path = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(file_path, sheet_name='Pen Sales')
# print(df_pen_sales.dtypes)

#-----------------------------------------------------------------------------------------------------------------------
#Agrupe por artículo y calcule el costo promedio de envío.

df_avg_pen_cost = df_pen_sales.groupby("Item")["Shipping Cost"].mean().sort_values() #.mean() calcula la media aritmetica
# print(df_avg_pen_cost)

#-----------------------------------------------------------------------------------------------------------------------
# Cree un gráfico de barras que compare los costos de envío por tipo

plt.figure(figsize = (15,8))
df_avg_pen_cost.plot(kind = 'barh', color='purple')
plt.title('Average shipping cost per item')
plt.xlabel('Average shipping cost')
plt.ylabel('Pen type')
plt.show()