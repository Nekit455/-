# -*- coding: utf-8 -*-
"""Lab2 ЕЯ.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c3o_egxnRJiP_uvvCTrpMwjQgCgfBCcM
"""

import requests
response = requests.get("https://marigostra.ru/persist/cbow.txt")

import gensim
import re
import tempfile

with tempfile.NamedTemporaryFile(delete=False) as temp_file:
  temp_file.write(response.content)
  temp_file_path = temp_file.name

# Загрузка модели
word2vec = gensim.models.KeyedVectors.load_word2vec_format(temp_file_path, binary=False)

# Задаем слова для комбинации
pos = ["спорщик_NOUN", "оппонент_NOUN"]
neg = ["враг_NOUN"]

# Вычисляем ближайшие по смыслу слова (цель: собеседник, полемист)
dist = word2vec.most_similar(positive=pos, negative=neg)

for i in dist:
  print(i)

# Отбираем существительные
pat = re.compile("(.*)_NOUN")

for i in dist:
    e = pat.match(i[0])
    if e is not None:
        print(e.group(1))  # Печатаем только лемму

