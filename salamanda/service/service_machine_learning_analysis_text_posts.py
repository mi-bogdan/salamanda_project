import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist

from accounts.models import Profile
from django.contrib.auth.models import User


def add_analysis_text_posts(title_post: str, keyword_old: list) -> str:
    """Машинное обучение определяет ключевые слова для выявления похожих постов в дальнейшем"""

    # загрузка стоп-слов из NLTK
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')

    # инициализация лемматизатора для дальнейшей обработки текста
    lemmatizer = WordNetLemmatizer()

    # токенизация текста и удаление стоп-слов
    # lower - приводим к нижнему регистру
    tokens = word_tokenize(title_post.lower())
    stop_words = set(stopwords.words('english'))
    clean_tokens = [token for token in tokens if token not in stop_words]

    # лемматизация токенов для уменьшения количества уникальных слов
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in clean_tokens]

    # определение наиболее частых слов и создание списка ключевых слов
    fdist = FreqDist(lemmatized_tokens)
    keywords_new = [word for word, count in fdist.most_common(3)]

    extend_array = set(keyword_old + keywords_new)
    string = ','.join(extend_array)

    return string
