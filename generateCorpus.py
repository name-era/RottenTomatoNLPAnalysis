import pandas as pd

#csvデータの読み込み
data = pd.read_csv("./sf150.csv", header=None)
#前処理
#Critics Consensus: を削除する
for i in range(len(data)):
    data.values[i][1] = data.values[i][1].lstrip("Critics Consensus: ")
    data.values[i][1] = data.values[i][1]+"\n"

#コーパス作成用の全てのテキストを連結した.txtファイルを作成する
txt=""
for i in range(len(data)):
    txt+=data.values[i][1]
#改行削除
txt = txt.replace("0", "")
txt = txt.replace("\n"," ")
txt = txt.replace(".", "")
txt = txt.replace(",", "")
txt = txt.lower()
f=open("corpus.txt", "w")
f.write((txt))

