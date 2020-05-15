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
import decimal
decimal.getcontext().prec = 6
n = {}
gy = {}
eig = {}
jyu = []
ei = []
i = 0
j = 0
g = 0
c = 0
c2 = 0
f = open("text/w/game.txt", "r",encoding='utf-8')
# 行ごとにすべて読み込んでリストデータにする
reader = csv.reader(f)
for y in reader:
	gy.update({y[0]:i})
	i += 1
f2 = open("text/w/name.txt", "r",encoding='utf-8')
# 行ごとにすべて読み込んでリストデータにする
reader2 = csv.reader(f2)
for x in reader2:
	n.update({x[0]:j})
	j += 1
f3 = open("text/w/set.txt", "r",encoding='utf-8')
# 行ごとにすべて読み込んでリストデータにする
reader3 = csv.reader(f3)
Ze = np.zeros((j,i), dtype = int)
#print(i)
#i:805 j:374
for z in reader3:
	if z == []:
		pass
	else:
		pass
#		print(n[z[1]])
		Ze[n[z[1]]][gy[z[0]]] = 1
#print(Ze[373][804])
g = 0
Ge = np.zeros((i,i))
for k in range(0,i):
	for m in range(0,i):
		g = 0
		for l in range(0,j):
			g += Ze[l][k]*Ze[l][m]/np.count_nonzero(Ze == 1, axis=1)[l]
		Ge[k][m] = g/np.sqrt(np.count_nonzero(Ze == 1, axis=0)[k]*np.count_nonzero(Ze == 1, axis=0)[m])
for e in np.linalg.eig(Ge)[0]:
	eig.update({c:e})
	c += 1
dic = sorted(eig.items(),key=lambda x:x[1],reverse = True)
for d in dic:
	jyu.append(d[0])
	ei.append(d[1])
zv = np.linalg.eig(Ge)[1]
for w in jyu:
	for v in range(0,i):
		zv[v][c2] = round(zv[v][w]*np.sqrt(np.count_nonzero(Ze == 1)/np.count_nonzero(Ze == 1, axis=0)[v]),10)
	c2 += 1
for p in ei:
	f3 = open("text/w/eig.csv", "a",encoding='utf-8')
	# 行ごとにすべて読み込んでリストデータにする
	writer = csv.writer(f3)
	writer.writerow([p])
	f3.close()

for q in zv:
	f4 = open("text/w/w.csv", "a",encoding='utf-8')
	# 行ごとにすべて読み込んでリストデータにする
	writer = csv.writer(f4)
	writer.writerow(q)
	f4.close()
# i:6175 j:6173
# 一行ずつ表示する
#"[]","[]"
"""
c_n = 0
c_g = 0
c_b = 0
c_vg = 0
c_vb = 0
c_v = 0
c_w = 0
		if row[2] == '普通':
		if row[2] == '良い(+1 pnt)':
		if row[2] == '悪い(-1 pnt)':
		if row[2] == 'とても良い(+2 pnt)':
		if row[2] == 'とても悪い(-2 pnt)':
		if row[2] == '最高(+3 pnt)':
		if row[2] == '最悪(-3 pnt)':
"""