import re # Biblioteca para expressões regulares
import nltk # Natural Language Toolkit (processamento de linguagem)
from nltk.corpus import stopwords # Palavras comuns que queremos ignorar

# Isso você roda uma vez no ambiente local ou garante que está no startup da API
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


def text_clear(text):
    text = text.lower() # Coloca tudo em letras minúsculas
    text = re.sub(r'\n',' ', text) # Substitui as quebras de linha (\n) por espaço
    text = re.sub(r'[^\w\s]', '', text) # Remove pontuação e caracteres especiais (\w representa letras/números e _; \s representa espaços.)
    tokens = text.split() # Quebra o texto em palavras (tokens), Exemplo: ["python", "é", "legal"]
    tokens = [t for t in tokens if t not in stopwords.words('portuguese')] # Remove stopwords
    return ' '.join(tokens) # Junta as palavras de volta em uma string limpa
