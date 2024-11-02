import nltk
import string
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

from nltk.corpus import stopwords

# Завантажуємо текст
try:
    with open('edgeworth-parents.txt', 'r', encoding='utf-8') as file:
        text = file.read()
except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)

# Функція для підрахунку слів у тексті
def count_words(text):
    sentences = nltk.sent_tokenize(text)  # токенізація по реченням
    k_words = 0
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        k_words += len(words)
    return k_words

# Функція для визначення 10 найбільш вживаних слів
def most_used_words(text, title):
    words = text.split() # Список зі словами
    cnt = Counter(words)
    cort = cnt.most_common(10)
    
    x = [cort[el][0] for el in range(len(cort))]  # слова
    y = [cort[el][1] for el in range(len(cort))]  # к-ть повторень у тексті

    plt.bar(x, y)
    plt.title(title)
    plt.xlabel("Слова")
    plt.ylabel("Зустрічаються разів у тексті")
    plt.show()

# Підрахунок кількості слів у тексті
word_count = count_words(text)
print(f"Кількість слів у тексті: {word_count}")

# Виведення 10 найбільш вживаних слів до очищення тексту
print("10 найбільш вживаних слів до очищення тексту:")
most_used_words(text, "10 найбільш вживаних слів (до очищення)")

# Видалення стоп-слів і пунктуації
def remove_stopwords_punctuation(text):
    words = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words_cleaned = [word for word in words if word.lower() not in stop_words and word not in string.punctuation]
    return ' '.join(words_cleaned)

# Очищений текст
cleaned_text = remove_stopwords_punctuation(text)

# Виведення 10 найбільш вживаних слів після очищення тексту
print("10 найбільш вживаних слів після очищення тексту:")
most_used_words(cleaned_text, "10 найбільш вживаних слів (після очищення)")
