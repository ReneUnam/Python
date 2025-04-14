import pandas as pd
import matplotlib.pyplot as plt

path_file = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(path_file, sheet_name='Pen Sales')

review = "Doddle with me|I love it"
print(review.split("|")[1].split(" "))

# Divida la columna Revisar para separar el nombre del revisor y el comentario.


#Realizar un análisis básico de sentimientos (contar las apariciones de palabras positivas como amor, genial, bueno frente a palabras negativas como malo, disgusto).
review = df_pen_sales["Review"]
positive_words =["I love it", "I like it", "Love", "good", "excellent", "best"]
positive_count = review.str.contains("|".join(positive_words), case=False, na=False).sum()
print(positive_count)