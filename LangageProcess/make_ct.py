# ファイルをオープンする
import requests
import numpy as np
import csv
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer
import re
import gensim
from gensim.corpora import Dictionary
import cchardet
from collections import Counter
import pandas as pd

f = open("text/dc2.txt", "r",encoding='utf-8')
# 行ごとにすべて読み込んでリストデータにする
reader = csv.reader(f)
csv.field_size_limit(1000000000)
lis = []
# 一行ずつ表示する
#"[]","[]"
ga = ''
na = ''
dc=[]
N = 0
t = Tokenizer()
stwd =['「','」',',','"','【','】','年月日','点','年','月','日','ツイート','リンク','コピー','サイト','埋め込む','インスタグラム','フォロー','アカウント','リツイート','スレッド','Twitter','twitter','返信','件','コメント','投稿','更新','|','(',')','レビュー','()','[',']','円']
# 一行ずつ表示する
#"[]","[]"
for row in reader:
	if row == []:
		pass
	else:
	#	if po.search(row[3]):
		N += 1 
		lis.extend(row[1:])
for k,v in Counter(lis).most_common():
	f2 = open("text/ct.txt", "a",encoding='utf-8')
	f2.write("{},{}\n".format(k,int(v))+'\n')
	f2.close()
print(N)
#6172
#		result = bs.find_all('td',  attrs={})	
#for k,v in Counter(lis).most_common():
#	f2 = open("text/ct.txt", "a",encoding='utf-8')
#	f2.write("{},{}\n".format(k,v))
#	f2.close()
#[[],[],[]]