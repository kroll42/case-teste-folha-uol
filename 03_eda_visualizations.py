import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud

def generate_eda_plots(df: pd.DataFrame, output_dir: str = 'plots/'):
    """Gera visualizações para a apresentação"""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Distribuição de categorias (gráfico de barras horizontal)
    fig1 = px.bar(
        df['category_grouped'].value_counts().head(10).reset_index(),
        x='count', y='category_grouped', orientation='h',
        title='📰 Top 10 Categorias de Notícias',
        labels={'category_grouped': 'Categoria', 'count': 'Quantidade'},
        color='count', color_continuous_scale='Blues'
    )
    fig1.write_html(f'{output_dir}top_categories.html')
    fig1.write_image(f'{output_dir}top_categories.png', width=1000, height=600)
    
    # 2. Evolução temporal de publicações
    df_monthly = df.groupby([df['date'].dt.to_period('M')]).size().reset_index(name='count')
    df_monthly['date'] = df_monthly['date'].dt.to_timestamp()
    
    fig2 = px.line(
        df_monthly, x='date', y='count',
        title='📈 Volume de Notícias ao Longo do Tempo (2015-2017)',
        labels={'date': 'Data', 'count': 'Número de Notícias'}
    )
    fig2.update_traces(line=dict(width=3))
    fig2.write_html(f'{output_dir}time_series.html')
    
    # 3. Heatmap: Categoria x Dia da Semana
    heatmap_data = pd.crosstab(df['day_of_week'], df['category_grouped'])
    fig3 = px.imshow(
        heatmap_data, text_auto=True, aspect="auto",
        title='🗓️ Distribuição de Categorias por Dia da Semana',
        color_continuous_scale='Viridis'
    )
    fig3.write_html(f'{output_dir}heatmap_day_category.html')
    
    # 4. WordCloud por categoria principal
    for cat in df['category_grouped'].value_counts().head(3).index:
        text_cat = ' '.join(df[df['category_grouped'] == cat]['text_clean'].dropna())
        if len(text_cat) > 100:
            wc = WordCloud(width=800, height=400, background_color='white', 
                          colormap='Set2', max_words=100).generate(text_cat)
            plt.figure(figsize=(12, 6))
            plt.imshow(wc, interpolation='bilinear')
            plt.axis('off')
            plt.title(f'☁️ WordCloud - {cat.title()}', fontsize=16, fontweight='bold')
            plt.tight_layout()
            plt.savefig(f'{output_dir}wordcloud_{cat}.png', dpi=300, bbox_inches='tight')
            plt.close()
    
    # 5. Boxplot: Tamanho do texto por categoria
    fig5 = px.box(
        df, x='category_grouped', y='text_length',
        title='📏 Tamanho Médio dos Textos por Categoria',
        labels={'category_grouped': 'Categoria', 'text_length': 'Caracteres'},
        color='category_grouped'
    )
    fig5.update_layout(xaxis_tickangle=-45, showlegend=False)
    fig5.write_html(f'{output_dir}text_length_by_category.html')
    
    print(f"✅ {len(os.listdir(output_dir))} visualizações geradas em '{output_dir}'")

# Execução
if __name__ == "__main__":
    df = pd.read_csv('articles_processed.csv', encoding='utf-8')
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    generate_eda_plots(df)