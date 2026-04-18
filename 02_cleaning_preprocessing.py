import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download de recursos NLTK (executar uma vez)
# nltk.download('punkt')
# nltk.download('stopwords')

def clean_text(text: str) -> str:
    """Limpeza básica para análise de texto"""
    if pd.isna(text):
        return ""
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+|@\w+|#\w+', '', text)  # Remove URLs, menções
    text = re.sub(r'[^a-zà-ú\s]', '', text)  # Mantém apenas letras e acentos
    text = re.sub(r'\s+', ' ', text).strip()  # Remove espaços extras
    return text

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """Cria features derivadas para análise"""
    df = df.copy()
    
    # Features temporais
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day_of_week'] = df['date'].dt.day_name()
    df['is_weekend'] = df['day_of_week'].isin(['Saturday', 'Sunday'])
    
    # Features de texto
    df['text_clean'] = df['text'].apply(clean_text)
    df['title_length'] = df['title'].str.len()
    df['text_length'] = df['text'].str.len()
    df['word_count'] = df['text_clean'].apply(lambda x: len(x.split()))
    
    # Feature de categoria (agrupar categorias raras)
    category_counts = df['category'].value_counts()
    rare_categories = category_counts[category_counts < 1000].index
    df['category_grouped'] = df['category'].apply(
        lambda x: 'outros' if x in rare_categories else x
    )
    
    return df

# Execução
if __name__ == "__main__":
    df = pd.read_csv('articles.csv', encoding='utf-8')
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    df_processed = create_features(df)
    
    print("✅ Features criadas:")
    print(df_processed[['title_length', 'text_length', 'word_count', 
                       'year', 'month', 'category_grouped']].head())
    
    # Salvar para próxima etapa
    df_processed.to_csv('articles_processed.csv', index=False, encoding='utf-8')
    print("💾 Dataset processado salvo!")