from gensim.models import word2vec
import pandas as pd
import numpy as np

path = "./corpus.txt"
sentences = word2vec.LineSentence(path)

#分散表現を求める
model = word2vec.Word2Vec(sentences, sg=1, vector_size=200, min_count=1, window=3)
model.save("./movie.model")

#ベクトル化する
#csvデータの読み込み
data = pd.read_csv("./sf150.csv", header=None)
for i in range(len(data)):
    data.values[i][1] = data.values[i][1].lstrip("Critics Consensus: ")

model = word2vec.Word2Vec.load("./movie.model")
#0行目は削除
for i in range(1, len(data)):
    #ベクトル用のarray
    vec = np.zeros(200)
    #各作品の文を読み込む
    sentense = data.values[i][1].split()

    for word in sentense:
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.lower()
        try:
            vec += model.wv[word]
        except KeyError:
            print(word+" is not exist in the list")

    vec= vec.tolist()
    data.values[i][1] = vec

#Ghost in the ShellとAkiraの類似度を計算する
similarity = np.dot(data.values[131][1], data.values[124][1])/(np.linalg.norm(data.values[131][1])*np.linalg.norm(data.values[124][1]))
print(similarity)

#2つの映画から類似度の高い映画を求める
input_vector = np.array(data.values[136][1])+np.array(data.values[143][1])
max_similarity=0
index=0
for i in range(1, len(data.values)):
    similarity = np.dot(input_vector, np.array(data.values[i][1]))/(np.linalg.norm(input_vector)*np.linalg.norm(data.values[i][1]))
    if max_similarity < similarity:
        max_similarity = similarity
        index = i

print("high similar movie is " + data.values[index][0] + ". similarity is " + str(max_similarity))


