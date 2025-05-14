import kagglehub
from kagglehub import KaggleDatasetAdapter
import matplotlib.pyplot as plt

# Cargar dataset
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "fabriziocominetti/imdb-data",
    "IMDB-Movie-Data.csv"
)

# Ordenar por rating descendente
top10 = df.sort_values("Rating", ascending=False).head(10)

# Graficar
plt.figure(figsize=(10, 6))
plt.barh(top10["Title"], top10["Rating"], color="skyblue")
plt.xlabel("Rating")
plt.title("Top 10 películas con mejor rating")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("grafica.png")
