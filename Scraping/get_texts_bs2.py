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
	read_url = open("urls/url_g.txt", "r",encoding="utf-8")
	# 行ごとにすべて読み込んでリストデータにする
	lines = read_url.readlines()
	lis = []
	num = 0
	n = num
	nu = re.compile(r'(\d+)件中')
	ti = re.compile(r'jp\/(.+)\/product-reviews\/')
	# 一行ずつ表示する
	for urls in lines[0].split(',')[num:]:

#		for i in range(1,100):
		for i in range(1,100):
			url = "https://sakuhindb.com"+urls+str(i)+".html#sort_review"
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
				if bs.find('td',  attrs={'class': 'padding_cell'}).find_all('div',  attrs={'class': 'inline'}) == []:
					break
#				print(bs.find('span',  attrs={'itemprop': 'name'}).text)
		#		result = bs.find_all('td',  attrs={})
		#		print(response.html.find('tr td.center'))
				for res in bs.find('td',  attrs={'class': 'padding_cell'}).find_all('div',  attrs={'class': 'inline', 'itemprop': 'review'}):
					if res.find('span',  attrs={'class': 'no_sex'}):
#						result.append([bs.find('span',  attrs={'itemprop': 'name'}).text,res.find('span',  attrs={'class': 'no_sex'}).text,res.find('b').find('span'),res.find('div',  attrs={'class': 'inline', 'itemprop': 'reviewBody'})])
						f = open('text/text_all_g2.txt', 'a',encoding=response.encoding)
						writer = csv.writer(f)
						writer.writerow([bs.find('span',  attrs={'itemprop': 'name'}).text,res.find('span',  attrs={'class': 'no_sex'}).text,res.find('span').text,res.find('div',  attrs={'class': 'inline', 'itemprop': 'reviewBody'}).text])
						f.close()
					if res.find('span',  attrs={'class': 'man'}):
#						result.append([bs.find('span',  attrs={'itemprop': 'name'}).text,res.find('span',  attrs={'class': 'no_sex'}).text,res.find('span'),res.find('div',  attrs={'class': 'inline', 'itemprop': 'reviewBody'})])
						f = open('text/text_all_g2.txt', 'a',encoding=response.encoding)
						writer = csv.writer(f)
						writer.writerow([bs.find('span',  attrs={'itemprop': 'name'}).text,res.find('span',  attrs={'class': 'man'}).text,res.find('span').text,res.find('div',  attrs={'class': 'inline', 'itemprop': 'reviewBody'}).text])
						f.close()

					if res.find('span',  attrs={'class': 'woman'}):
#						result.append([bs.find('span',  attrs={'itemprop': 'name'}).text,res.find('span',  attrs={'class': 'no_sex'}).text,res.find('span'),res.find('div',  attrs={'class': 'inline', 'itemprop': 'reviewBody'})])						
						f = open('text/text_all_g2.txt', 'a',encoding=response.encoding)
						writer = csv.writer(f)
						writer.writerow([bs.find('span',  attrs={'itemprop': 'name'}).text,res.find('span',  attrs={'class': 'woman'}).text,res.find('span').text,res.find('div',  attrs={'class': 'inline', 'itemprop': 'reviewBody'}).text])
						f.close()
				print(i)
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