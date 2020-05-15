# ファイルをオープンする
f = open("text/list.txt", "r",encoding='utf-8')

# 行ごとにすべて読み込んでリストデータにする
lines = f.read()
lis = []
# 一行ずつ表示する
f2 = open("text/list.txt", "w",encoding='utf-8')
f2.write(lines.replace('","','\n').replace('[','').replace(']','').replace('"',''))
#"[]","[]"