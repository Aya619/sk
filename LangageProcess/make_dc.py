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
# ファイルをオープンする
f = open("text/text_all_g2.txt", "r",encoding='utf-8')
dc = []
# 行ごとにすべて読み込んでリストデータにする
reader = csv.reader(f)
csv.field_size_limit(1000000000)
lis = []
t = Tokenizer()
stwd =['「','」',',','"','【','】','年月日','点','年','月','日','ツイート','リンク','コピー','サイト','埋め込む','インスタグラム','フォロー','アカウント','リツイート','スレッド','Twitter','twitter','返信','件','コメント','投稿','更新','|','(',')','レビュー','()','[',']','円']
# 一行ずつ表示する
#"[]","[]"
for row in reader:
	dc = []
#		result = bs.find_all('td',  attrs={})
	if row == []:
		pass
	else:
	#	if po.search(row[3]):

		for token in t.tokenize(row[1]):
			if token.surface not in stwd:
				dc.append(token.surface)
		f2 = open("text/dc.txt", "a",encoding='utf-8')
		writer = csv.writer(f2)
		writer.writerow([row[0],dc])
		f2.close()

#				if token.part_of_speech.split(',')[0] == '名詞':
#					bow_l.append(token.surface)
#				elif token.part_of_speech.split(',')[0] == '形容詞':
#					bow_l.append(token.surface)
#				elif token.part_of_speech.split(',')[0] == '動詞':
#					bow_l.append(token.surface)
