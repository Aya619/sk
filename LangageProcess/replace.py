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
read_url = open("text/ct.txt", "r",encoding="utf-8")
# 行ごとにすべて読み込んでリストデータにする
lis = read_url.read()
# 一行ずつ表示する 
f = open('text/ct.txt', 'w',encoding="utf-8")
f.write(lis.replace("'",''))
f.close()
