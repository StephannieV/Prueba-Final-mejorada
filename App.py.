import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# URL del archivo CSV en GitHub en formato "raw"
url = 'https://raw.githubusercontent.com/tu-usuario/streamlit-dashboard/main/data/datos_mercado.csv'

@st.cache_data
def load_data():
    df = pd.read_csv(url)
    return df

df = load_data()

st.title("Dashboard del Mercado de Muebles")

# Mostrar tabla completa
st.subheader("Datos Crudos")
st.dataframe(df)

# Filtrar por categoría
categorias = df['Categoria'].dropna().unique()
categoria_seleccionada = st.selectbox("Selecciona una categoría", categorias)

df_filtrado = df[df['Categoria'] == categoria_seleccionada]

st.subheader(f"Subcategorías en {categoria_seleccionada}")
st.dataframe(df_filtrado[['Subcategoria', 'Valor_2025_USD_mil_millones', 'Valor_2030_USD_mil_millones', 'CAGR_%', 'Comentario']])

# Visualización de crecimiento si hay datos
st.subheader("Visualización de crecimiento (si aplica)")

cols_valor = ['Valor_2025_USD_mil_millones', 'Valor_2030_USD_mil_millones', 'Valor_2032_USD_mil_millones', 'Valor_2033_USD_mil_millones']
df_plot = df_filtrado.dropna(subset=cols_valor, how='all')

if not df_plot.empty:
    for _, row in df_plot.iterrows():
        subcat = row['Subcategoria']
        valores = [row.get(col, None) for col in cols_valor]
        años = [int(col.split('_')[1]) for col in cols_valor if pd.notna(row.get(col))]
        valores_limpios = [v for v in valores if pd.notna(v)]

        if valores_limpios:
            plt.plot(años[:len(valores_limpios)], valores_limpios, marker='o', label=subcat)

    plt.title("Evolución de Subcategorías")
    plt.xlabel("Año")
    plt.ylabel("Valor (USD mil millones)")
    plt.legend()
    st.pyplot(plt)
else:
    st.write("No hay suficientes datos para visualizar el crecimiento.")


