import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Configuración de Streamlit
st.title('Análisis de Datos de Salud y Economía')

# Cargar el archivo CSV usando el cargador de archivos de Streamlit
archivo_csv = st.file_uploader("Sube tu archivo CSV", type="csv")

if archivo_csv:
    try:
        # Cargar los datos
        data = pd.read_csv(archivo_csv)

        # Mostrar las primeras filas del dataset
        st.write(data.head())

        # Seleccionar un país
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

    except pd.errors.EmptyDataError:
        st.error("El archivo está vacío. Por favor, verifique el contenido del archivo.")
    except Exception as e:
        st.error(f"Ocurrió un error al procesar el archivo: {e}")
else:
    st.info("Por favor, sube un archivo CSV para comenzar.")
