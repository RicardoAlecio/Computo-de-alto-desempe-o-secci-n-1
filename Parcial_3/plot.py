import matplotlib.pyplot as plt
from elasticsearch import Elasticsearch

# Conexión
es = Elasticsearch("http://localhost:9200")

# Buscar los documentos
res = es.search(index="productos", query={"match_all": {}}, size=1000)

# Extraer datos
nombres = []
ventas = []

for doc in res["hits"]["hits"]:
    source = doc["_source"]
    nombres.append(source["name"])
    ventas.append(source["ventas"])

# Graficar
plt.bar(nombres, ventas)
plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Ventas")
plt.savefig("grafica.png")


