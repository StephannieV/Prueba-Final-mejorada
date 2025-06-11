import streamlit as st
import pandas as pd

# URL del CSV (ajusta con tu repositorio real)
url = 'https://raw.githubusercontent.com/tu-usuario/tu-repo/main/datos_mercado.csv'

@st.cache_data
def cargar_datos():
    return pd.read_csv(url)

df = cargar_datos()

st.title("Dashboard del Mercado de Muebles")

# Mostrar bloques disponibles
bloques = df['Bloque'].dropna().unique()
bloque_seleccionado = st.selectbox("Selecciona el bloque de datos", bloques)

df_filtrado = df[df['Bloque'] == bloque_seleccionado]

st.subheader(f"Datos: {bloque_seleccionado}")
st.dataframe(df_filtrado.reset_index(drop=True))

# Mostrar solo columnas con datos relevantes
columnas_numericas = [
    'Valor_2024_USD_mil_millones',
    'Valor_2025_USD_mil_millones',
    'Valor_2030_USD_mil_millones',
    'Valor_2032_USD_mil_millones',
    'Valor_2033_USD_mil_millones',
    'CAGR_%',
    'CAGR_2024_2029_%',
    'CAGR_2025_2030_%',
    'Crecimiento_%',
    'Proyección_2029_USD_mil_millones',
    'Tamaño_mercado_global_tropical_USD_mil_millones',
    'Proyección_muebles_lujo_USD_millones',
    'Valor_2025_USD_millones',
]

df_numerico = df_filtrado[['Categoria'] + columnas_numericas].dropna(how='all', axis=1)
st.subheader("Valores Numéricos")
st.dataframe(df_numerico.reset_index(drop=True))

# Comentarios si existen
comentarios = df_filtrado['Comentario'].dropna()
if not comentarios.empty:
    st.subheader("Comentarios")
    for c in comentarios:
        st.write(f"• {c}")


