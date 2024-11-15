# -*- coding: utf-8 -*-
"""Lab1_EO.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TU1mDqAzk1p_yllS-f0RF-RZphlJq5Bu
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
import pymorphy2
nltk.download('punkt')

# Инициализация морфологического анализатора
morph = pymorphy2.MorphAnalyzer()

# Функция для проверки, является ли слово существительным или прилагательным
def is_noun_or_adj(tag):
    return 'NOUN' in tag or 'ADJF' in tag or 'ADJS' in tag

# Функция для проверки, совпадают ли тэги по роду, числу и падежу
def check_gender_number_case(tag1, tag2):
    return tag1.gender == tag2.gender and tag1.number == tag2.number and tag1.case == tag2.case

# Чтение текста из файла
with open('/content/text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Сегментация текста
segments = sent_tokenize(text)

# Проход по каждому сегменту
for segment in segments:
    # Токенизация сегментов
    tokens = word_tokenize(segment)
    print(tokens)

    # Перебор всех пар соседних слов в пределах сегмента
    for i in range(len(tokens) - 1):
        tok1 = tokens[i]
        tok2 = tokens[i+1]

        # Морфологический разбор слов
        morph_tok1 = morph.parse(tok1)[0]
        morph_tok2 = morph.parse(tok2)[0]

        # Проверяем, являются ли слова существительными или прилагательными
        if is_noun_or_adj(morph_tok1.tag) and is_noun_or_adj(morph_tok2.tag):
            # Проверяем совпадение по роду, числу и падежу
            if check_gender_number_case(morph_tok1.tag, morph_tok2.tag):
                # Выводим леммы слов
                print(f'{morph_tok1.normal_form} {morph_tok2.normal_form}')