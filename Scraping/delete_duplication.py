import warnings

warnings.filterwarnings(
    'ignore',
    'detected Windows; aliasing chunkize to chunkize_serial',
)
import requests
import numpy as np
import csv
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer
import re
import gensim
from gensim.corpora import Dictionary
import cchardet
import time
from requests_html import HTMLSession
	# 行ごとにすべて読み込んでリストデータにする
	# ファイルをオープンする
read_url = open("text/corpus_name_row.txt", "r",encoding="utf-8")
# 行ごとにすべて読み込んでリストデータにする
lines = csv.reader(read_url)
lis = []
li = []
for x in lines:
	li.extend(x)
lis = list(set(li))
# 一行ずつ表示する
for y in lis:
	f = open('text/corpus_name.txt', 'a',encoding="utf-8")
	f.write(y+'\n')
	f.close()
