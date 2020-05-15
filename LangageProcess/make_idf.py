# ファイルをオープンする
import csv
import re
from dc import Dc
from collections import Counter
import pandas as pd
import numpy as np
csv.field_size_limit(1000000000)

f = open("text/dc.txt", "r",encoding='utf-8')
# 行ごとにすべて読み込んでリストデータにする
reader = csv.reader(f)
f2 = open("text/ct.txt", "r",encoding='utf-8')
# 行ごとにすべて読み込んでリストデータにする
vc = csv.reader(f2)
lis = []
# 一行ずつ表示する
#"[]","[]"
ga = []
hy = []
te = []
vca = []
c = 0
for row in reader:
	if row == []:
		pass
	else:
		lis.append(row[1:])

for v in vc:
	c = 0
	if v == []:
		pass
	else:
		pass
		for x in lis:
			if v[0] in x:
				c += 1
		f2 = open("text/df.txt", "a",encoding='utf-8')
		f2.write("{},{}\n".format(v[0],c))
		f2.close()