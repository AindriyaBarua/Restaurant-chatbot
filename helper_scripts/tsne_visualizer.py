# from sklearn.manifold import TSNE
# import json
# import numpy as np
# from sklearn.cluster import KMeans
#
# # embedded data has fasttext vectors of the sentences
# with open("embedded_data_short.json") as file:
#     data = json.load(file)
#
# X = []
#
# for intent in data['intents']:
#
#     for pattern in intent['patterns']:
#       if not (intent['tag'] == 'general'):
#         pattern = np.array(pattern)
#         X.append(pattern)
#
#
# clusters = KMeans(n_clusters=5)
# clusters.fit(X)
#
# tsne = TSNEVisualizer()
# tsne.fit(X, ["c{}".format(c) for c in clusters.labels_])
# tsne.poof()
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import json
import numpy as np
from sklearn.cluster import KMeans

# embedded data has fasttext vectors of the sentences
with open("embedded_data_short.json") as file:
    data = json.load(file)

X = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        if not (intent['tag'] == 'general'):
            pattern = np.array(pattern)
            X.append(pattern)

clusters = KMeans(n_clusters=5)
clusters.fit(X)

X = np.array(X)  # 转换 X 为 NumPy 数组，以确保它有正确的形状

# 使用 TSNE 进行降维
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X)

# 获取每个点的聚类标签
labels = clusters.labels_

# 绘制 t-SNE 可视化结果
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=labels, cmap='jet', alpha=0.5)
plt.colorbar(ticks=range(5))
plt.clim(-0.5, 4.5)
plt.show()
