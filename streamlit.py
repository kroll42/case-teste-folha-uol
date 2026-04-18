import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Folha/UOL", layout="wide")
st.title("📊 Análise Editorial Folha/UOL (2015-2017)")

@st.cache_data
def load_data():
    df = pd.read_csv('articles_processed.csv', encoding='utf-8')
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

# Filtros
categorias = st.multiselect("Selecione categorias:", df['category_grouped'].unique(), default=['poder', 'mercado', 'ilustrada'])
data_min = df['date'].min().date()
data_max = df['date'].max().date()
data_range = st.date_input("Período:", [data_min, data_max])

# Filtrar dados
mask = (df['category_grouped'].isin(categorias)) & (df['date'].dt.date >= data_range[0]) & (df['date'].dt.date <= data_range[1])
df_filtered = df[mask]

# Gráfico temporal
ts = df_filtered.groupby(df_filtered['date'].dt.to_period('M')).size().reset_index(name='count')
ts['date'] = ts['date'].dt.to_timestamp()
fig1 = px.line(ts, x='date', y='count', title='Volume de Notícias por Mês')
st.plotly_chart(fig1, use_container_width=True)

# Distribuição de categorias
fig2 = px.bar(df_filtered['category_grouped'].value_counts().reset_index(), 
              x='count', y='category_grouped', orientation='h', 
              title='Quantidade por Categoria', color='count')
st.plotly_chart(fig2, use_container_width=True)

# Tabela de amostra
st.subheader("Amostra das Notícias")
st.dataframe(df_filtered[['title', 'date', 'category_grouped']].head(20))