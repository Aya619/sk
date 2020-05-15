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
import subprocess
import math
try:
	# 行ごとにすべて読み込んでリストデータにする
	lis = []
	bow_id = []
	bow_l =[]
	BOW =[]
	# 一行ずつ表示する
	wo = ['a','i','u','e','o','ka','ki','ku','ke','ko','sa','si','su','se','so','ta','ti','tu','te','to','na','ni','nu','ne','no','ha','hi','hu','he','ho','ma','mi','mu','me','mo','ya','yu','yo','ra','ri','ru','re','ro','wa']
	for w in wo:
		url = "https://sakuhindb.com/anime/j_game_"+w+".html"
		response = requests.get(url)
		stop_noodle = [',','年月日','点','年','月','日','ツイート','リンク','コピー','サイト','埋め込む','インスタグラム','フォロー','アカウント','リツイート','スレッド','Twitter','twitter','返信','件','コメント','投稿','更新','|','(',')','レビュー','()','[',']','円','\u202c\u202a','人','こと','こと']
		if response.status_code == requests.codes.ok:
			response.encoding = cchardet.detect(response.content)["encoding"]
			bs = BeautifulSoup(response.text, 'html.parser')
			result = []
			texts = []
			bow = []
			bow_l = []
			regex = u'[一-龥ぁ-んァ-ン]'
			row = []
			t = Tokenizer()
	#		result = bs.find_all('td',  attrs={})
			for res in bs.find('div',  attrs={'class': 'article container'}).find_all('a'):
				result.append(res.attrs['href'])
	#		for x in result:
	#			texts.append(x.replace('\n',''))

			f = open('urls/url_g.txt', 'a',encoding=response.encoding)
			writer = csv.writer(f)
			writer.writerow(result)
			f.close()
			print(w)
		else:
			print(response.status_code)

	#	dct = Dictionary(bow_l)
	#	bow_id = dct.token2id

	#	for text in bow_l:
	#		BOW.append(dct.doc2bow(text))
	#	f = open('bow_id.csv', 'w')

	#	writer = csv.writer(f)
	#	writer.writerow(bow_id)
	#	f.close()

	#	f = open('BOW.csv', 'w')
	#	writer = csv.writer(f)
	#	writer.writerow(BOW)
	#	f.close()
except UnicodeEncodeError:
	pass