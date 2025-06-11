import streamlit as st
import pandas as pd

# URL del archivo CSV en formato raw de GitHub (ajusta esta URL a tu repositorio)
url = 'https://raw.githubusercontent.com/tu-usuario/streamlit-dashboard/main/data/datos_mercado.csv'

@st.cache_data
def load_data():
    df = pd.read_csv(url)
    return df

df = load_data()

st.title("Dashboard del Mercado de Muebles")

# Mostrar tabla completa
st.subheader("Datos Completos")
st.dataframe(df)

# Filtro por categoría
categorias = df['Categoria'].dropna().unique()
categoria_seleccionada = st.selectbox("Filtrar por categoría", categorias)

df_filtrado = df[df['Categoria'] == categoria_seleccionada]

st.subheader(f"Subcategorías en {categoria_seleccionada}")
st.dataframe(df_filtrado[['Subcategoria', 
                          'Valor_2024_USD_mil_millones', 
                          'Valor_2025_USD_mil_millones', 
                          'Valor_2030_USD_mil_millones', 
                          'Valor_2032_USD_mil_millones', 
                          'Valor_2033_USD_mil_millones', 
                          'CAGR_%', 
                          'CAGR_2024_2029_%', 
                          'Proyección_2029_USD_mil_millones', 
                          'Comentario']])


