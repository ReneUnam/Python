import pandas as pd
import matplotlib.pyplot as plt

path_file = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(path_file, sheet_name='Pen Sales')

# review = "Doddle with me|I love it"
# print(review.split("|")[1].split(" "))
reviews = df_pen_sales["Review"]

# Divida la columna Revisar para separar el nombre del revisor y el comentario.
df_pen_sales["Review Text"]= reviews.str.split("|").str[1]

#Realizar un análisis básico de sentimientos (contar las apariciones de palabras positivas como amor, genial, bueno frente a palabras negativas como malo, disgusto).
positive_words =["love", "great", "good", "amazing" "excellent", "best"]
negative_words = ["bad", "poor", "dislike", "terrible", "worst", "disappointed", "unfortunately"]

# positive_count = df_pen_sales["Review Text"].str.contains("|".join(positive_words), case=False, na=False).sum()
# print(positive_count)
# negative_count = df_pen_sales["Review Text"].str.contains("|".join(negative_words), case=False, na=False).sum()
# print(negative_count)

positive_review_count = reviews.str.contains("|".join(positive_words), case=False, na=False).sum()
# for review in reviews:
#     for positive_word in positive_words:
#         if positive_word.lower() in review.lower():
#             positive_review_count += 1
#             break
print(f"Canditad de reviews postivos {positive_review_count}")

# negative_review_count = reviews.str.contains("|".join(positive_words), case=False, na=False).sum()
negative_review_count = 0
for review in reviews:
    for negative_word in negative_words:
        if negative_word.lower() in review.lower():
            negative_review_count += 1
print(f"Cantidad de reviews negativos {negative_review_count}")

# Genere una nube de palabras o un gráfico circular de sentimientos.
plt.pie([positive_review_count, negative_review_count],
        labels=["Positive reviews", "Negative reviews"],
        autopct="%1.1f%%", colors=["blue", "red"],
        startangle=140)
plt.title("Sentiment reviews analysis")
plt.show()