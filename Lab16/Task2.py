import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# Завантажуємо необхідні компоненти NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')  # Для лемматизатора, щоб підтримувати різні форми слів

# Читаємо текст із файлу
try:
    with open('sample-text.txt', 'r', encoding='utf-8') as file:
        text = file.read()
except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)

# Токенізація по словам
tokens = word_tokenize(text)

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Видалення пунктуації та стоп-слів
stop_words = set(stopwords.words('english'))
cleaned_tokens = [word for word in tokens if word.lower() not in stop_words and word not in string.punctuation]

# Лемматизація та стеммінг очищених слів
lemmatized_words = [lemmatizer.lemmatize(word) for word in cleaned_tokens]
stemmed_words = [stemmer.stem(word) for word in lemmatized_words]

# Запис обробленого тексту у інший файл
with open('processed-text.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(' '.join(stemmed_words))

print("Оброблений текст збережено у 'processed-text.txt'")
