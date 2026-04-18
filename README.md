
---

## 🚀 Principais Entregáveis

### 🔍 Exploratory Data Analysis (EDA)
- Distribuição temporal de publicações (sazonalidade)
- Heatmap: categorias × dia da semana
- WordClouds com stop words personalizadas para jornalismo PT-BR
- Boxplots: tamanho de texto por categoria

### 🧠 Análise de Sentimento
- **Modelo 1**: `leia-br` (VADER adaptado para português)
- **Modelo 2**: `manushya-ai/SYAS1-PTBR` (BERT fine-tuned)
- Comparação via Índice Kappa de Cohen
- Teste de hipótese (Mann-Whitney U) entre categorias

### 📊 Modelagem Preditiva
- Classificação de subcategorias com **TF-IDF + Logistic Regression**
- Acurácia: ~68.6% (baseline para produção)
- Matriz de confusão das 10 classes mais frequentes

### 📖 Métricas de Legibilidade
- Índice Flesch Reading Ease (adaptado para PT-BR)
- Densidade lexical por categoria
- Insights sobre complexidade textual

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Ferramentas |
|-----------|------------|
| **Linguagem** | Python 3.12 |
| **Análise de Dados** | pandas, numpy |
| **Visualização** | matplotlib, seaborn, plotly, wordcloud |
| **NLP** | nltk, textstat, leia-br, transformers |
| **Modelagem** | scikit-learn (TF-IDF, LogisticRegression) |
| **Estatística** | scipy.stats (teste de hipótese) |
| **Ambiente** | Jupyter Notebook, venv |

---

## 📦 Instalação e Execução

```bash
# 1. Clone o repositório
git clone <seu-repositorio>
cd case_teste_2

# 2. Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute o notebook principal
jupyter notebook all.ipynb
