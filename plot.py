import matplotlib.pyplot as plt

productos = ['A', 'B', 'C']
ventas = [100, 150, 80]

plt.bar(productos, ventas)
plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Ventas")
plt.savefig("grafica.png")
