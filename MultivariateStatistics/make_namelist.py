# ファイルをオープンする
import csv
import re
from dc import Dc
from collections import Counter
f = open("text/w/set.txt", "r",encoding='utf-8')
# 行ごとにすべて読み込んでリストデータにする
reader = csv.reader(f)
lis = []
# 一行ずつ表示する
#"[]","[]"
ga = []
na =  []
lis_n = []
po = re.compile(r'\/\sプロバイダ')
for row in reader:
	if row == []:
		pass
	else:
		if row[1] not in ga:
#			na.append(row[1])
#			f2 = open("text/w/name.txt", "a",encoding='utf-8')
#			f2.write(row[1]+'\n')
#			f2.close()
			ga.append(row[1])
			f3 = open("text/w/name.txt", "a",encoding='utf-8')
			f3.write(row[1]+'\n')
			f3.close()
