import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from google.colab import drive

# Montar Google Drive
drive.mount('/content/drive')

# Ruta al archivo CSV en tu Google Drive
csv_file_path = '/content/drive/MyDrive/PROYECTO_PROGRAMACION/PROYECTO_ORDINARIO.csv'

# Leer el archivo CSV usando pandas
data = pd.read_csv(csv_file_path)

# Mostrar los nombres de las columnas
print(data.columns)

# Crear una conexión a la base de datos SQLite (o crearla si no existe)
db_conn = sqlite3.connect('/content/drive/MyDrive/PROYECTO_PROGRAMACION/PROYECTO_ORDINARIO.db')

# Guardar los datos en una tabla en la base de datos SQLite
data.to_sql('Levantamiento', db_conn, if_exists='replace', index=False)

# Cerrar la conexión a la base de datos
db_conn.close()

# Volver a abrir la conexión para realizar consultas y graficar
db_conn = sqlite3.connect('/content/drive/MyDrive/PROYECTO_PROGRAMACION/PROYECTO_ORDINARIO.db')

# Consulta SQL para obtener los datos de la tabla
query = "SELECT `Y`, `X`, `Z` FROM levantamiento"

# Obtener los datos de la tabla en un DataFrame
result = pd.read_sql(query, db_conn)

# Cerrar la conexión a la base de datos
db_conn.close()

# Graficar los datos con mejoras
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Añadir color y tamaño a los puntos
scatter = ax.scatter(result['Y'], result['X'], result['Z'], c=result['Z'], cmap='viridis', s=50)

# Añadir una barra de color
cbar = plt.colorbar(scatter)
cbar.set_label('Valor Z')

# Rotar las etiquetas de los ejes para mejorar la legibilidad
ax.set_xlabel('Y')
ax.set_ylabel('X')
ax.set_zlabel('Z')
ax.xaxis.labelpad = 15
ax.yaxis.labelpad = 15
ax.zaxis.labelpad = 15

# Añadir una leyenda si es necesario
# Por ejemplo, si hay diferentes categorías que representan los colores
# ax.legend(['Categoría 1', 'Categoría 2'])


plt.title('Levantamineto Topografico')
plt.show()
