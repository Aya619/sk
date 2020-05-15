# ファイルをオープンする
import csv
import re
from dc import Dc
from collections import Counter
f = open("text/text_all_g2.txt", "r",encoding='utf-8')
# 行ごとにすべて読み込んでリストデータにする
reader = csv.reader(f)
lis = []
# 一行ずつ表示する
#"[]","[]"
ga = ''
na =  []
na1 =  []
na2 =  []
na3 =  []
na4 =  []
na5 =  []
na6 =  []
lis_n = []
po = re.compile(r'\/\sプロバイダ')
for row in reader:
	if row == []:
		pass
	else:
		if row[2] == 'とても良い(+2 pnt)':
				na.append(row[0])
				f2 = open("text/vg/set.txt", "a",encoding='utf-8')
				f2.write(row[0]+','+row[1]+'\n')
				f2.close()
		elif row[2] == '良い(+1 pnt)':
				na1.append(row[0])
				f2 = open("text/g/set.txt", "a",encoding='utf-8')
				f2.write(row[0]+','+row[1]+'\n')
				f2.close()
		elif row[2] == '最高(+3 pnt)':
				na2.append(row[0])
				f2 = open("text/v/set.txt", "a",encoding='utf-8')
				f2.write(row[0]+','+row[1]+'\n')
				f2.close()
		elif row[2] == '普通':
				na3.append(row[0])
				f2 = open("text/n/set.txt", "a",encoding='utf-8')
				f2.write(row[0]+','+row[1]+'\n')
				f2.close()
		elif row[2] == '悪い(-1 pnt)':
				na4.append(row[0])
				f2 = open("text/b/set.txt", "a",encoding='utf-8')
				f2.write(row[0]+','+row[1]+'\n')
				f2.close()
		elif row[2] == '最悪(-3 pnt)':
				na5.append(row[0])
				f2 = open("text/w/set.txt", "a",encoding='utf-8')
				f2.write(row[0]+','+row[1]+'\n')
				f2.close()
		elif row[2] == 'とても悪い(-2 pnt)':
				na6.append(row[0])
				f2 = open("text/vb/set.txt", "a",encoding='utf-8')
				f2.write(row[0]+','+row[1]+'\n')
				f2.close()
