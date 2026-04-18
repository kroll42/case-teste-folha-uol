import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Configurações de estilo para apresentação
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

def load_and_explore(filepath: str) -> pd.DataFrame:
    """
    Carrega o dataset e retorna informações essenciais para o case.
    """
    print("🔍 Carregando dataset...")
    df = pd.read_csv(filepath, encoding='utf-8')
    
    print(f"\n📦 Shape: {df.shape}")
    print(f"\n📋 Colunas: {list(df.columns)}")
    print(f"\n🔎 Tipos de dados:\n{df.dtypes}")
    print(f"\n❌ Missing values:\n{df.isnull().sum()}")
    print(f"\n📊 Primeiras linhas:\n{df.head(3).to_string()}")
    
    return df

# Execução
if __name__ == "__main__":
    df = load_and_explore('articles.csv')
    
    # Conversão de data
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    # Métricas rápidas para storytelling
    print(f"\n📈 Período: {df['date'].min().date()} a {df['date'].max().date()}")
    print(f"📰 Total de notícias: {len(df):,}")
    print(f"🏷️  Categorias únicas: {df['category'].nunique()}")
    print(f"📝 Tamanho médio do texto: {df['text'].str.len().mean():.0f} caracteres")