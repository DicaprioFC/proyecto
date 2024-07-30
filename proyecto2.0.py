import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gdown
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Configuración de Streamlit
st.title('Análisis de Datos de Salud y Economía')

# URL del archivo en Google Drive
url = 'https://drive.google.com/uc?id=1-97H6wZkvQPC7iBnfzoNFGOO-jfpxC5O'
output = 'datos_salud_economia.csv'

# Descargar archivo
gdown.download(url, output, quiet=False)

# Cargar los datos
data = pd.read_csv(output)

# Mostrar las primeras filas del dataset
st.write(data.head())

# Función para graficar y mostrar gráficos en Streamlit
def plot_and_show(data, x, y, title, xlabel, ylabel, plot_type='line', color='blue'):
    plt.figure(figsize=(10, 6))
    if plot_type == 'line':
        sns.lineplot(x=x, y=y, data=data, color=color)
    elif plot_type == 'bar':
        sns.barplot(x=x, y=y, data=data, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    st.pyplot(plt.gcf())
    plt.close()

# Visualización de datos generales
plot_and_show(data, 'Year', 'Life expectancy ', 'Expectativa de Vida a lo largo de los Años', 'Año', 'Expectativa de Vida', 'line', 'teal')
plot_and_show(data, 'Year', 'Adult Mortality', 'Mortalidad Adulta a lo largo de los Años', 'Año', 'Mortalidad Adulta', 'bar', 'coral')
plot_and_show(data, 'Year', 'infant deaths', 'Muertes Infantiles a lo largo de los Años', 'Año', 'Muertes Infantiles', 'line', 'green')
plot_and_show(data, 'Year', 'Alcohol', 'Consumo de Alcohol a lo largo de los Años', 'Año', 'Consumo de Alcohol', 'bar', 'orange')
plot_and_show(data, 'Year', 'GDP', 'PIB a lo largo de los Años', 'Año', 'PIB', 'line', 'purple')
plot_and_show(data, 'Year', 'Schooling', 'Escolaridad a lo largo de los Años', 'Año', 'Escolaridad', 'bar', 'blue')

# Seleccionar un país para el análisis de regresión lineal
paises = data['Country'].unique()
pais_seleccionado = st.selectbox("Selecciona un país", paises)

# Filtrar datos para el país seleccionado
data_pais = data[data['Country'] == pais_seleccionado]

if not data_pais.empty:
    # Realizar la regresión lineal
    X = data_pais[['Year']].values
    y = data_pais['Life expectancy '].values

    # Ajustar modelo de regresión lineal
    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)
    r2 = r2_score(y, predictions)

    # Graficar la regresión lineal
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Year', y='Life expectancy ', data=data_pais, color='blue')
    sns.lineplot(x=data_pais['Year'], y=predictions, color='red')
    plt.title(f'Regresión Lineal: Expectativa de Vida en {pais_seleccionado}')
    plt.xlabel('Año')
    plt.ylabel('Expectativa de Vida')
    plt.grid(True)
    st.pyplot(plt.gcf())
    plt.close()

    # Mostrar el valor de R²
    st.write(f'Precisión de la regresión lineal (R²) para {pais_seleccionado}: {r2:.2f}')
else:
    st.warning("No hay suficientes datos para realizar la regresión lineal.")
