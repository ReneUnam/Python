import pandas as pd
import matplotlib.pyplot as plt

# Calcular tiempo de entrega = Fecha de entrega - Fecha de compra.
path_file = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(path_file, sheet_name='Pen Sales')
delivery_date = df_pen_sales['Delivery Date']
purchase_time = df_pen_sales['Purchase Date']
# print(delivery_time)
# print(purchase_time)

delivery_time = (df_pen_sales['Delivery Date']-df_pen_sales['Purchase Date']).dt.days
# print(delivery_time)

df_pen_sales['Delivery Time'] = delivery_time
# print(df_pen_sales.dtypes)

# Agrupe por artículo y encuentre el tiempo medio de entrega.
average_delivery_time = df_pen_sales.groupby('Item')['Delivery Time'].mean().sort_values()
print(average_delivery_time)

# Traza un gráfico de barras para comparar los tiempos de entrega.
average_delivery_time.plot(kind='bar', figsize=(15,10), color="orange")
plt.title('Average Delivery Time')
plt.xlabel('Product')
plt.ylabel('Average Delivery Time')
plt.xticks(rotation=45,ha='right')
plt.grid(axis ='x', linestyle = '--', alpha = 0.9)
plt.grid(axis ='y', linestyle = '--', alpha = 0.9)
plt.show()