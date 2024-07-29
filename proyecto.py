import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Función para crear el gráfico de esperanza de vida por país y año
def plot_life_expectancy(data):
    st.subheader('Esperanza de Vida por País y Año')
    df_life_expectancy = data.groupby(['Country', 'Year'])['Life expectancy '].mean().unstack()
    df_life_expectancy.plot(kind='line', marker='o', figsize=(10, 6))
    plt.title('Esperanza de Vida por País y Año')
    plt.xlabel('Año')
    plt.ylabel('Esperanza de Vida')
    plt.legend(title='Países', bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot()

# Función para crear el gráfico de mortalidad por enfermedad
def plot_mortality_by_disease(data):
    st.subheader('Mortalidad por Enfermedad por Año')
    df_mortality = data.groupby('Year').agg({
        'Adult Mortality': 'mean',
        'infant deaths': 'mean',
        'under-five deaths ': 'mean',
        'HIV/AIDS': 'mean',
        'Measles ': 'mean',
        'Polio': 'mean',
        'Diphtheria ': 'mean',
        'Hepatitis B': 'mean',
        'Alcohol': 'mean',
        'percentage expenditure': 'mean'
    })
    df_mortality.plot(kind='bar', figsize=(12, 7))
    plt.title('Mortalidad por Enfermedad por Año')
    plt.xlabel('Año')
    plt.ylabel('Media de Mortalidad')
    plt.legend(title='Enfermedades', bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot()

# Crear la aplicación Streamlit
def main():
    st.title('Análisis de Datos de Salud Global')

    # Subida de archivo CSV
    uploaded_file = st.file_uploader("Cargar archivo CSV", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        # Mostrar los gráficos
        plot_life_expectancy(data)
        plot_mortality_by_disease(data)
    else:
        st.info("Por favor, sube un archivo CSV para analizar.")

if __name__ == '__main__':
    main()

