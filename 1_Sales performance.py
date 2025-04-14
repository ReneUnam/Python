import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize

path_file = "./Data/Pen Sales Data Modificado 1er Ejercicio.xlsx"
df_pen_sales = pd.read_excel(path_file, sheet_name='Pen Sales')

#Convierta la fecha de compra a un formato de fecha y hora.
df_pen_sales["Purchase Date"] = pd.to_datetime(df_pen_sales["Purchase Date"]) #Aunque ya estaba
print(df_pen_sales.dtypes)

#Cuenta el número de ventas por mes.
df_purchase_month = df_pen_sales["Purchase Date"].dt.month
df_pen_sales["Month"] = df_purchase_month
df_sales_by_month = df_pen_sales.groupby(["Month"])["Purchase Date"].count()
print(df_sales_by_month)

#Traza un gráfico de líneas de series temporales para visualizar las tendencias de ventas.
df_sales_by_month.plot(kind='line', figsize=(8, 5), marker='o', color='blue', linewidth=2)
plt.xlabel('Month')
plt.ylabel('Number of Sales')
# plt.xticks(rotation=0)
plt.show()